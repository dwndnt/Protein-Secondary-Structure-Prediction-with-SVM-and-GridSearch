# SVM Optimization for Protein Secondary Structure Prediction with GridSearch Validation
Program ini bertujuan untuk mengoptimalkan algoritma Support Vector Machine (SVM) dalam memprediksi struktur sekunder protein. Program ini menggunakan metode GridSearch Validation untuk menemukan parameter SVM yang optimal, sehingga dapat meningkatkan akurasi prediksi struktur sekunder protein. Dengan kata lain, program ini bertujuan untuk meningkatkan kualitas prediksi struktur sekunder protein dengan mengatur parameter SVM secara otomatis melalui proses penalaan parameter.

## Deskripsi Program:

Program ini membaca data dari file 'Data_RS126.txt', di mana file ini berisi sekuensi protein primer dan struktur sekunder yang sesuai. Data ini digunakan untuk melatih model prediksi struktur sekunder protein.

1.Program membaca data protein primer dan struktur sekunder dari file 'Data_RS126.txt' dan menyimpannya ke dalam dua list, yaitu raw_primary dan raw_secondary.

2.Kemudian program memeriksa apakah panjang setiap sekuensi protein primer dan struktur sekunder sesuai. Jika ada yang tidak sesuai, program akan mencetak informasi tentang sekuensi yang tidak sesuai.

3.Program menghapus data yang tidak sesuai dari list raw_primary dan raw_secondary.

4.Selanjutnya, program menghitung jumlah karakter dalam semua sekuensi protein primer dan struktur sekunder.

5.Program melakukan konversi sekuensi protein primer dan struktur sekunder menjadi representasi vektor dengan menggunakan fungsi orthogonal_pri dan orthogonal_sec.

6.Program menggabungkan vektor-vektor yang dihasilkan dari langkah sebelumnya menjadi data yang akan digunakan sebagai fitur (X) dan label (Y) dalam pemodelan.

7.Program membagi data menjadi data pelatihan dan data pengujian menggunakan train_test_split.

8.Program membangun model klasifikasi menggunakan algoritma SVM (Support Vector Machine) dengan kernel rbf. Kemudian, program melakukan penalaan parameter SVM menggunakan GridSearchCV untuk mencari parameter yang optimal.

9.Hasil dari penalaan parameter dicetak ke layar, termasuk parameter terbaik yang ditemukan.

## Cara Menggunakan Program:

1. Pastikan Anda memiliki file 'Data_RS126.txt' yang berisi data sekuensi protein primer dan struktur sekunder.

2. Jalankan program ini di lingkungan Python yang sesuai.

3. Program akan membaca data dari file dan melakukan pemodelan prediksi struktur sekunder protein.

4. Hasil penalaan parameter dan performa model akan dicetak ke layar.

## Dependensi:

- Python 3.x
- NumPy
- Scikit-learn


