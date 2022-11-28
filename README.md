# SkinCancerDetection
A Deep Learning project where we attempted to detect skin cancer using the images of the skin. We used the ISIC Archives for our dataset and fine tuned the MobileNet pretrained model to make predictions. 

# Contributions:

Bharatan Mudaliar: https://github.com/bharat029

Kunjal Panchal: https://github.com/astuary 

# Dataset:

https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000

# Files:

1. MobileNetFineTuning.ipynb

This python notebook is the final compilation of this project, where we order the code cells in the order of the machine learning pipeline.

2. images.py  

This script performs all data augmentations and separates the data into train/test/validation data sets.

3. sorting_data.py

This script separates images belonging to separate classes into separate folders.

4. try.py

This script tests the behaviour for a baseline model to compare the project against.

# Setup and How to Run:

1. Download dataset and extract into the source file.
2. Run the images.py script
3. Run the sorting_data.py script
4. Run the MobileNetFineTuning.ipynb till the last cell
