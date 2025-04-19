from pydantic import BaseModel
from typing import List

#https://ru.wikipedia.org/wiki/TLE
#strip

class Satelite(BaseModel):
    name: str

    cutalog_num: str # Номер спутника в базе данных NORAD
    classfic: str # Классификация (U=Unclassified — не секретный)
    international_des_year: int # Международное обозначение (последние две цифры года запуска)
    international_des_num: int # Международное обозначение (номер запуска в этом году)
    international_des_push: str # Международное обозначение (часть запуска)
    epoch_year: int # 	Год эпохи (последние две цифры)
    epoch_day: float # Время эпохи (целая часть — номер дня в году, дробная — часть дня)
    first_meanmotion_a: float # Первая производная от среднего движения (ускорение), делённая на два [виток/день^2]
    second_meanmotion_a: str # Вторая производная от среднего движения, делённая на шесть
    drag_term_b: str # Коэффициент торможения B*
    nul: int # Изначально — типы эфемерид, сейчас — всегда число 0
    el_set_num: int # Номер (версия) элемента

    inclin_digrees: float # Наклонение в градусах
    ascension: float # Долгота восходящего узла в градусах
    eccentricity: float # Эксцентриситет (подразумевается, что число начинается с десятичного разделителя)
    perigee_arg: float # Аргумент перицентра в градусах
    meananomaly: float # Средняя аномалия в градусах
    meanmotion: float # Частота обращения (оборотов в день) (среднее движение) [виток/день]
    revolution_num: int # Номер витка на момент эпохи

    checksum: int # Контрольная сумма по модулю 10



class TLE_encoder:
    @staticmethod
    def decode_tle(tle: List[str]) -> Satelite:
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

        return Satelite(name=name, 
                        cutalog_num=cutalog_num1, classfic=classfic, international_des_year=international_des_year,
                        international_des_num=international_des_num, international_des_push=international_des_push, epoch_year=epoch_year, epoch_day=epoch_day, 
                        first_meanmotion_a=first_meanmotion_a, second_meanmotion_a=second_meanmotion_a, drag_term_b=drag_term_b, nul=nul, el_set_num=el_set_num,
                        inclin_digrees=inclin_digrees, ascension=ascension, eccentricity=eccentricity, 
                        perigee_arg=perigee_arg, meananomaly=meananomaly, meanmotion=meanmotion, revolution_num=revolution_num, checksum=checksum2)

    
    @staticmethod
    def open_TLEfile(path: str) -> List[Satelite]:
        tles = []
        with open(path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):
                tle = lines[i : i +3]
                tles.append(TLE_encoder.decode_tle(tle))
        return tles

if __name__ == "__main__":
    TLE_encoder.open_TLEfile("TLE/TLE_msu.txt")