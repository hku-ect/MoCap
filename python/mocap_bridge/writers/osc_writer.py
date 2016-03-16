from mocap_bridge.utils.color_terminal import ColorTerminal

try:
    import OSC
except ImportError:
    ColorTerminal().fail("Error importing library, please install pyOSC by running: sudo pip install pyOSC")

class OscWriter:
    def __init__(self, host="127.0.0.1", port=8080, manager=None, autoStart=True):
        self.host = host
        self.port = port

        self.client = None
        self.running = False
        self.manager = manager

        if self.manager != None:
            # the event class already discards duplicates, so no need to check
            self.manager.updateEvent += self.onUpdate

        if autoStart == True:
            self.start()

    def connect(self):
        try:
            self.client = OSC.OSCClient()
            self.client.connect((self.host, int(self.port)))
        except OSC.OSCClientError as err:
            ColorTerminal().error("OSC connection failure: {0}".format(err))
            return False

        return True

    def disconnect(self):
        if hasattr(self, 'client') and self.client:
            self.client.close()
            self.client = None

    def start(self):
        if self.connect():
            ColorTerminal().success("OSC client connected to " + self.host + ':' + str(self.port))

        self.running = True

    def stop(self):
        self.disconnect()
        ColorTerminal().success("OSC client closed")
        self.running = False

    def onUpdate(self, manager):
        if not self.running:
            return

        for rigid_body in self.manager.allRigidBodies():
            self._sendMessage("/rigidbody", rigid_body.toJSON())

    def _sendMessage(self, tag, content):
        msg = OSC.OSCMessage()
        msg.setAddress(tag) # set OSC address
        msg.append(content)

        try:
            self.client.send(msg)
        except OSC.OSCClientError as err:
            pass
            # ColorTerminal().warn("OSC failure: {0}".format(err))
            # no need to call connect again on the client, it will automatically
            # try to connect when we send ou next message

    def configure(self, host=None, port=None):
        if host:
            self.host = host
        if port:
            self.port = port

        if (host or port) and self.running:
            self.stop()
            self.start()
