# Proyek Klasifikasi Gambar - Submission

## Deskripsi
Notebook ini membangun model CNN untuk klasifikasi gambar menggunakan TensorFlow/Keras.

## Dataset
- Struktur dataset: `dataset/train`, `dataset/val`, `dataset/test`
- Label kelas diambil dari nama folder di dalam masing-masing split.

## Model
- Keras Sequential
- Conv2D + Pooling
- Callback: EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

## Output yang dihasilkan
- `saved_model/` (SavedModel)
- `tflite/model.tflite` dan `tflite/label.txt`
- `tfjs_model/` (TFJS)

## Cara menjalankan
1. Pastikan dataset sudah berada di struktur folder yang benar.
2. Jalankan notebook dari atas sampai selesai.
3. Pastikan cell konversi TFJS dijalankan (install `tensorflowjs` jika perlu).
