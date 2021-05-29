
from datetime import datetime
import os
import time
from win10toast import ToastNotifier


def popup():
    toaster = ToastNotifier()
    toaster.show_toast(
        "Good Morning Sir , Its time for your online class ! Opening Teams Now ....."
        , duration=10)


def reminder():
    popup()
    t_path = "C:\\Users\\dell\\AppData\\Local\\Microsoft\\Teams\\current\\teams.exe"
    os.startfile(t_path)


if __name__ == "__main__":
    while True:
        obj_now = datetime.now()
        if(obj_now.hour == 10 and obj_now.minute == 5):
            reminder()
            time.sleep(60)
