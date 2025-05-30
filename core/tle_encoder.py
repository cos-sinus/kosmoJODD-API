from pydantic import BaseModel
from typing import List
from models import SatelliteSchema

class TLE_encoder:
    @staticmethod
    def decode_tle(tle: List[str]) -> SatelliteSchema:
        line1 = tle[1].strip()
        line2 = tle[2].strip()

        name = tle[0].strip()

        cutalog_num1 = line1[2:7]
        classfic = line1[7]
        international_des_year = int(line1[9:11])
        international_des_num = int(line1[11:14])
        international_des_push = line1[14:17]
        epoch_year = int(line1[18:20])
        epoch_day = float(line1[20:32])
        first_meanmotion_a = float(line1[33:43])
        second_meanmotion_a = line1[44:52]
        drag_term_b = line1[53:61]
        nul = int(line1[62])
        el_set_num = int(line1[64:68])

        inclin_digrees = float(line2[8:16])
        ascension = float(line2[17:25])
        eccentricity = float(line2[26:33])
        perigee_arg = float(line2[34:42])
        meananomaly = float(line2[43:51])
        meanmotion = float(line2[52:63])
        revolution_num = int(line2[63:68])
        checksum2 = int(line2[68])

        return SatelliteSchema(name=name, 
                        full_TLE=f'{tle[1].strip()}\n{tle[2].strip()}',
                        cutalog_num=cutalog_num1, classfic=classfic, international_des_year=international_des_year,
                        international_des_num=international_des_num, international_des_push=international_des_push, epoch_year=epoch_year, epoch_day=epoch_day, 
                        first_meanmotion_a=first_meanmotion_a, second_meanmotion_a=second_meanmotion_a, drag_term_b=drag_term_b, nul=nul, el_set_num=el_set_num,
                        inclin_digrees=inclin_digrees, ascension=ascension, eccentricity=eccentricity, 
                        perigee_arg=perigee_arg, meananomaly=meananomaly, meanmotion=meanmotion, revolution_num=revolution_num, checksum=checksum2)

    
    @staticmethod
    def open_TLEfile(path: str) -> List[SatelliteSchema]:
        tles = []
        with open(path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                tle = lines[i : i +3]
                tles.append(TLE_encoder.decode_tle(tle))
        return tles

if __name__ == "__main__":
    TLE_encoder.open_TLEfile("TLE/TLE_msu.txt")