import os

dataset_path = "/home/dawwi/Dicoding/BDL_Submision2/dataset2"
valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

class_counts = {}
total_dataset = 0

for class_name in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_name)
    
    if os.path.isdir(class_path):
        total_images = len([
            f for f in os.listdir(class_path)
            if f.lower().endswith(valid_extensions)
        ])
        
        class_counts[class_name] = total_images
        total_dataset += total_images

print("Jumlah data per kelas:")
for k, v in class_counts.items():
    print(f"{k}: {v}")

print("\nTotal seluruh dataset:", total_dataset)