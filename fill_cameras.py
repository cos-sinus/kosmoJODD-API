from repositories import SatelliteRepository
from models import get_db, Base, engine


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    with get_db() as db:
        satellite_repository = SatelliteRepository(db)
        with open("cameras.txt") as file:
            for line in file:
                try:
                    satellite_repository.add_camera(line.strip())
                except Exception as e:
                    print(f"Error adding camera: {e}")