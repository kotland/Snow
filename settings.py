import os

FPS = 60
MOVE_DOWN = 4
PLATFORM = (500, 500)
NUM_SNOWS = 30
NORMAL = 0
MOVE_IN_SIDE = "wind"
PROJECT_PATH = os.path.dirname(__file__)  # полный путь
BUTTON_IMAGE_PATH = os.path.join(PROJECT_PATH, 'Buttons')
SNOW_IMAGE_PATH = os.path.join(PROJECT_PATH, 'examples')
SCROLL_IMAGE_PATH = os.path.join(PROJECT_PATH, 'scroll')

if __name__ == "__main__":
    print(PROJECT_PATH)