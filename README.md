# VisdeurBot-YOLO

VisdeurBot is an AI model created to help identify fish travelling through the Weerdsluis canal of Utrecht, created using the [jetson-inference](https://github.com/dusty-nv/jetson-inference) packages for the Nvidia Jetson Orin Nano SoM. This repository is a fork of the original, using [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) to be compatible on the latest Jetson systems and other computers.

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
 
# Installing dependencies

General installations will require the `ultralytics`, `numpy` and `scipy` packages:
```
pip install ultralytics[export]
pip install --upgrade numpy==1.26.4
pip install --upgrade scipy==1.15.3
sudo reboot
```

**Jetson-specific dependencies**


For Jetson systems running JetPack 6.x, the `torch`, `torchvision` and `onnxruntime-gpu` packages must be installed from the Ultralytics repository:
```
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torch-2.5.0a0+872d972e41.nv24.08-cp310-cp310-linux_aarch64.whl
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torchvision-0.20.0a0+afc54f7-cp310-cp310-linux_aarch64.whl
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/onnxruntime_gpu-1.23.0-cp310-cp310-linux_aarch64.whl
```
Due to a dependency issue, the `cuSPARSElt` package must also be installed from the Nvidia repository:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/arm64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install libcusparselt0 libcusparselt-dev
```


# How to use
Clone and enter the Git repository: 
```
git clone https://github.com/Exist-nt/VisdeurBot-YOLO.git
cd VisdeurBot-YOLO
```
Download the `visdeurbot-yolo.pt` package from the [Releases](https://github.com/Exist-nt/VisdeurBot-YOLO/releases) tab, and move it to your working VisdeurBot-YOLO folder.

Run the detection script:

**For CUDA devices:**
```
python3 run-cuda.py path/to/input path/to/output
```

**For Apple Silicon devices:**
```
python3 run-mps.py path/to/input path/to/output
```

**For any other devices (CPU inference):**
> This method is not recommended for speed reasons, but it will work.
```
python3 run-cpu.py path/to/input path/to/output
```


The AI will then run on the given image, outputting data in the terminal as well as saving the output at the specified location.
> NOTE: Sample images are provided in `images/`
