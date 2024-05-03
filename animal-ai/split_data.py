import os
import shutil
from sklearn.model_selection import train_test_split

current_script_path = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(current_script_path, 'animal_data')
print(data_dir)

categories = os.listdir(data_dir)

train_dir = os.path.join(current_script_path, 'training')
test_dir = os.path.join(current_script_path, 'testing')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for category in categories:
    category_path = os.path.join(data_dir, category)
    images = os.listdir(category_path)
    
    train_cat_dir = os.path.join(train_dir, category)
    test_cat_dir = os.path.join(test_dir, category)
    os.makedirs(train_cat_dir, exist_ok=True)
    os.makedirs(test_cat_dir, exist_ok=True)
    
    train_imgs, test_imgs = train_test_split(images, test_size=0.1, random_state=42)
  
    for img in train_imgs:
        shutil.copy(os.path.join(category_path, img), os.path.join(train_cat_dir, img))
    for img in test_imgs:
        shutil.copy(os.path.join(category_path, img), os.path.join(test_cat_dir, img))
