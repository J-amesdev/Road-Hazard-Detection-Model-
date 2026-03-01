import os
import random
import shutil

# Paths
image_dir = "data/processed/images/train"
label_dir = "data/processed/labels/train"
output_base = "data/processed"

# Define the split
split_ratio = {'train': 0.70, 'test': 0.20, 'val': 0.10}

def split_dataset():
    images = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))]
    random.shuffle(images)

    # Calculate split indices
    train_end = int(len(images) * split_ratio['train'])
    test_end = train_end + int(len(images) * split_ratio['test'])

    splits = {
        'train': images[:train_end],
        'test': images[train_end:test_end],
        'val': images[test_end:]
    }

    for split_name, split_images in splits.items():
        # Create folders
        os.makedirs(os.path.join(output_base, 'images', split_name), exist_ok=True)
        os.makedirs(os.path.join(output_base, 'labels', split_name), exist_ok=True)

        for img_name in split_images:
            # Move Image
            shutil.move(os.path.join(image_dir, img_name), 
                        os.path.join(output_base, 'images', split_name, img_name))
            
            # Move corresponding Label
            label_name = img_name.rsplit('.', 1)[0] + ".txt"
            if os.path.exists(os.path.join(label_dir, label_name)):
                shutil.move(os.path.join(label_dir, label_name), 
                            os.path.join(output_base, 'labels', split_name, label_name))

split_dataset()
print("70-20-10 Split Complete!")