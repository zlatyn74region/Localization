import os

from models import *
from typing import Tuple

def print_functionality(funs: Tuple[str]):
    local.print_translated(('Функциональность', ': ') + funs)

def input_int(
    msg: str, 
    min: int = None, 
    max: int = None,
) -> int:
    while True:
        try:
            num = int(input(msg))
            if min != None and num < min or max != None and num > max:
                min_msg = '' if min == None else f' от {min}'
                max_msg = '' if max == None else f' до {max}'
                print(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                continue
            return num
        except:
            print('Ошибка: нужно ввести число!')

if __name__ == "__main__":
    os.system('cls')
    print('Выберите перевод для программы:\n' + \
        '1 - ru (русский)\n' + \
        '2 - en (английский)\n' + \
        '3 - sp (испанский)')
    choose = input_int('>>> ')
    os.system('cls')
    
    local = Localization(Languages(choose))
    local.print_translated(('Робот после создания', ))
    print('---------------------')
    robot = RobotV()
    local.print_translated(robot.get_parameters())
    print()

    local.print_translated(('Робот после первичного обучения', ))
    print('---------------------')
    robot = RobotVita(robot=robot)
    local.print_translated(robot.get_parameters())
    print_functionality((
        '\n1) ', robot.build_home(),
        '\n2) ', robot.build_barn(),
    ))
    print()

    local.print_translated(('Робот после практики', ))
    print('---------------------')
    robot = RobotVitaliy(robot=robot)
    local.print_translated(robot.get_parameters())
    print_functionality((
        '\n1) ', robot.build_home(),
        '\n2) ', robot.build_barn(),
        '\n3) ', robot.add_floor(),
        '\n4) ', robot.remove_floor(),
    ))