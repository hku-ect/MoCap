# Python MOCAP tools

This repository contains a number of python MOCAP tools meant to receive the live [NATNET](http://optitrack.com/products/natnet-sdk/) data from [Motive](http://optitrack.com/products/motive/) and subsequently forward this data to [OSC](https://en.wikipedia.org/wiki/Open_Sound_Control) to be able to receive and use the data in various programs. The data is sent over OSC using [JSON](ttps://www.w3schools.com/js/js_json_intro.asp) notation.

* The tools are compatible with Python2 and Python3
* The tools send everything (Skeleton&Rigid Bodies) as rigid bodies
* The tools DO NOT send the names of the RigidBodies only the ID's
* The tools use the [optirx](https://pypi.python.org/pypi/optirx) python library
  * the optirx library is included in the source code
  * it uses a fork of the optirx library with some minor fixes [link](https://github.com/ikbenmacje/python-optirx)

A comprehensive MOCAP manual using these tools can be found at the [MOCAP_manual](https://github.com/hku-ect/MOCAP_manual) github repository of [HKU-ECT](https://github.com/hku-ect/)


### These tools consist of:


## Python MocapBridge

This software receives the [NATNET](http://optitrack.com/products/natnet-sdk/) data and sends it out with [OSC](https://en.wikipedia.org/wiki/Open_Sound_Control) as [JSON](https://www.w3schools.com/js/js_json_intro.asp).
For more information see the [python README](https://github.com/hku-ect/MoCap/blob/master/python/README.md)


## Cinema4D

Here you will find a Cinema4D example file with MOCAP [BVH](https://research.cs.wisc.edu/graphics/Courses/cs-838-1999/Jeff/BVH.html) example data. For more information see the [C4D README](https://github.com/hku-ect/Python-MOCAP-tools/blob/master/cinema4d/README.md)


## Unity

Here you will find Unity packages to help you use live MOCAP data in Unity. For more information see the [Unity README](https://github.com/hku-ect/Python-MOCAP-tools/blob/master/unity/README.md)


## Blender
Here you will find tools to work with the MOCAP data live in [Blender](https://www.blender.org/). For more information see the [blender README](https://github.com/hku-ect/Python-MOCAP-tools/blob/master/blender/README.md)

## Processing
Here you will find an example processing sketch which receives the [OSC](https://en.wikipedia.org/wiki/Open_Sound_Control) data and decodes the data. 