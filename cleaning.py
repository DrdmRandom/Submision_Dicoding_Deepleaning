import os
import shutil

dataset_path = "/home/dawwi/Dicoding/BDL_Submision2/dataset2"

# === 1. MERGE JELLYFISH ===
jellyfish_classes = [
    "blue_jellyfish",
    "compass_jellyfish",
    "barrel_jellyfish",
    "Moon_jellyfish",
    "mauve_stinger_jellyfish",
    "lions_mane_jellyfish"
]

merged_folder = os.path.join(dataset_path, "jellyfish")
os.makedirs(merged_folder, exist_ok=True)

for cls in jellyfish_classes:
    class_path = os.path.join(dataset_path, cls)
    
    if os.path.exists(class_path):
        for file in os.listdir(class_path):
            src = os.path.join(class_path, file)
            dst = os.path.join(merged_folder, file)
            
            # Rename jika ada nama file sama
            if os.path.exists(dst):
                base, ext = os.path.splitext(file)
                dst = os.path.join(merged_folder, base + "_merged" + ext)
            
            shutil.move(src, dst)
        
        # Hapus folder lama
        shutil.rmtree(class_path)

print("Merge jellyfish selesai.")

# === 2. DROP KELAS DENGAN DATA < 50 ===

valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

for class_name in os.listdir(dataset_path):
    class_path = os.path.join(dataset_path, class_name)
    
    if os.path.isdir(class_path):
        total_images = len([
            f for f in os.listdir(class_path)
            if f.lower().endswith(valid_extensions)
        ])
        
        if total_images < 50:
            shutil.rmtree(class_path)
            print(f"Kelas '{class_name}' dihapus karena hanya {total_images} gambar")

print("Proses selesai.")