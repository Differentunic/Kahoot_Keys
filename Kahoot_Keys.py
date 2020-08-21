import pyautogui
import keyboard
import PySimpleGUI as sg
from multiprocessing import Process
import time
import sys
sg.theme('DarkAmber')  # Add a touch of colour

# noinspection PyTypeChecker
SysTray = sg.SystemTray(menu=None,
                        filename=None,
                        data=None,
                        data_base64=None,
                        tooltip=None,
                        metadata=None)


def notification():
    sg.SystemTray.ShowMessage(SysTray, 'Kahoot Keys Is Running', 'Press (Esc) To Stop',
                              filename=None,
                              data=None,
                              data_base64=None,
                              messageicon=None,
                              time=(300, 5000))


def key_check():
    while True:

        if keyboard.is_pressed('j'):
            pyautogui.moveTo(480, 270)
            pyautogui.leftClick()

        if keyboard.is_pressed('k'):
            pyautogui.moveTo(480 * 3, 270)
            pyautogui.leftClick()

        if keyboard.is_pressed('n'):
            pyautogui.moveTo(480, 270 * 3)
            pyautogui.leftClick()

        if keyboard.is_pressed('m'):
            pyautogui.moveTo(480 * 3, 270 * 3)
            pyautogui.leftClick()

        if keyboard.is_pressed('esc'):
            sg.SystemTray.ShowMessage(SysTray, 'Kahoot Keys Has Stopped', '',
                                      filename=None,
                                      data=None,
                                      data_base64=None,
                                      messageicon=None,
                                      time=(1000, 5000))
            break

notification()
key_check()
