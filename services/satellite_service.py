from repositories import SatelliteRepository
from core.tle_encoder import TLE_encoder

class SatelliteService:
    def __init__(self, satellite_repo: SatelliteRepository):
        self.satellite_repo = satellite_repo

    def fill_satellites(self, file_path: str = "TLE/TLE_msu.txt"):
        satellites = TLE_encoder.open_TLEfile(file_path)
        for satellite in satellites:
            self.satellite_repo.create(satellite)

    def get_all(self):
        return self.satellite_repo.get_all()