
# 🌲 JagaPawana REST API - Sistem Pemantauan Karhutla & AQI Kalimantan

JagaPawana adalah layanan REST API backend berbasis Flask yang dirancang untuk memantau titik *hotspot* kebakaran hutan dan lahan (karhutla) serta kualitas udara (AQI) di wilayah Kalimantan secara *real-time*.

---

## 🚀 Link Deployment Vercel
- **Base URL**: `https://jaga-pawana-flaskrestapi.vercel.app`
- **Main Endpoint (Hotspot)**: `https://jaga-pawana-flaskrestapi.vercel.app/hotspot`

---

## 🗄️ Skema Database (ERD)
Database PostgreSQL di Supabase terdiri dari **6 tabel berelasi** menggunakan *foreign key*:
1. **`wilayah`** (Master data kabupaten/kota lokasi pemantauan)
2. **`sensor_kualitas_udara`** (Data perangkat sensor AQI per wilayah)
3. **`kualitas_udara`** (Histori indeks kualitas udara/PM2.5)
4. **`titik_hotspot`** (Data lokasi karhutla, suhu permukaan, & tingkat kepercayaan)
5. **`laporan_warga`** (Data kejadian karhutla yang dilaporkan masyarakat)
6. **`penanganan_kebakaran`** (Log tindakan & status pemadaman oleh tim respon)

**Relasi:**
`wilayah` ──< `titik_hotspot` ──< `penanganan_kebakaran`  
`wilayah` ──< `sensor_kualitas_udara` ──< `kualitas_udara`  
`wilayah` ──< `laporan_warga`

---

## 📡 Dokumentasi Pemanggilan API

### 1. Health Check / Root Index
- **Method**       : `GET`
- **URL**          : `https://jaga-pawana-flaskrestapi.vercel.app/`
- **Deskripsi**    : Mengecek status aktif aplikasi backend.
- **Headers**      : `Content-Type: application/json`
- **Request Body** : (Tidak ada)
- **Response Sukses (200 OK)**:
  ```json
  {
    "status": "success",
    "message": "Selamat datang di REST API JagaPawana - Sistem Pemantauan Karhutla & AQI Kalimantan"
  }
  ```
- **Response Error (500 Internal Server Error)**:
  ```json
  {
    "status": "error",
    "message": "Terjadi kesalahan pada server"
  }
  ```

---

### 2. Get All Hotspots (Read List)
- **Method**       : `GET`
- **URL**          : `https://jaga-pawana-flaskrestapi.vercel.app/hotspot`
- **Deskripsi**    : Mengambil seluruh data titik hotspot kebakaran hutan beserta relasi nama wilayahnya.
- **Headers**      : `Content-Type: application/json`
- **Request Body** : (Tidak ada)
- **Response Sukses (200 OK)**:
  ```json
  {
    "status": "success",
    "data": [
      {
        "id_hotspot": 1,
        "id_wilayah": 1,
        "nama_wilayah": "Palangkaraya",
        "latitude": -2.235,
        "longitude": 113.95,
        "suhu_permukaan": 52.8,
        "tingkat_kepercayaan": 95,
        "status_api": "Proses Pemadaman"
      },
      {
        "id_hotspot": 2,
        "id_wilayah": 1,
        "nama_wilayah": "Palangkaraya",
        "latitude": -2.18,
        "longitude": 113.88,
        "suhu_permukaan": 45.3,
        "tingkat_kepercayaan": 88,
        "status_api": "Aktif"
      }
    ]
  }
  ```
- **Response Error (500 Internal Server Error)**:
  ```json
  {
    "status": "error",
    "message": "Gagal terhubung ke database Supabase"
  }
  ```

---

### 3. Get Detail Hotspot (Read Detail)
- **Method**       : `GET`
- **URL**          : `https://jaga-pawana-flaskrestapi.vercel.app/hotspot/1`
- **Deskripsi**    : Mengambil detail data satu titik hotspot berdasarkan `id_hotspot`.
- **Headers**      : `Content-Type: application/json`
- **Request Body** : (Tidak ada)
- **Response Sukses (200 OK)**:
  ```json
  {
    "status": "success",
    "data": {
      "id_hotspot": 1,
      "id_wilayah": 1,
      "nama_wilayah": "Palangkaraya",
      "latitude": -2.235,
      "longitude": 113.95,
      "suhu_permukaan": 52.8,
      "tingkat_kepercayaan": 95,
      "status_api": "Proses Pemadaman"
    }
  }
  ```
- **Response Error (404 Not Found)**:
  ```json
  {
    "status": "error",
    "message": "Data titik hotspot tidak ditemukan"
  }
  ```

---

### 4. Create Hotspot (Create)
- **Method**       : `POST`
- **URL**          : `https://jaga-pawana-flaskrestapi.vercel.app/hotspot`
- **Deskripsi**    : Menambahkan titik hotspot kebakaran baru.
- **Headers**      : `Content-Type: application/json`
- **Request Body** :
  ```json
  {
    "id_wilayah": 1,
    "latitude": -2.210,
    "longitude": 113.92,
    "suhu_permukaan": 48.5,
    "tingkat_kepercayaan": 90,
    "status_api": "Aktif"
  }
  ```
- **Response Sukses (201 Created)**:
  ```json
  {
    "status": "success",
    "message": "Titik hotspot berhasil ditambahkan",
    "data": {
      "id_hotspot": 4,
      "id_wilayah": 1,
      "suhu_permukaan": 48.5,
      "status_api": "Aktif"
    }
  }
  ```
- **Response Error (400 Bad Request)**:
  ```json
  {
    "status": "error",
    "message": "Field id_wilayah, latitude, dan longitude wajib diisi"
  }
  ```

---

### 5. Update Hotspot (Update)
- **Method**       : `PUT`
- **URL**          : `https://jaga-pawana-flaskrestapi.vercel.app/hotspot/1`
- **Deskripsi**    : Memperbarui data titik hotspot yang sudah ada.
- **Headers**      : `Content-Type: application/json`
- **Request Body** :
  ```json
  {
    "suhu_permukaan": 35.0,
    "status_api": "Padam Total"
  }
  ```
- **Response Sukses (200 OK)**:
  ```json
  {
    "status": "success",
    "message": "Data titik hotspot berhasil diperbarui",
    "data": {
      "id_hotspot": 1,
      "suhu_permukaan": 35.0,
      "status_api": "Padam Total"
    }
  }
  ```
- **Response Error (404 Not Found)**:
  ```json
  {
    "status": "error",
    "message": "Data titik hotspot yang akan diubah tidak ditemukan"
  }
  ```

---

### 6. Delete Hotspot (Delete)
- **Method**       : `DELETE`
- **URL**          : `https://jaga-pawana-flaskrestapi.vercel.app/hotspot/1`
- **Deskripsi**    : Menghapus data titik hotspot berdasarkan ID.
- **Headers**      : `Content-Type: application/json`
- **Request Body** : (Tidak ada)
- **Response Sukses (200 OK)**:
  ```json
  {
    "status": "success",
    "message": "Titik hotspot berhasil dihapus"
  }
  ```
- **Response Error (404 Not Found)**:
  ```json
  {
    "status": "error",
    "message": "Data titik hotspot tidak ditemukan"
  }
  ```