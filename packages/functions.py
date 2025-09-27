import os
import time
import pyautogui
import subprocess
import pandas as pd


def open_eset_nod32(path: str) -> None:
    if os.path.exists(path):
        subprocess.Popen([path])
    else:
        raise FileNotFoundError(f"The specified path does not exist: {path}")


def get_licenses(path: str) -> list:
    data = pd.read_csv(path)
    return data["Licencias"].tolist()


def get_location(image_path: str, confidence: float = 0.85) -> tuple:
    return pyautogui.locateCenterOnScreen(image_path, confidence=confidence)


def click_at_location(location: tuple, time_to_sleep: int) -> None:
    if location:
        pyautogui.click(location)
        time.sleep(time_to_sleep)
    else:
        raise ValueError("Location not found on the screen.")