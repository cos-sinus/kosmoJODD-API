from skyfield.api import load, EarthSatellite, Time
from models import SatelliteSchema
import numpy as np


class GeometryEngine:
    def check_visibility(self, target_schema: SatelliteSchema, observer_schema: SatelliteSchema, d:int=50) -> Time | None:
        ts = load.timescale()
        count = 0
        target_tle = target_schema.full_TLE.splitlines()
        observer_tle = observer_schema.full_TLE.splitlines()
        target = EarthSatellite(*target_tle, name=target_schema.name, ts =ts)
        observer = EarthSatellite(*observer_tle, name=observer_schema.name, ts=ts)
    
        # Временной диапазон (ближайшие 24 часа)
        t_start = ts.now()
        t_end = t_start + 2  # 1 день
        times = ts.linspace(t_start, t_end, 1440)  # Шаг 1 минута

        # Проверка условий
        for time in times:
            # Позиции в ECI
            target_pos = target.at(time).position.km
            observer_pos = observer.at(time).position.km

            # Вектор от наблюдателя к цели
            relative_pos = target_pos - observer_pos
            distance = np.linalg.norm(relative_pos)
            # Угол между вектором и надиром (упрощённо)
            if distance < d:  # Пример: макс. расстояние 100 км
                return time
        return None