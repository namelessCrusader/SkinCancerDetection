import pandas as pd
from PIL import Image

# Open file with labels
df = pd.read_csv(r'D:\VA\Python Workspace\SkinCancerDetection\ISIC Dataset\NewDatasets\ISIC-images\metadata_5.csv')

# Isolate relevant feilds
df = df[['name', 'meta.clinical.benign_malignant']]
df.set_index('name', inplace=True)

# Load data into a Python Dictionary 
data = df.to_dict()['meta.clinical.benign_malignant']

# Designate Folder to save data to
frm = r'ISIC Dataset\NewDatasets\ISIC-images\UDA-1'
to_b = r'Data\Benign'
to_m = r'Data\Malignant'

b = 401
m = 639

# Save data into relevant folders
for k, v in data.items():
    if v == 'benign':
        img = Image.open(frm + "\\"  + k + ".jpg")
        b += 1
        img.save(to_b + "\\"  + str(b) + ".jpg")
    elif v == 'malignant':
        img = Image.open(frm + "\\"  + k + ".jpg")
        m += 1
        img.save(to_m + "\\"  + str(m) + ".jpg")
    print(k, ':', v)
    
print(b, ':', m)
