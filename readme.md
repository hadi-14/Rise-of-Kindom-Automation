**Project Overview**

The project involves automating a series of tasks related to image recognition and mouse interactions on a computer. This automation script is designed to work with a specific application or game, as indicated by the use of image recognition to locate and click on certain elements on the screen. The script uses several Python libraries, including PyAutoGUI, Mouse, Keyboard, Firebase, and Pillow, to achieve its automation goals.

**What We Did for This Project**

1. **Imports**: The project starts with the necessary library imports, which include PyAutoGUI for simulating mouse and keyboard inputs, Mouse for mouse-related interactions, Keyboard for registering hotkeys, Firebase Admin for connecting to a database, and Pillow for image processing.
2. **Image Resizing**: The script includes a function called `resize_image()` that resizes images to match the screen resolution. This is necessary because the script uses image recognition to locate specific elements on the screen.
3. **Firebase Database Check**: The script connects to a Firebase database using credentials from a JSON file. It queries the database to check for a specific key entered by the user and retrieves associated data if the key exists. The Firebase database is used for some form of authentication or configuration.
4. **Automate Function**: The `automate()` function is the core of the automation process. It performs the following tasks:

   - Simulates a left-click using the Mouse library to initiate an action.
   - Obtains the screen's width and height using PyAutoGUI for image resizing purposes.
   - Resizes a set of images to match the screen resolution. These images are later used for image recognition.
   - Locates a specific image (`s1.png`) on the screen with a confidence threshold of 80%. If the image is found, it moves the mouse cursor to its center and simulates a left-click. This process repeats for a set of images (`s2.png` to `s5.png`).
   - Each image recognition and interaction step is followed by a one-second delay to control the pacing of the automation.
5. **Hotkey Registration**: The script registers a hotkey (`ctrl + shift + z`) to trigger the `automate()` function. This allows the user to initiate the automation by pressing the designated hotkey.
6. **User Interaction**: The script requests the user to input an app key, which is checked in the Firebase database. If a valid key is found, the script registers the hotkey for automation.
7. **Project Results**: The project is designed for automating specific interactions with an application or game. It relies on image recognition to locate elements on the screen and simulate mouse clicks. The use of Firebase for key validation suggests that this script could be part of a larger system where specific actions or configurations are authorized based on keys stored in a database.

**Problem Encountered:**
In the process of automating actions within the game Rise of Kingdoms, we encountered a significant challenge related to the detection of buttons and user interface elements. This challenge arose due to the presence of many similar pixels on the screen and variations in screen sizes.

**Related Projects**

The project can be related to other automation and computer vision projects, particularly those involving:

1. **Game Automation**: Similar automation techniques can be used for automating repetitive tasks in games, such as bot actions or script-based gameplay.
2. **Robotic Process Automation (RPA)**: This project shares similarities with RPA, where software robots automate tasks in business processes. The use of image recognition for interaction can be relevant in RPA.
3. **Computer Vision Applications**: Projects that rely on computer vision for tasks like object detection, facial recognition, or image analysis are related due to the use of image recognition in this project.
4. **Database-Driven Automation**: Automation systems that rely on database checks, such as user authentication or configuration settings, can be considered related.

These related projects often involve a combination of Python libraries for automation, image processing, and database interactions to achieve specific goals.
