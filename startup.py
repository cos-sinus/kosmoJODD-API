from models import Base, get_db, engine
from repositories import RequestRepository, SatelliteRepository
from services import SatelliteService
from core import GeometryEngine

STATUSES = [
    "В процессе",
    "Отклонено",
    "Завершено"
]

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    with get_db() as db:
        repo = RequestRepository(db)
        satellite_repo = SatelliteRepository(db)
        g_e = GeometryEngine()
        satellite_service = SatelliteService(satellite_repo, g_e)

        for status in STATUSES:
            repo.create_status(status)

        satellite_service.fill_satellites()

        with open("cameras.txt") as file:
            for line in file:
                try:
                    satellite_repo.add_camera(line.strip())
                except Exception as e:
                    print(f"Error adding camera: {e}")
