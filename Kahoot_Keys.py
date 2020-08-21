from os import path
from pyautogui import leftClick
from keyboard import is_pressed
from plyer import notification


def notification_on_start():
    if path.isfile("Kahoot_Keys.ico"):
        notification.notify(
            title='Kahoot Keys',
            message="Kahoot Keys is running. \n Press (Esc) to quit",
            app_name="Kahoot Keys",
            app_icon="Kahoot_Keys.ico"
        )
        key_check()

    else:
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
            if path.isfile("Kahoot_Keys.ico"):
                notification.notify(
                    title='Kahoot Keys',
                    message="Kahoot Keys is running. \n Press (Esc) to quit",
                    app_name="Kahoot Keys",
                    app_icon="Kahoot_Keys.ico"
                )
                exit()
            else:
                exit()


notification_on_start()
