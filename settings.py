from helpers import *
import os

MODE = 'release'  # debug/release рабочий/отладочный материал

FPS = 60
MOVE_DOWN = 4
PLATFORM = (500, 500)
NUM_SNOWS = 350
PROJECT_PATH = os.path.dirname(__file__)  # полный путь
BUTTON_IMAGE_PATH = os.path.join(PROJECT_PATH, 'Buttons')
IMAGE_PATH = os.path.join(PROJECT_PATH, 'images')
SCROLL_IMAGE_PATH = os.path.join(PROJECT_PATH, 'scroll')
BACKGROUNG_IMG = '4.jpg'

if __name__ == "__main__":
    print(PROJECT_PATH)