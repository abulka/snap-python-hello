# Installing a different version of Python using Snapcraft

Proves you can deploy a Python 3.9 program as a snap, using `core20` which only comes with Python 3.8 built in.

Based on the thread https://forum.snapcraft.io/t/build-a-snap-with-any-version-of-python-i-want/10420/8

# Use

    snapcraft
    sudo snap install --devmode --dangerous *.snap

which will build and install the snap. Then to run it - twice with different entry points:

    andy-snap-python-hello
    andy-snap-python-hello.python-v

# Notes

The `$SNAP` reference

    command: bin/python3 $SNAP/src/main.py

refers to the prime directory, which is what is ultimately copied into the resulting snap file created.  The reference to python is `bin/python` which could be `$SNAP/bin/python3` as the location of the venv/bin directory seems to end up in the prime directory as `bin`.  The command could be simplified to

    command: bin/python3 src/main.py

confirmed.  That works.

## Verify the contents of the snap

    $ unsquashfs -l *.snap|less

where `squashfs-root/` is the `prime` directory during build.  E.g.

    squashfs-root
    squashfs-root/bin
    squashfs-root/bin/pip
    squashfs-root/bin/pip3
    squashfs-root/bin/pip3.9
    squashfs-root/bin/python
    squashfs-root/bin/python3
    squashfs-root/bin/python3.9
    squashfs-root/src/main.py
    etc.

After installation

    $ ls /snap/andy-snap-python-hello/

to see what is actually being copied to your file system from the .snap file - this is what is being ultimately run.

## core20 vs core18

Unfortunately I couldn't get it working with core18 since I got the error 

    Could not find a required package in 'build-packages': python3.9-venv

