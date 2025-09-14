# Auto Scroller \& Clicker

A simple yet powerful Python script that automates the process of scrolling through an application window to find and click a specific image.

> **To use with Wabbajack:**
> Run Wabbajack and begin downloading your modlist. Once a new window opens and redirects you to the Nexus page, take a screenshot of the "SLOW DOWNLOAD" button. Save this image as `target_image.png` and follow the instructions below.

***

## What It Does

The script repeatedly performs the following actions in a loop:

1. **Searches**: Scans the entire screen to find a specified target image (`target_image.png`).
2. **Clicks**: If the image is found, moves the mouse cursor to the center of the image and clicks it.
3. **Scrolls**: If the image is not found, scrolls the active window down.
4. **Waits**: Waits for a configurable interval before repeating the process.

This loop continues indefinitely until manually stopped.

***

## Features

- **Continuous Operation**: Runs in an infinite loop until stopped.
- **Image Recognition**: Utilizes PyAutoGUI's image recognition to locate elements on the screen.
- **Configurable**: Easily adjust the target image, time interval, scroll distance, and match confidence.
- **Robust Error Handling**: Gracefully handles cases where the image isn't on screen.
- **User-Friendly Feedback**: Prints its current action (clicking, scrolling, waiting) to the console.

***

## Prerequisites

Make sure you have Python installed. Then install the necessary libraries:

```bash
pip install pyautogui opencv-python
```

> _Note_: `opencv-python` is required for image recognition features.

***

## How to Use

1. **Capture the Target Image**
Take a clear screenshot of the button, icon, or element you want to click. Save this as a `.png` file (e.g., `target_image.png`).
2. **File Placement**
Place the image in the **same folder** as `auto_scroller_clicker.py`.
3. **Configure the Script**
Edit `auto_scroller_clicker.py` and adjust the following variables in the **CONFIGURATION** section:
    - `IMAGE_TO_FIND`: Filename of your target image.
    - `INTERVAL_SECONDS`: Time to wait between actions.
    - `SCROLL_AMOUNT`: Pixels to scroll (negative value for scrolling down).
    - `CONFIDENCE_LEVEL`: Accuracy for image matching (between 0.0 and 1.0).
4. **Run the Script**
    - Open the application to automate and ensure its window is active.
    - Open your terminal or command prompt.
    - Navigate to the script and image directory.
    - Run:

```bash
python auto_scroll_click.py
```

    - You have a 3-second countdown to focus your target application window.
5. **Stop the Script**
Switch back to the terminal and press **Ctrl + C**.

***

## ⚠️ Important Warnings

- **Mouse \& Keyboard Control**: This script takes control of your mouse and keyboard. Do not leave it running unattended.
- **Fail-Safe**: PyAutoGUI has a built-in safety feature. If the script misbehaves, **move your mouse cursor to any screen corner** to stop immediately.
- **Permissions**: On some systems (esp. macOS), you may need to grant accessibility permissions for mouse/screen control.

***

## License

This project is licensed under the MIT License. See the LICENSE file for details.
