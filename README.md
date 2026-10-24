# JagaPawana REST API - Sistem Pemantauan Karhutla & AQI Kalimantan

REST API backend untuk pemantauan titik hotspot kebakaran hutan dan kualitas udara (AQI) di Kalimantan.

## Link Deployment Vercel
https://jaga-pawana-flaskrestapi-9aisercmt-indirabe.vercel.app
	
## Skema Database (ERD)
Terdiri dari 6 tabel berelasi:
- `wilayah` (Master Data Wilayah)
- `sensor_kualitas_udara` (Relasi ke Wilayah)
- `kualitas_udara` (Histori AQI)
- `titik_hotspot` (Data Kebakaran Hutan)
- `laporan_warga` (Laporan Masarakat)
- `penanganan_kebakaran` (Log Tim Respon)

## Daftar Endpoint API
### 1. Get All Hotspots
- **Method**: GET
- **URL**: `https://jaga-pawana-flaskrestapi-9aisercmt-indirabe.vercel.app/hotspot`
- **Description**: Mengambil seluruh daftar titik hotspot karhutla beserta nama wilayah.
- **Response Success (200 OK)**:
  ```json
  {
    "status": "success",
    "data": [
      {
        "id_hotspot": 1,
        "id_wilayah": 1,
        "nama_wilayah": "Palangkaraya",
        "suhu_permukaan": 52.8,
        "tingkat_kepercayaan": 95,
        "status_api": "Proses Pemadaman"
      }
    ]
  }