# LogSnap

**LogSnap** is a tool that captures an image using your webcam and sends a notification to your Telegram account on every login to your PC.

## Features

- Captures an image upon user login.
- Sends the captured image to a specified Telegram account with a timestamp.

## Requirements

- Python 3.x
- `pip` (Python package installer)
- `git` (version control system)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/LogSnap.git
   cd LogSnap
Install the required packages:

sh
Copy code
pip install -r requirements.txt
Configure telegram-send:

Follow the setup instructions for telegram-send to configure it with your Telegram account.

Usage
Update the main() function in logsnap.py with the correct image path and camera device index:

python
Copy code
def main():
    image_path = "C:\\Users\\YOUR_USERNAME\\Desktop\\Image.jpg"
    camera_device = 0 # Update with your camera index
    
    try:
        capture_image(camera_device, image_path)
        send_telegram_message(image_path, "New Login")
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)
Test the script:

sh
Copy code
python logsnap.py
Setup to Run on Login
Open Task Scheduler:

Press Win + R, type taskschd.msc, and press Enter.

Create a new task:

Click on Create Task... in the right-hand Actions pane.
In the General tab, give your task a name (e.g., LogSnap) and optionally a description.
Set the trigger:

Go to the Triggers tab and click New....
In the Begin the task dropdown, select At log on.
Optionally, you can specify for which user(s) this task should run.
Click OK.
Set the action:

Go to the Actions tab and click New....
In the Action dropdown, select Start a program.
In the Program/script field, enter the path to your Python executable (e.g., C:\Path\To\Python\python.exe).
In the Add arguments (optional) field, enter the path to your logsnap.py script (e.g., C:\Path\To\LogSnap\logsnap.py).
Click OK.
Finish and save:

Adjust any other settings as needed (e.g., conditions, settings).
Click OK to save and finish creating the task.
Your LogSnap script will now run every time you log in to your PC, capturing an image and sending it to your Telegram account.

csharp
Copy code

You can copy and paste this entire content into your `README.md` file on GitHub. Make sure to replace the placeholder paths with the actual paths used in your environment.




Install the required packages:

sh
Copy code
pip install -r requirements.txt
Configure telegram-send:

Follow the setup instructions for telegram-send to configure it with your Telegram account.

Usage
Update the main() function in logsnap.py with the correct image path and camera device index:

python
Copy code
def main():
    image_path = "C:\\Users\\YOUR_USERNAME\\Desktop\\Image.jpg"
    camera_device = 0 # Update with your camera index
    
    try:
        capture_image(camera_device, image_path)
        send_telegram_message(image_path, "New Login")
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)
Test the script:

sh
Copy code
python logsnap.py
Setup to Run on Login
Open Task Scheduler:

Press Win + R, type taskschd.msc, and press Enter.

Create a new task:

Click on Create Task... in the right-hand Actions pane.
In the General tab, give your task a name (e.g., LogSnap) and optionally a description.
Set the trigger:

Go to the Triggers tab and click New....
In the Begin the task dropdown, select At log on.
Optionally, you can specify for which user(s) this task should run.
Click OK.
Set the action:

Go to the Actions tab and click New....
In the Action dropdown, select Start a program.
In the Program/script field, enter the path to your Python executable (e.g., C:\Path\To\Python\python.exe).
In the Add arguments (optional) field, enter the path to your logsnap.py script (e.g., C:\Path\To\LogSnap\logsnap.py).
Click OK.
Finish and save:

Adjust any other settings as needed (e.g., conditions, settings).
Click OK to save and finish creating the task.

add this to markdown aswell
ChatGPT
Here is the entire README.md content with all the details included in markdown format:

markdown
Copy code
# LogSnap

**LogSnap** is a tool that captures an image using your webcam and sends a notification to your Telegram account on every login to your PC.

## Features

- Captures an image upon user login.
- Sends the captured image to a specified Telegram account with a timestamp.

## Requirements

- Python 3.x
- `pip` (Python package installer)
- `git` (version control system)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/LogSnap.git
   cd LogSnap
Install the required packages:

sh
Copy code
pip install -r requirements.txt
Configure telegram-send:

Follow the setup instructions for telegram-send to configure it with your Telegram account.

Usage
Update the main() function in logsnap.py with the correct image path and camera device index:

python
Copy code
def main():
    image_path = "C:\\Users\\YOUR_USERNAME\\Desktop\\Image.jpg"
    camera_device = 0 # Update with your camera index
    
    try:
        capture_image(camera_device, image_path)
        send_telegram_message(image_path, "New Login")
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)
Test the script:

sh
Copy code
python logsnap.py
Setup to Run on Login
Open Task Scheduler:

Press Win + R, type taskschd.msc, and press Enter.

Create a new task:

Click on Create Task... in the right-hand Actions pane.
In the General tab, give your task a name (e.g., LogSnap) and optionally a description.
Set the trigger:

Go to the Triggers tab and click New....
In the Begin the task dropdown, select At log on.
Optionally, you can specify for which user(s) this task should run.
Click OK.
Set the action:

Go to the Actions tab and click New....
In the Action dropdown, select Start a program.
In the Program/script field, enter the path to your Python executable (e.g., C:\Path\To\Python\python.exe).
In the Add arguments (optional) field, enter the path to your logsnap.py script (e.g., C:\Path\To\LogSnap\logsnap.py).
Click OK.
Finish and save:

Adjust any other settings as needed (e.g., conditions, settings).
Click OK to save and finish creating the task.
Your LogSnap script will now run every time you log in to your PC, capturing an image and sending it to your Telegram account.
