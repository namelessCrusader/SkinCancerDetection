from PIL import Image
import os
from random import shuffle
from shutil import copy, move

def extract(dest):
    src = r'E:\SkinCancerDetection\PH2Dataset\PH2 Dataset images'
    list_src = os.listdir(src)
    len_src = len(list_src)
    for i in range(len_src):
        copy(src + '\\' + list_src[i] + '\\' + list_src[i] + '_Dermoscopic_Image\\' + list_src[i] + '.bmp', dest)
        print(i + 1, 'of', len_src)
        
def divide(src, dest, malignant_src):
    combo = os.listdir(src)
    malignant = os.listdir(malignant_src)
    len_combo = len(combo)
    for i in range(len_combo):
        if combo[i] in malignant:
            move(src + '\\' + combo[i], dest)
        print(i, 'of', len_combo)
    
def all_crops(src, dest):
    crop_images(src, dest, mode = 'center', size = 448)
    crop_images(src, dest, mode = 'top-left', size = 224)
    crop_images(src, dest, mode = 'top-right', size = 224)
    crop_images(src, dest, mode = 'bottom-right', size = 224)
    crop_images(src, dest, mode = 'bottom-left', size = 224)
    
def crop_images(src, dest, mode = 'center', size = None):
    list_of_images = os.listdir(src)
    total_data_size = len(list_of_images)

    for i in range(total_data_size):
        try:
            crop_img(src + '\\' + list_of_images[i], dest + "\\" + mode + '\\' + list_of_images[i], mode, size)
            print(i + 1, 'of', total_data_size, 'copied and cropped from', src, 'to', dest)
        except Exception as e:
            print(list_of_images[i], 'not copied')
            print(e)
    print('Copied everything from', src, 'to', dest)

def crop_img(imgsrc, imgdest, mode = 'center', size = None):
    im = Image.open(imgsrc)
    width, height = im.size
    
    if size is None and mode == 'center':
        dim = min(width, height)
    elif size is not None:
        dim = size
        
    if mode == 'center':
        left = (width - dim)/2
        top = (height - dim)/2
        right = (width + dim)/2
        bottom = (height + dim)/2
    elif mode == 'top-left':
        left = 0
        top = 0
        right = dim
        bottom = dim
    elif mode == 'top-right':
        left = width - dim
        top = 0
        right = width
        bottom = dim
    elif mode == 'bottom-right':
        left = width - dim
        top = height - dim
        right = width
        bottom = height
    elif mode == 'bottom-left':
        left = 0
        top = height - dim
        right = dim
        bottom = height
        
    im = im.crop((left, top, right, bottom))
    im.save(imgdest)    
    
def train_valid_test_split(src, train_dest, valid_dest, test_dest, dir_name):
    list_of_images = os.listdir(src)
    shuffle(list_of_images)
    total_data_size = len(list_of_images)
    num_of_train_images = 1820
    num_of_valid_images = 230
    
    for i in range(total_data_size):
        if i < num_of_train_images:
            copy(src + '\\' + list_of_images[i], train_dest + '\\' + dir_name) 
        elif i < num_of_train_images + num_of_valid_images:
            copy(src + '\\' + list_of_images[i], valid_dest + '\\' + dir_name) 
        else:
            copy(src + '\\' + list_of_images[i], test_dest + '\\' + dir_name) 
        print(i + 1, 'of', total_data_size, 'copied')
    print('Split completed from', src)

def moving_cropped(src, dest):
    main_dir = os.listdir(src)
    actual_dir = None
    
    for name_dir in main_dir:
        if name_dir.startswith('center'):
            actual_dir = src + '\\' + name_dir
            images = os.listdir(actual_dir)
            for image in images:
                pos = image.find('.')
                copy(actual_dir + '\\' + image, dest + '\\' + image[:pos] + '-' + name_dir + image[pos:] )
        print(name_dir)

benign_src = r'E:\SkinCancerDetection\Cropped\DiskFreeCrops'
malignant_src = r'E:\SkinCancerDetection\Malignant'
nb_src = r'E:\SkinCancerDetection\NB'
benign_dest = r'E:\SkinCancerDetection\Dataset\Benign'
malignant_dest = r'E:\SkinCancerDetection\Dataset\Malignant'
nb_dest = r'E:\SkinCancerDetection\Cropped\NewBenign'
train_dest = r'E:\SkinCancerDetection\Train'
valid_dest = r'E:\SkinCancerDetection\Valid'
test_dest = r'E:\SkinCancerDetection\Test'
new_data = r'E:\SkinCancerDetection\Data'
new_data_dest = r'E:\SkinCancerDetection\Cropped\Data'
diskfree_src = r'E:\SkinCancerDetection\New folder\benigndiskless'
diskfree_dest = r'E:\SkinCancerDetection\Cropped\DiskFreeCrops'
removable_src = r'E:\SkinCancerDetection\New folder\BenignSorted'
removable_dest = r'E:\SkinCancerDetection\Cropped\RemovableDisksCrops'
trial_dest = r'E:\SkinCancerDetection\Cropped\Center'

#moving_cropped(benign_src, benign_dest)
#all_crops(diskfree_src, diskfree_dest)
#copy_and_crop(removable_dest, trial_dest)
#copy_and_crop(nb_src, nb_dest)
#copy_and_crop(malignant_src, malignant_dest)
#train_valid_test_split(benign_dest, train_dest, valid_dest, test_dest, dir_name='Benign')
train_valid_test_split(malignant_dest, train_dest, valid_dest, test_dest, dir_name='Malignant')
#divide(nb_dest, malignant_dest, malignant_src)
#extract(new_data)

# for i in os.listdir(benign_dest)[:2280]:
#     move(benign_dest + '\\' + i, benign_dest_f + '\\' + i)
    
input('You are ready to go now!')