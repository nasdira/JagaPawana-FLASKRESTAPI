from app.extensions import db

class Wilayah(db.Model):
    __tablename__ = 'wilayah'
    
    id_wilayah = db.Column(db.Integer, primary_key=True)
    nama_wilayah = db.Column(db.String(100), nullable=False)
    provinsi = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Numeric(9, 6))
    longitude = db.Column(db.Numeric(9, 6))

    def to_dict(self):
        return {
            "id_wilayah": self.id_wilayah,
            "nama_wilayah": self.nama_wilayah,
            "provinsi": self.provinsi,
            "latitude": float(self.latitude) if self.latitude else None,
            "longitude": float(self.longitude) if self.longitude else None
        }

class TitikHotspot(db.Model):
    __tablename__ = 'titik_hotspot'
    
    id_hotspot = db.Column(db.Integer, primary_key=True)
    id_wilayah = db.Column(db.Integer, db.ForeignKey('wilayah.id_wilayah'), nullable=False)
    tingkat_kepercayaan = db.Column(db.Integer)
    suhu_permukaan = db.Column(db.Numeric(5, 2))
    latitude = db.Column(db.Numeric(9, 6))
    longitude = db.Column(db.Numeric(9, 6))
    status_api = db.Column(db.String(30))
    
    # Relasi ke Model Wilayah
    wilayah = db.relationship('Wilayah', backref='hotspots', lazy=True)

    def to_dict(self):
        return {
            "id_hotspot": self.id_hotspot,
            "id_wilayah": self.id_wilayah,
            "nama_wilayah": self.wilayah.nama_wilayah if self.wilayah else None,
            "tingkat_kepercayaan": self.tingkat_kepercayaan,
            "suhu_permukaan": float(self.suhu_permukaan) if self.suhu_permukaan else None,
            "latitude": float(self.latitude) if self.latitude else None,
            "longitude": float(self.longitude) if self.longitude else None,
            "status_api": self.status_api
        }