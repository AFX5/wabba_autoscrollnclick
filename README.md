Auto Scroller & Clicker
A simple yet powerful Python script that automates the process of scrolling through an application window to find and click a specific image. 
(To use in wabbajack: Run Wabbajack and begin downloading your modlist. Once a new window opens, redirecting you onto Nexus page, take a screenshot of the SLOW DONWLOAD button.)
The script runs in a continuous loop, making it ideal for repetitive tasks, automated testing, or interacting with applications that load content dynamically.

What it Does?
The script repeatedly performs the following actions in a loop:
Searches: It scans the entire screen to find a specified target image (target_image.png).
Clicks: If the image is found, it moves the mouse cursor to the center of the image and clicks it.
Scrolls: If the image is not found, it scrolls the active window down.
Waits: After either action, it waits for a configurable interval before repeating the process.
This loop continues indefinitely until the user manually stops the script.

Features
Continuous Operation: Runs in an infinite loop until stopped.
Image Recognition: Uses pyautogui's image recognition to locate elements on the screen.
Configurable: Easily adjust the target image, time interval, scroll distance, and match confidence.
Robust Error Handling: Gracefully handles cases where the image isn't on screen without crashing.
User-Friendly Feedback: Prints its current action (clicking, scrolling, waiting) to the console.

Prerequisites
Before running the script, you need to have Python installed on your system. 
Then, install the necessary libraries using pip:
pip install pyautogui opencv-python

Note: opencv-python is a required dependency for the image recognition features of pyautogui.

How to Use
Capture the Target Image: Take a clear screenshot of the button, icon, or element you want the script to click. Save this image as a .png file (e.g., target_image.png).
File Placement: Place the saved image file in the exact same folder as the auto_scroller_clicker.py script.
Configure the Script: Open auto_scroller_clicker.py in a text editor and modify the variables in the CONFIGURATION section to fit your needs:
IMAGE_TO_FIND: The filename of your target image.
INTERVAL_SECONDS: The time to wait between actions.
SCROLL_AMOUNT: The number of pixels to scroll (use a negative value to scroll down).
CONFIDENCE_LEVEL: The accuracy for image matching (a value between 0.0 and 1.0). You might need to lower this from the default 0.8 if the target image has slight variations.
Run the Script:
Open the application you want to automate and make sure its window is active.
Open a terminal or command prompt.
Navigate to the directory where you saved the script and image.
Execute the script using the command:
python auto_scroll_click.py

You will have a 3-second countdown to switch focus to your target application window.
Stop the Script: To stop the automation, switch back to the terminal window and press Ctrl + C.

⚠️ Important Warnings
This script takes control of your mouse and keyboard. Do not leave it running unattended.
Fail-Safe: pyautogui has a built-in safety feature. If the script is behaving unexpectedly, you can forcefully move your mouse cursor to any of the four corners of the screen to immediately stop the script with an exception.
Permissions: On certain operating systems (especially macOS), you may need to grant accessibility permissions to your terminal or code editor for the script to be able to control the mouse and see the screen.

License: This project is licensed under the MIT License. See the LICENSE file for details.
