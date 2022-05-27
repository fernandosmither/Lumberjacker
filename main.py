import time
import utils
from os.path import exists
from const import WOOD_COLOR


def main():
    """" First we need to calibrate the coordinates,
    if the config file doesn't exist yet."""

    if not exists('config.txt'):
        utils.calibrate()

    with open('config.txt', 'r') as file:
        config = file.readlines()
        LEFT_POS = tuple(int(x) for x in
                    config[0].split('=')[1].strip().split(','))
        RIGHT_POS = tuple(int(x) for x in
                     config[1].split('=')[1].strip().split(','))

    while True:
        left_color = utils.get_pixel_colour(*LEFT_POS)
        right_color = utils.get_pixel_colour(*RIGHT_POS)
        if left_color == WOOD_COLOR:
            utils.move('Right')
            time.sleep(0.005)
            utils.move('Right')
        elif right_color == WOOD_COLOR:
            utils.move('Left')
            time.sleep(0.005)
            utils.move('Left')
        else:
            utils.move('Left')
        time.sleep(0.1)


if __name__ == '__main__':
    main()
