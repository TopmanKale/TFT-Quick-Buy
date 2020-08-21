import pyautogui
from pynput import keyboard


def on_press(key):
    print(key)


def on_release(key):
    if key == keyboard.Key.num_lock:
        return False
    if key == keyboard.KeyCode(char='1'):
        pyautogui.click(580, 1000)
        pyautogui.dragTo(580, 1000)
    if key == keyboard.KeyCode(char='2'):
        pyautogui.click(780, 1000)
        pyautogui.dragTo(780, 1000)
    if key == keyboard.KeyCode(char='3'):
        pyautogui.click(980, 1000)
        pyautogui.dragTo(980, 1000)
    if key == keyboard.KeyCode(char='4'):
        pyautogui.click(1180, 1000)
        pyautogui.dragTo(1180, 1000)
    if key == keyboard.KeyCode(char='5'):
        pyautogui.click(1380, 1000)
        pyautogui.dragTo(1380, 1000)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(on_press=on_press, on_release=on_release)

listener.start()
