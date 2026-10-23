from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.jagapawana import TitikHotspot

hotspot_bp = Blueprint('hotspot', __name__, url_prefix='/hotspot')

# Get: Ambil Semua Hotspot
@hotspot_bp.route('', methods=['GET'])
def get_all_hotspots():
    hotspot = TitikHotspot.query.all()
    return jsonify({
        "status": "success",
        "data": [h.to_dict() for h in hotspot]
    }), 200

# POST: Tambah Hotspot Baru
@hotspot_bp.route('', methods=['POST']) 
def create_hotspot():
    data = request.get_json() or {}
    if not data.get('id_wilayah'):
        return jsonify({"error": "id_wilayah wajib diisi"}), 400

    new_hotspot = TitikHotspot(
        id_wilayah=data.get('id_wilayah'),
        tingkat_kepercayaan=data.get('tingkat_kepercayaan', 80),
        suhu_permukaan=data.get('suhu_permukaan', 45.0),
        status_api=data.get('status_api', 'Aktif')
    )
    db.session.add(new_hotspot)
    db.session.commit()

    return jsonify({
        "message": "Data hotspot berhasil ditambahkan",
        "data": new_hotspot.to_dict()
    }), 201

# PUT: Update Status/Suhu Hotspot
@hotspot_bp.route('/<int:id>', methods=['PUT'])
def update_hotspot(id):
    hotspot = TitikHotspot.query.get(id)
    if not hotspot:
        return jsonify({"error": "Data hotspot tidak ditemukan"}), 404

    data = request.get_json() or {}
    hotspot.status_api = data.get('status_api', hotspot.status_api)
    hotspot.suhu_permukaan = data.get('suhu_permukaan', hotspot.suhu_permukaan)

    db.session.commit()
    return jsonify({
        "message": "Data hotspot berhasil diperbarui",
        "data": hotspot.to_dict()
    }), 200

# DELETE: Hapus Data Hotspot
@hotspot_bp.route('/<int:id>', methods=['DELETE'])
def delete_hotspot(id):
    hotspot = TitikHotspot.query.get(id)
    if not hotspot:
        return jsonify({"error": "Data hotspot tidak ditemukan"}), 404

    db.session.delete(hotspot)
    db.session.commit()
    return jsonify({"message":  "Data hotspot berhasil dihapus"}), 200