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

  ```json
  {
    "status": "error",
    "message": "Terjadi kesalahan pada server"
  }