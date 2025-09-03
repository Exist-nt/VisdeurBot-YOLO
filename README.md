# VisdeurBot-YOLO

VisdeurBot is an AI model created to help identify fish travelling through the Weerdsluis canal of Utrecht, created using the [jetson-inference](https://github.com/dusty-nv/jetson-inference) packages for the Nvidia Jetson Orin Nano SoM. This repository is a fork of the original, using Ultralytics YOLO to be compatible on the latest Jetson systems.

Learn more about the Fish Doorbell project [here](https://visdeurbel.nl) ([English link](https://visdeurbel.nl/en)).

See the AI in action [here](https://xistnt.neocities.org/projects/visdeurbel.html).

This model can detect the following species of fish, identified as being the most common to pass through the Weerdsluis:
- Alver (Common bleak)
- Baars (Perch)
- Blankvoorn (Common roach)
- Brasem (Common bream)
- Kolblei (White bream)
- Meerval (Wels catfish)
- Paling (European eel)
- Ruisvoorn (Common rudd)
- Snoek (Northern pike)
- Snoekbaars (Pikeperch)
- Winde (Ide)
 
# Dependencies
This model must be run on an Nvidia Tegra system with the jetson-inference packages and the latest release of L4T Ubuntu installed.

To build the jetson-inference packages:
```
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
mkdir build && cd build
cmake ../
```
It is recommended to install PyTorch when the option shows up at this step, although it can still be installed later.

Continue the setup as below:
```
make -j$(nproc)
sudo make install
sudo ldconfig
```

# How to use
Clone and enter the Git repository: 
```
git clone https://github.com/Exist-nt/VisdeurBot-YOLO.git
cd VisdeurBot-YOLO
```

Run the detection script:
> The full instructions still need to be completed for the YOLO model.

```
```

The AI will then take about 5 minutes to load the model to disk, and if everything goes right you will be able to watch the AI work in real-time in a separate window.

The input and output fields can be either video or photo files, but they must be in the same file format. 

> NOTE: The input can also be a camera device - usually found at /dev/video0. Use `v4l2-ctl --list-devices` (part of the `v4l-utils` package) to see attached cameras if /dev/video0 does not exist. 

You can also leave the output field blank, and the script will still display the results in real-time.
