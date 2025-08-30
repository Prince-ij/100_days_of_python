import pyautogui
import time

time.sleep(3)  # Time to switch to the game

# Dino game automation
while True:
    # Check pixels ahead of Dino
    x1 = pyautogui.pixel(655, 385)
    x2 = pyautogui.pixel(659, 375)
    x3 = pyautogui.pixel(663, 369)


    # If any pixel is dark (obstacle), press space
    if (x1[1] < 230) or (x2[1] < 230) or (x3[0] < 230):
        pyautogui.press('space')
