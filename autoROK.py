import pyautogui
import time
import mouse
import keyboard
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from PIL import Image
import os

def resize_image(image_path, target_width, target_height):
    image = Image.open(image_path)
    original_width, original_height = image.size
    scaled_width = int(target_width * original_width / 1920)  # Scale width based on 1920x1080 reference resolution
    scaled_height = int(target_height * original_height / 1080)  # Scale height based on 1080p reference resolution
    scaled_image = image.resize((scaled_width, scaled_height))
    os.makedirs("images", exist_ok=True)
    scaled_image.save(f"images/{image_path.split('/')[-1]}")

def check_key(key):
    cred = credentials.Certificate("credidentials.json")
    try:firebase_admin.initialize_app(cred)
    except:pass
    db = firestore.client()

    collection_ref = db.collection(u'allusers')
    docs = collection_ref.stream()

    for doc in docs:
        for data in doc.to_dict()["allusers"]:
            if data["key"] == key:
                return data
    
    return None

def automate():
    mouse.click('left')
    time.sleep(1)

    screen_width, screen_height = pyautogui.size()

    # Resizing the images to match the screen resolution
    resize_image('original_image/s1.png', screen_width, screen_height)
    resize_image('original_image/s2.png', screen_width, screen_height)
    resize_image('original_image/s3.png', screen_width, screen_height)
    resize_image('original_image/s4.png', screen_width, screen_height)
    resize_image('original_image/s5.png', screen_width, screen_height)

    l1 = pyautogui.locateOnScreen('images/s1.png', confidence=0.8)
    if str(l1) == "None":
        print("l1 None")
        return
    else:
        mouse.move(l1.left + l1.width / 2, l1.top + l1.height / 2, absolute=True, duration=0.1)
        mouse.click('left')
        time.sleep(1)
    time.sleep(1)
    l2 = pyautogui.locateOnScreen('images/s2.png', confidence=0.8)
    if str(l2) == "None":
        print("l2 None")
        return
    else:
        mouse.move(l2.left + l2.width / 2, l2.top + l2.height / 2, absolute=True, duration=0.1)
        mouse.click('left')
        time.sleep(1)
    time.sleep(1)
    l3 = pyautogui.locateOnScreen('images/s3.png', confidence=0.8)
    if str(l3) == "None":
        print("l3 None")
        return
    else:
        mouse.move(l3.left + l3.width / 2, l3.top + l3.height / 2, absolute=True, duration=0.1)
        mouse.click('left')
        time.sleep(1)
    time.sleep(1)
    l4 = pyautogui.locateOnScreen('images/s4.png', confidence=0.8)
    if str(l4) == "None":
        print("l4 None")
        return
    else:
        mouse.move(l4.left + l4.width /2 , l4.top + l4.height / 2, absolute=True, duration=0.1)
        mouse.click('left')
        time.sleep(1)   
    time.sleep(1)
    l5 = pyautogui.locateOnScreen('images/s5.png', confidence=0.8)
    if str(l5) == "None":
        print("l5 None")
        return
    else:
        mouse.move(l5.left + l5.width /2 , l5.top + l5.height / 2, absolute=True, duration=0.1)
        mouse.click('left')
        time.sleep(1)
    
    time.sleep(1)
    return


# Register all of our keybindings
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # s = input()
    # print(s)

    key = check_key(input("Enter Your app key: "))

    if key is not None:
        print(key)
        keyboard.add_hotkey('ctrl + shift + z', automate)
        keyboard.wait('esc')