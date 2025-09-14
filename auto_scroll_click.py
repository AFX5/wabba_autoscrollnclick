import pyautogui
import time
import sys

# --- CONFIGURATION ---
# 1. Replace 'target_image.png' with the filename of the image you want to click.
#    Make sure the image file is in the SAME FOLDER as this script.
IMAGE_TO_FIND = 'target_image.png'

# 2. Set the interval (in seconds) between each scroll action.
INTERVAL_SECONDS = 2

# 3. Set the scroll amount (a negative value scrolls down).
SCROLL_AMOUNT = -500

# 4. Set the confidence level for image matching (0.8 means 80% confident).
#    You might need to lower this if your image has slight variations or is on
#    a screen with transparency effects.
CONFIDENCE_LEVEL = 0.8
# --- END OF CONFIGURATION ---


print("--- Auto Scroller and Clicker ---")
print("Starting script. The script will run continuously.")
print("To stop manually, press Ctrl+C in this terminal window.")
print("\nEnsure the target application window is active and in the foreground.")
# A brief countdown to allow you to switch to the correct window
for i in range(3, 0, -1):
    print(f"Starting in {i}...", end='\r')
    time.sleep(1)
print("Script is running...      ")

try:
    # Main loop: continues indefinitely until the script is interrupted.
    while True:
        location = None
        try:
            # Step 1: Look for the image on the screen.
            # We wrap this in a try...except block to handle cases where PyAutoGUI
            # raises an ImageNotFoundException instead of returning None.
            location = pyautogui.locateOnScreen(IMAGE_TO_FIND, confidence=CONFIDENCE_LEVEL)

        except pyautogui.ImageNotFoundException:
            # If the image is not found, the exception is caught, and 'location' remains None.
            # We can simply ignore the exception and proceed to the scrolling step.
            pass

        # Step 2: Check if the image was found and take action.
        if location is not None:
            # If found, print a success message and click it.
            print(f"✅ Image '{IMAGE_TO_FIND}' found. Clicking it.")
            
            center_point = pyautogui.center(location)
            pyautogui.click(center_point)

        else:
            # If not found (either from exception or returning None), scroll down.
            print(f"❌ Image not found. Scrolling down...")
            pyautogui.scroll(SCROLL_AMOUNT)
        
        # Step 3: Wait for the specified interval before the next cycle.
        print(f"Waiting for {INTERVAL_SECONDS} seconds...")
        time.sleep(INTERVAL_SECONDS)

except KeyboardInterrupt:
    # This code runs only when you press Ctrl+C to stop the script.
    print("\n\n🛑 Script stopped manually by user.")

except FileNotFoundError:
    # A specific check in case the image file itself is missing.
    print(f"\n\nERROR: The image file '{IMAGE_TO_FIND}' was not found.")
    print("Please make sure the image is in the same folder as the script and the filename is correct.")
