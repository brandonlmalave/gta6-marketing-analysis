import subprocess
import sys
import os
import webbrowser
import time

def main():
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")
    
    process = subprocess.Popen(
        ["python", "-m", "streamlit", "run", script_path],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    
    time.sleep(4)
    webbrowser.open("http://localhost:8501")
    process.wait()

if __name__ == "__main__":
    main()