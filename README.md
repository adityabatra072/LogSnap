
# LogSnap
![WhatsApp Image 2024-07-01 at 7 31 13 PM](https://github.com/adityabatra072/LogSnap/assets/173267139/01ee8193-1dbc-457e-b409-615731e048fd)


## Description
LogSnap notifies you on every login to your PC by sending a Telegram message with an image.

## Requirements
- Python 3.x
- `pip` (Python package installer)
- `telegram-send` (For sending messages via Telegram)

## Setup Instructions

### 1. Clone the Repository
    git clone https://github.com/yourusername/LogSnap.git
    cd LogSnap
    pip install -r requirements.txt
### 2. Setup telegram-send
    telegram-send -c
  and follow the instructions to successfully configure telegram-send bot with api
### 3. Setup your camera in pygame
 Default set to camera at index 0 you can change it as needed refer https://www.pygame.org/docs/ref/camera.html
### 4. Setup to run on login
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

##
  



