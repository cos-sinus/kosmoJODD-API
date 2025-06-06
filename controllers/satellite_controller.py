from services import SatelliteService
from flask import request, jsonify


class SatelliteController:
    def __init__(self, satellite_service: SatelliteService):
        self.satellite_service = satellite_service

    def get_all(self):
        sattelites = self.satellite_service.get_all()
        return jsonify([satellite.model_dump() for satellite in sattelites]), 200

    def near_satellites(self, satellite_id: int):
        sattelites = self.satellite_service.near_satellites(satellite_id)
        return jsonify([satellite.model_dump() for satellite in sattelites]), 200