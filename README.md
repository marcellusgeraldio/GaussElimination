# 🧮 **Gauss Elimination Solver**

*Dibuat oleh:* **Marcellus Geraldio Florenta (2702262816)**  
*Universitas Bina Nusantara – Computer Science*  

---

## 📘 **Deskripsi Proyek**

Program ini merupakan implementasi **metode eliminasi Gauss** (Gaussian Elimination) menggunakan bahasa **Python**.
Tujuannya adalah menyelesaikan sistem persamaan linear dengan menggunakan operasi baris elementer pada **matriks augmented** hingga didapatkan solusi untuk setiap variabel.

Metode ini umum digunakan dalam **Scientific Computing** dan **Numerical Analysis** untuk menyelesaikan sistem linear dengan efisien.

---

## ⚙️ **Fitur Utama**

✅ Menerima input matriks augmented secara manual dari pengguna  
✅ Melakukan **pivoting otomatis** jika elemen diagonal utama bernilai nol  
✅ Melakukan **normalisasi pivot** agar elemen diagonal bernilai 1  
✅ Melakukan **eliminasi maju (forward elimination)** untuk membuat bentuk segitiga atas  
✅ Melakukan **substitusi mundur (back substitution)** untuk mendapatkan solusi setiap variabel  
✅ Menangani kasus **sistem tidak konsisten** dengan pesan error yang sesuai  

---

## 🧩 **Struktur Program**

| Fungsi / Bagian                       | Deskripsi                                                                                    |
| ------------------------------------- | -------------------------------------------------------------------------------------------- |
| `gauss_elimination(augmented_matrix)` | Melakukan eliminasi Gauss lengkap (pivoting, normalisasi, eliminasi, dan substitusi mundur). |
| `main()`                              | Mengatur input dari pengguna, memvalidasi jumlah koefisien, dan menampilkan hasil akhir.     |
| `np.array()`                          | Mengubah list menjadi matriks numerik agar bisa dilakukan operasi matematis.                 |

---

## 🧠 **Langkah-Langkah Proses Gauss**

1. **Membentuk matriks augmented** dari input pengguna.
   Contoh sistem persamaan:

   ```
   2x + y - z = 8
   -3x - y + 2z = -11
   -2x + y + 2z = -3
   ```

   akan diinput sebagai:

   ```
   2 1 -1 8
   -3 -1 2 -11
   -2 1 2 -3
   ```

2. **Mencari pivot utama** (elemen diagonal yang tidak nol).
   Jika pivot bernilai nol, baris akan ditukar otomatis.

3. **Normalisasi baris pivot**, membuat nilai pivot menjadi 1.

4. **Eliminasi elemen di bawah pivot**, menghasilkan matriks segitiga atas.

5. **Substitusi mundur**, menghitung nilai variabel dari bawah ke atas.

6. **Menampilkan solusi akhir**, misalnya:

   ```
   Solusi untuk x1 = 2.0
   Solusi untuk x2 = 3.0
   Solusi untuk x3 = -1.0
   ```

---

## 💻 **Cara Menjalankan Program**

1. Pastikan Python dan library **NumPy** sudah terpasang.
   Jika belum, jalankan perintah:

   ```
   pip install numpy
   ```

2. Simpan program dengan nama `gauss_elimination.py`.

3. Jalankan di terminal:

   ```
   python gauss_elimination.py
   ```

4. Masukkan matriks augmented sesuai jumlah persamaan dan variabel.
   Misalnya untuk 3 variabel:

   ```
   Masukkan matriks augmented:
   2 1 -1 8
   -3 -1 2 -11
   -2 1 2 -3
   ```

---

## 🧾 **Contoh Output**

```
Masukkan matriks augmented:
2 1 -1 8
-3 -1 2 -11
-2 1 2 -3

Solusi untuk x1 = 2.0
Solusi untuk x2 = 3.0
Solusi untuk x3 = -1.0
```

---

## 🧠 **Konsep Pemrograman yang Digunakan**

* **NumPy Array** – untuk efisiensi operasi matriks.
* **Perulangan (loop)** – untuk melakukan eliminasi dan substitusi.
* **Kondisi (if-else)** – untuk mendeteksi pivot nol atau sistem tidak konsisten.
* **Fungsi modular** – membagi proses menjadi `gauss_elimination()` dan `main()` agar mudah dibaca.

---

## 🎯 **Tujuan Proyek**

Proyek ini bertujuan untuk:

* Melatih pemahaman tentang **metode numerik dalam sistem persamaan linear**.
* Menunjukkan penerapan **operasi baris elementer** dalam komputasi ilmiah.
* Meningkatkan kemampuan penggunaan **NumPy** untuk operasi matriks di Python.

---
