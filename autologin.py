import pyautogui
import time

def launch_and_input(login, password, game_path):
    # Запускаем игру
    pyautogui.hotkey('win', 'r')
    pyautogui.write(game_path)
    pyautogui.press('enter')

    # Даем игре время на запуск
    time.sleep(10)

    # Вводим логин
    pyautogui.write(login)

    # Переходим к полю пароля
    pyautogui.press('tab')

    # Вводим пароль
    pyautogui.write(password)

    # Можно дополнительно нажать "Enter" после ввода пароля
    # pyautogui.press('enter')

# Пример использования
login = "your_login"
password = "your_password"
game_path = "F:\\L2\\System\\L2.exe"
launch_and_input(login, password, game_path)