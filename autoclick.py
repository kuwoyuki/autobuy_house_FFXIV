from pyautogui import *
import time

#
# Functions.
#

def do_click(box, button):
    time.sleep(0.2)
    x, y = box.left + box.width / 2, box.top + box.height / 2
    moveTo(x, y)
    long_click(button=button)


# Locates gui element.
def locate_click(imgname, alt=None, t=0.1, button="left"):
    # Add pause to allow time for gui elements to appear.
    time.sleep(t)

    # Try to find image from screengrab.
    box = locateOnScreen(imgname)
    print(imgname, "found at:\n\t", box)

    # It not found, try to find alt image.
    if box is None:
        if alt is not None:
            box = locate_click(alt, button=button)
        return False, None

    # Get center of button and click.
    do_click(box, button)
    return True, box


# Longer click, so FFXIV registers it.
def long_click(t=0.100, button="left"):
    mouseDown(button=button)
    time.sleep(t)
    mouseUp(button=button)


#
# Main logic.
#

# Define image paths:
img_dir = "img/"
img_purchaseland = img_dir + "PurchaseLand.png"
img_purchaseland_alt = None
img_freecompany = img_dir + "FreeCompany.png"
img_freecompany_alt = img_dir + "FreeCompanyAlt.png"
img_yes = img_dir + "Yes.png"
img_yes_alt = None
count = 1

# save pos
saved_purchase = None
saved_yes = None

while True:
    # Option to pause every 5 iteratons to stop program
    # if count%5 == 0: time.sleep(5);

    # get center left third of of screen
    start_x, start_y = size()
    start_x /= 3
    start_y /= 2

    # move cursor to get focus, and click on sign
    moveTo(start_x, start_y)
    click()
    long_click(button="right")

    # Attempt to find gui buttons.
    if saved_purchase is not None:
        print("using saved purchase pos\n\t", saved_purchase)
        do_click(saved_purchase, "left")
    else:
        success, box = locate_click(img_purchaseland, img_purchaseland_alt, t=0.4)
        if not success:
            press("esc")
            continue
        saved_purchase = box
    # if not locate_click(img_freecompany_alt, img_freecompany):
    #     press("esc");
    #     press("esc");
    #     continue
    if saved_yes is not None:
        print("using saved yes pos\n\t", saved_yes)
        do_click(saved_yes, "left")
    else:
        sucess, box = locate_click(img_yes, img_yes_alt)
        if not success:
            press("esc")
            press("esc")
            continue
        saved_yes = box

    count += 1
