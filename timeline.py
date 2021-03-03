import time
from checker import check_seibro
from datetime import datetime

def timeline():

    while True:
        result = check_seibro()
        if result:
            return print('끝')


        time.sleep(600)


if __name__ == '__main__':
    timeline()