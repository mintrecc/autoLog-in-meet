import time
import pyautogui
import webbrowser

chrome_path = '"C:/Program Files/Google/Chrome/Application/chrome.exe" %s --profile-directory="Profile 4"'


def ahk():
    time.sleep(7)
    pyautogui.hotkey('ctrl', 'd')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(2)
    pyautogui.press('enter')


def checkerD(list_pairs, num):
    subject = list_pairs.get(str(num))

    if not subject:
        time.sleep(1)
        return

    links = {
        'Алгоритми та структура даних[Лк]': 'https://meet.google.com/cvt-mgdc-rzm?authuser=1',
        "Комп'ютерні дискретні структури[Лк]": 'https://meet.google.com/wea-byrr-bvk?authuser=1',
        'Групова динаміка та комунікації[Лк]': 'https://meet.google.com/rcb-oyse-yhs?authuser=1',
        'Програмування[Лк]': 'https://meet.google.com/mob-juzw-deh?authuser=1',
        "Комп'ютерна графіка та обробка зображень[Лк]": 'https://meet.google.com/mob-juzw-deh?authuser=1&pageId=none'
    }

    if subject in links:
        webbrowser.get(chrome_path).open(links[subject], new=2)
        ahk()