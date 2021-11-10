import os
from questioner import Questioner

questioner = Questioner("questions")

if __name__ == "__main__":
    while True:
        questioner.start()

        if input("\n엔터를 누르면 다시 시작합니다") == "":
            os.system("cls")
            continue