
# Clipboard Formatter (Beta)

**Clipboard Formatter** is a lightweight system tray utility for Windows.  
It listens for a configurable hotkey (default: `Ctrl+Shift+C`), transforms your clipboard text into a structured, Excel-friendly format, and pastes it automatically.

> Mind that his is a **testing / beta version**. Expect rough edges. Feedback welcome!

---

## Features

- Runs in the system tray with a right-click Exit menu
- Global hotkey (e.g. `Ctrl+Shift+C`, fully configurable via `config.json`)
- Formats text into structured rows with headers:
    ```
    Input:
    1. apple
    2. banana
    cherry

    Output:
    Position    Text
    1           apple
    2           banana
    3           cherry
    ```
- Automatically pastes the result after transformation

---

## Download & Run

> Prebuilt executable is included in the [**Releases**](../../releases) tab!

### Or clone & run manually:
```bash
git clone https://github.com/yourusername/clipboard-formatter.git
cd clipboard-formatter
pip install -r requirements.txt
python clipboard_tray.py

Configuration
Edit the config.json file (auto-created or bundled):

json
Copy
Edit
{
  "hotkey": "ctrl+shift+c",
}
Change "hotkey" to any valid combination like:

ctrl+alt+v

shift+insert

ctrl+space

Set "auto_paste" to false to just copy without pasting.


Limitations (for now)
Windows only

Single hotkey

Clipboard only handles text

Building the Executable
To create a .exe:

pip install pyinstaller
pyinstaller --noconsole --onefile --add-data "icon.png;." clipboard_tray.py
This will generate dist/clipboard_tray.exe.
In the dist you should include the icon.png and the config.json file.

