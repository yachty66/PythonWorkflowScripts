from curses import keyname
from pynput import keyboard
from pynput.keyboard import KeyCode
import subprocess

current = []

dictApplications = {"Music": "https://www.youtube.com/watch?v=Dx5qFachd3A", "Drive": "https://drive.google.com/drive/my-drive", "Gmail": "https://mail.google.com/mail/u/0/?tab=km#inbox",
                    "Translate": "https://translate.google.com/", "DailyNotes": "/Users/maxhager/Projects2022/Notes/dailyNotes.md", "Calendar": "/Applications/AppicationsMe/Cron.app", "Todoist": "https://todoist.com/app/today", "MessageCenter":  ("https://mail.google.com/mail/u/0/?tab=km#inbox",  "https://app.slack.com/client/THHRTPPGV/D01A6CT53BM", "https://webmail.htw-berlin.de/currentNG/?_task=mail&_mbox=INBOX", "https://web.whatsapp.com/", "https://discord.com/channels/@me"), "Discord": "https://discord.com/channels/@me", "FocusMode": ['python3', '/Users/maxhager/Projects2022/PythonAutomation/FocusMode/focusMode.py']}

dictOverviewSheet = {"Music": "Control + l", "Drive": "Control + 5", "Gmail": "Control + 5",
                     "Translate": "Control + t", "DailyNotes": "Control + n", "Calendar": "Control + 4", "Todoist": "Control + 9", "MessageCenter": "Control + 2", "Discord": "Control + 1", "FocusMode": "Control + f"}


def execute(param):
    if param == "MessageCenter":
        for i in dictApplications[param]:
            subprocess.call(("open", i))
    elif param == "FocusMode":
        subprocess.call(dictApplications[param])
    else:
        subprocess.call(("open", dictApplications[param]))


def on_press(key):
    current.append(key)
    if keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("n") in current and len(current) == 2:
        execute("DailyNotes")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("l") in current and len(current) == 2:
        execute("Music")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("4") in current and len(current) == 2:
        execute("Calendar")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("5") in current and len(current) == 2:
        execute("Drive")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("7") in current and len(current) == 2:
        execute("Gmail")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("t") in current and len(current) == 2:
        execute("Translate")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("9") in current and len(current) == 2:
        execute("Todoist")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("2") in current and len(current) == 2:
        execute("MessageCenter")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("1") in current and len(current) == 2:
        execute("Discord")
    elif keyboard.Key.ctrl in current and keyboard.KeyCode.from_char("f") in current and len(current) == 2:
        execute("FocusMode")


def on_release(key):
    current.clear()


if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
