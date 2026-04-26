import time
import ctypes
from datetime import datetime
from parser import get_schedule
from binds import checkerD


def main():
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000003)
    list_pairs = get_schedule()

    while True:
        current_time = datetime.now().strftime("%H:%M")
        time.sleep(10)

        if current_time == "08:05":
            checkerD(list_pairs, 1)
            time.sleep(60)
        if current_time == "09:35":
            checkerD(list_pairs, 2)
            time.sleep(60)
        if current_time == "11:15":
            checkerD(list_pairs, 3)
            time.sleep(60)
        if current_time == "12:40":
            checkerD(list_pairs, 4)
            time.sleep(60)
        if current_time == "14:10":
            checkerD(list_pairs, 5)
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
            break


if __name__ == "__main__":
    main()