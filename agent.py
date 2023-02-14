import eel
import pyautogui

@eel.expose
def mouseMove(tempX, tempY):
    screenWidth, screenHeight = pyautogui.size()
    x = tempX / 100 * screenWidth
    y = tempY / 100 * screenHeight
    pyautogui.moveTo(round(x), round(y))

eel.init('web')
eel.start('index.html')