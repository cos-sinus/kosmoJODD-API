from repositories import SatelliteRepository
from core.tle_encoder import TLE_encoder
from core import GeometryEngine
from models import SatelliteCrossSchema
from typing import List


class SatelliteService:
    def __init__(
            self, 
            satellite_repo: SatelliteRepository,
            geometry_engine: GeometryEngine
        ):
        self.satellite_repo = satellite_repo
        self.geometry_engine = geometry_engine

    def fill_satellites(self, file_path: str = "TLE_msu.txt"):
        satellites = TLE_encoder.open_TLEfile(file_path)
        for satellite in satellites:
            self.satellite_repo.create(satellite)

    def get_all(self):
        return self.satellite_repo.get_all()
    
    def near_satellites(self, satellite_id: int) -> List[SatelliteCrossSchema]:
        target_satellite = self.satellite_repo.get_by_id(satellite_id)
        result = []
        for satellite in self.get_all():
            if satellite.camera: # Если у спутника есть камера, то ищем только у него
                visible = self.geometry_engine.check_visibility(target_satellite, satellite)
                if satellite.id != target_satellite.id and visible is not None:
                    print("Найден близкий спутник", satellite.name)
                    result.append(SatelliteCrossSchema(
                        id=satellite.id, 
                        target_id=target_satellite.id, 
                        name=satellite.name, 
                        time_visible=visible.utc_datetime()
                    ))
        return result
