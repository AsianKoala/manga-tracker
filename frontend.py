from art import text2art
from tqdm import trange
from time import sleep
from colorama import Fore, Back
from colorama import init as colorama_init
from color import Color

def someRoutine():
    sleep(0.1)


def main():
    # start progress bar and attach routine:
    for i in trange(20):
        someRoutine()
    print("Ding, Ding chicken is done !")


# Run things
# main()
# Art = text2art("SOUP !", font='big')
# print(Art)
banner = text2art("MANGA        TRACKER")
Color.printer("BANNER", banner)
