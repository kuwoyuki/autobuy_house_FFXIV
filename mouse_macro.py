from pyautogui import *
import time

def locateClick(imgname, alt=None, t=0.1, button="left"):
    time.sleep(t)
    box = locateOnScreen(imgname)
    print(imgname, "found at: ", box)

    if box is None:
        if alt is not None:
            locateClick(alt, button=button)
        return False

    x, y = box.left + box.width/2, box.top + box.height/2
    moveTo(x, y)
    longClick(button=button)
    return True

def longClick(t=0.100, button="left"):
    mouseDown(button=button)
    time.sleep(t)
    mouseUp(button=button)

count = 1;
while(True):
    #if count%5 == 0: time.sleep(5);
    
    # get center of screen
    start_x, start_y = size()
    start_x /= 3;
    start_y /= 2;

    moveTo(start_x, start_y)
    click();
    longClick(button="right")

    if not locateClick("PurchaseLand.png", t=0.3): 
        press("esc");
        continue
    if not locateClick("FreeCompanyAlt.png", "FreeCompany.png"): pass
    if not locateClick("Yes.png"): pass
    count += 1;


