from pyautogui import *
import time

#
# Functions.
#

# Locates gui element.
def locate_click(imgname, alt=None, t=0.1, button="left"):
    # Add pause to allow time for gui elements to appear.
    time.sleep(t)

    # Try to find image from screengrab.
    box = locateOnScreen(imgname)
    print(imgname, "found at: ", box)

    # It not found, try to find alt image.
    if box is None:
        if alt is not None:
            locate_click(alt, button=button)
        return False

    # Get center of button and click.
    x, y = box.left + box.width/2, box.top + box.height/2
    moveTo(x, y)
    long_click(button=button)
    return True

# Longer click, so FFXIV registers it.
def long_click(t=0.100, button="left"):
    mouseDown(button=button)
    time.sleep(t)
    mouseUp(button=button)

#
# Main logic.
#

count = 1;
while(True):
    # Option to pause every 5 iteratons to stop program
    #if count%5 == 0: time.sleep(5);
    
    # get center left third of of screen 
    start_x, start_y = size()
    start_x /= 3;
    start_y /= 2;

    # move cursor to get focus, and click on sign
    moveTo(start_x, start_y)
    click();
    long_click(button="right")

    # Attempt to find gui buttons. 
    if not locate_click("PurchaseLand.png", t=0.3): 
        press("esc");
        continue
    if not locate_click("FreeCompanyAlt.png", "FreeCompany.png"): 
        press("esc");
        press("esc");
        continue
    if not locate_click("Yes.png"): 
        press("esc");
        press("esc");
        press("esc");
        continue

    count += 1;

