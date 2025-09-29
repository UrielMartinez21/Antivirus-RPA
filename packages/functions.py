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


def get_location(image_path: str, confidence: float = 0.85) -> tuple:
    return pyautogui.locateCenterOnScreen(image_path, confidence=confidence)


def click_at_location(location: tuple, time_to_sleep: int) -> None:
    if location:
        pyautogui.click(location)
        time.sleep(time_to_sleep)
    else:
        raise ValueError("Location not found on the screen.")


def update_license_status(csv_path: str, license_key: str, new_status: str) -> bool:
    """
    Update the status of a specific license in the CSV file.
    
    Args:
        csv_path (str): Path to the CSV file
        license_key (str): License key to update
        new_status (str): New status to set (e.g., "Error", "Activada", "Procesando")
    
    Returns:
        bool: True if update was successful, False otherwise
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Check if the license exists in the CSV
        license_mask = df['Licencias'] == license_key
        if not license_mask.any():
            print(f"⚠️ License {license_key} not found in CSV")
            return False
        
        # Update the status
        df.loc[license_mask, 'Estatus'] = new_status
        
        # Save the updated CSV
        df.to_csv(csv_path, index=False)
        
        print(f"✅ Updated license {license_key} status to: {new_status}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating license status: {str(e)}")
        return False


def get_license_with_status(csv_path: str) -> list:
    """
    Get all licenses with their current status from CSV.
    
    Args:
        csv_path (str): Path to the CSV file
    
    Returns:
        list: List of tuples (license_key, current_status)
    """
    try:
        df = pd.read_csv(csv_path)
        return list(zip(df['Licencias'].tolist(), df['Estatus'].tolist()))
    except Exception as e:
        print(f"❌ Error reading licenses with status: {str(e)}")
        return []


def get_pending_licenses(csv_path: str) -> list:
    """
    Get only licenses with 'Pendiente' status.
    
    Args:
        csv_path (str): Path to the CSV file
    
    Returns:
        list: List of pending license keys
    """
    try:
        df = pd.read_csv(csv_path)
        pending_licenses = df[df['Estatus'] == 'Pendiente']['Licencias'].tolist()
        return pending_licenses
    except Exception as e:
        print(f"❌ Error getting pending licenses: {str(e)}")
        return []