import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import keyboard
import pyperclip
import pyautogui
import threading
import time
import json

def get_clipboard_text():
    try:
        return pyperclip.paste()
    except Exception:
        return ""

def set_clipboard_text(text):
    try:
        pyperclip.copy(text)
    except Exception:
        pass

def is_already_transformed(text):
    return text.startswith("Position\tText")

def transform_text(text):
    lines = text.splitlines()
    result = ["Position\tText"]
    counter = 1

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if '.' in line and line[:line.find('.')].isdigit():
            number, rest = line.split('.', 1)
            result.append(f"{number.strip()}\t{rest.strip()}")
        else:
            result.append(f"{counter}\t{line}")
            counter += 1

    return '\r\n'.join(result)

def simulate_paste():
    pyautogui.hotkey('ctrl', 'v')

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except:
        return {"hotkey": "ctrl+shift+c"}  # fallback default

def action():
    text = get_clipboard_text()
    if not text or is_already_transformed(text):
        return

    transformed = transform_text(text)
    set_clipboard_text(transformed)
    time.sleep(0.1)
    simulate_paste()

def handle_hotkey():
    config = load_config()
    hotkey = config["hotkey"]
    keyboard.add_hotkey(hotkey, action)
    keyboard.wait()  # Keeps the thread alive


def create_image():
    img = Image.open("icon.png")
    return img.resize((16, 16))

def on_exit(icon, item):
    icon.stop()

def run_tray():
    icon = pystray.Icon("Clipboard Formatter")
    icon.icon = create_image()
    icon.menu = pystray.Menu(item('Exit', on_exit))
    icon.title = "Clipboard Formatter Running"
    icon.run()

if __name__ == "__main__":
    threading.Thread(target=handle_hotkey, daemon=True).start()
    run_tray()
