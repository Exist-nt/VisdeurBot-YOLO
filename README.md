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
This model must be run on an Nvidia Tegra system with the latest release of L4T Ubuntu, Cuda, and the Ultralytics package installed.

To install the ultralytics package:
```
pip install ultralytics[export]
sudo reboot
```
The above command will install the PyTorch and TorchVision packages, however these are not built for Jetson systems.
To install the correct versions of these packages:
```
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torch-2.5.0a0+872d972e41.nv24.08-cp310-cp310-linux_aarch64.whl
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torchvision-0.20.0a0+afc54f7-cp310-cp310-linux_aarch64.whl
```
This software also requires NumPy 1.26.4 and SciPy 1.15.3. 
To upgrade/downgrade these packages:
```
pip install --upgrade numpy==1.26.4
pip install --upgrade scipy==1.15.3
```

# How to use
Clone and enter the Git repository: 
```
git clone https://github.com/Exist-nt/VisdeurBot-YOLO.git
cd VisdeurBot-YOLO
```

Run the detection script:
```
python3 run.py path/to/input
```
The AI will then run on the given image, outputting data in the terminal as well as saving the output at `runs/detect/predict#/*.jpg`
> NOTE: Sample images are provided in `images/`
