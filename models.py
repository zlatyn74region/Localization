from abc import ABC
from enum import Enum
from typing import Tuple

class Robot(ABC):
    inv_num: str = "АА001221-56"
    name: str
    place: str

    def get_parameters(self) -> Tuple[str]:
        return ('Инвентарный номер', ': ', self.inv_num, '\n', 
                'Наименование', ': ', self.name, '\n',
                'Местонахождение', ': ', self.place)

class RobotV(Robot):
    def __init__(self):
        self.name = "В"
        self.place = "Робозавод"

class Decorator(Robot, ABC):
    robot: Robot

    def __init__(self, robot: Robot):
        self.robot = robot

    def build_home(self) -> str:
        return self.robot.build_home()

    def build_barn(self) -> str:
        return self.robot.build_barn()

    def add_floor(self) -> str:
        return self.robot.add_floor()

    def remove_floor(self) -> str:
        return self.robot.remove_floor()

class RobotVita(Decorator):
    def __init__(self, robot: Robot):
        super().__init__(robot=robot)
        self.name = 'Вита' 
        self.place = 'Первичное обучение'   

    def build_home(self) -> str:
        return 'Постройка домов'

    def build_barn(self) -> str:
        return 'Постройка сараев'

class RobotVitaliy(Decorator):
    def __init__(self, robot: Robot):
        super().__init__(robot=robot)
        self.name = 'Виталий' 
        self.place = 'Предприятие "ООО Кошмарик"'

    def add_floor(self) -> str:
        return 'Добавление этажей к постройкам'

    def remove_floor(self) -> str:
        return 'Снос верних этажей у построек'

class Languages(Enum):
    ru = 1
    en = 2
    sp = 3

class Localization():
    lang: Languages

    all_langs = [
    {
        'lang': Languages.ru,
        'В': 'В',
        'Вита': 'Вита',
        'Виталий': 'Виталий',
        'Инвентарный номер': 'Инвентарный номер',
        'Наименование': 'Наименование',
        'Местонахождение': 'Местонахождение',
        'Робозавод': 'Робозавод',
        'Первичное обучение': 'Первичное обучение',
        'Предприятие "ООО Кошмарик"': 'Предприятие "ООО Кошмарик"',
        'Постройка домов': 'Постройка домов',
        'Постройка сараев': 'Постройка сараев',
        'Добавление этажей к постройкам': 'Добавление этажей к постройкам',
        'Снос верних этажей у построек': 'Снос верних этажей у построек',
        'Функциональность': 'Функциональность',
        'Робот после создания': 'Робот после создания',
        'Робот после первичного обучения': 'Робот после первичного обучения',
        'Робот после практики': 'Робот после практики',
    },
    {
        'lang': Languages.en,
        'В': 'V',
        'Вита': 'Vita',
        'Виталий': 'Vitaliy',
        'Инвентарный номер': 'Inventory number',
        'Наименование': 'Name',
        'Местонахождение': 'Place',
        'Робозавод': 'Robo-factory',
        'Первичное обучение': 'Primary education',
        'Предприятие "ООО Кошмарик"': 'The company "OOO Koshmarik"',
        'Постройка домов': 'Building houses',
        'Постройка сараев': 'Building barns',
        'Добавление этажей к постройкам': 'Adding floors to buildings',
        'Снос верних этажей у построек': 'Demolition of the upper floors of buildings',
        'Функциональность': 'Functionality',
        'Робот после создания': 'Robot after creation',
        'Робот после первичного обучения': 'Robot after initial training',
        'Робот после практики': 'Robot after practice',
    },
    {
        'lang': Languages.sp,
        'В': 'UVE', 
        'Вита': 'Vita', 
        'Виталий': 'Vitaly', 
        'Инвентарный номер': 'Número de inventario',
        'Наименование': 'Denominación',
        'Местонахождение': 'Paradero',
        'Робозавод': 'Robo-fábrica',
        'Первичное обучение': 'Enseñanza primaria',
        'Предприятие "ООО Кошмарик"': 'Empresa "Pesadilla LLC"',
        'Постройка домов': 'Construcción de casas',
        'Постройка сараев': 'Construcción de cobertizos',
        'Добавление этажей к постройкам': 'Añadir pisos a edificios',
        'Снос верних этажей у построек': 'Demolición de los pisos superiores de los edificios',
        'Функциональность': 'Funcionalidad',
        'Робот после создания': 'Robot después de la creación',
        'Робот после первичного обучения': 'Robot después del entrenamiento primario',
        'Робот после практики': 'Robot después de la práctica',
    }]

    def __init__(self, lang: Languages = Languages):
        self.lang = lang

    def print_translated(self, phrases: Tuple[str]):
        for phrase in phrases:
            for lang in self.all_langs:
                if lang['lang'] == self.lang:
                    if phrase in lang:
                        print(lang[phrase], end='')
                    else:
                        print(phrase, end='')
        print()