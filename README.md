# ProjectTemplate

Status: Actively maintained. Any question or suggestion is welcome. Contact us by [email](mailto:yufeng_zheng@berkeley.edu?subject=[GitHub]%20Project%20Template) or raise an issue. We will give response within 48 hours.

Start your next deep learning project with fundamental experiment management scripts.

This is a basement folder for a new research project. I have implemented some simple yet necessary scripts for running a deep learning experiment. When starting a new project, you can get rid of the time consuming part which is basically implementing these functions repetitively.



## Usage

Simply replace the existing folder path and other settings to yours. Pick the code snippets that you need. Example usages are provided in the main.py file.



## Features & TODOs

- [x] Python script for setting result logging folder and copying source code to the result folder
- [x] Python script will also create a 'Experiment information.txt' in the result folder, which contains
  1. The python command line input to start the experiment
  2. The time when starting the experiment
  3. The original path of the script
- [x] A function to automatically set PyTorch device
  - [x] If no GPU, use CPU
  - [x] If multiple GPUs are available, automatically select the most 'idle' one.
- [x] A decorator for saving original visualization data while plotting figures.
- [x] A class for monitoring memory usage.
- [ ] Python `argparse` template.
- [ ] A bash script for run a series of jobs and keeping system workload within a certain level.
- [ ] A simple bash script for syncing code and results between remote server and local machine with rsync.
- [ ] A sample jupyter notebook for reading and visualizing multiple tensorboard files together.
- [ ] A template for experiment management tools, such as [NNI](https://nni.readthedocs.io/).



If you have any comment and idea, please create a issue!
