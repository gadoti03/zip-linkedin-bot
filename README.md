# LinkedIn Zip Game Automation

## Description
This project automates the LinkedIn Zip game. It navigates through the game page and performs actions automatically based on the starting pointer. 

⚠️ Important: The automation assumes the initial pointer is set to `1`. If previous attempts have been made manually, the pointer might have a different value, causing incorrect behavior.

## Requirements
- Python 3.10+
- Packages listed in `requirements.txt`

Example packages you might need (see `requirements.txt`):
```
beautifulsoup4
selenium
requests
```

## Setup
1. Clone the repository:
```bash
git clone <your-repo-url>
cd <project-folder>
```
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the script:
```bash
python main.py
```
2. The browser will open and navigate to the LinkedIn Zip game login page.
3. Log in with your LinkedIn credentials.
4. Once logged in, return to the terminal and press `<Enter>` to start the automation.

The automation will now play the game automatically.

## Disclaimer
- Make sure the starting pointer in the game is at `1` before running the automation.
- Using automation on platforms like LinkedIn may violate their terms of service. Use this project responsibly and at your own risk.