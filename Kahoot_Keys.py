from os import path, environ
from pyautogui import leftClick
from keyboard import is_pressed
from plyer import notification
from requests import get

environ['DISPLAY'] = ':0'

url = ("https://raw.githubusercontent.com/Differentunic/Kahoot_Keys/master/Kahoot_Keys.ico")
icon_data = get(url, verify=False)
open('Kahoot_Keys.ico', 'wb').write(icon_data.content)

def start():
    notification.notify(
        title="Kahoot Keys",
        message="Kahoot Keys is running. \n Press (Esc) to quit",
        app_name="Kahoot Keys",
        app_icon="Kahoot_Keys.ico"
    )
    key_check()



def quit():
    notification.notify(
        title="Kahoot Keys",
        message="Kahoot Keys has quit.",
        app_name="Kahoot Keys",
        app_icon="Kahoot_Keys.ico"
    )
    exit()

def key_check():
    while True:

        if is_pressed('j'):
            leftClick(480, 270)

        if is_pressed('k'):
            leftClick(480 * 3, 270)

        if is_pressed('n'):
            leftClick(480, 270 * 3)

        if is_pressed('m'):
            leftClick(480 * 3, 270 * 3)

        if is_pressed('esc'):
            quit()


# notification_on_start()

if __name__ == '__main__':
    start()
