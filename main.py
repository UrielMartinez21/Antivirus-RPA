import time
import pyautogui
from packages.functions import open_eset_nod32, get_licenses, get_location, click_at_location
from packages.pahts import (
    ACCEPT_ERROR,
    CHANGE_LICENSE,
    CHANGE_SUBS,
    CONTINUE_PROCESS,
    ENTER_LICENSE,
    ERROR_MESSAGE,
    LICENSES,
    ESET_NOD32,
    SECTION,
)


try:
    # -> Get all licenses
    licenses = get_licenses(LICENSES)
    if not licenses:
        raise ValueError("No licenses found in the CSV file.")

    # -> Open ESET NOD32
    open_eset_nod32(ESET_NOD32)
    time.sleep(4)

    # -> Go to objective section
    objective_section = get_location(SECTION)
    click_at_location(objective_section, 1)

    # -> Go to change subscriptions
    change_subs = get_location(CHANGE_SUBS)
    click_at_location(change_subs, 1)

    for license_key in licenses:
        # -> Go to change license
        change_license = get_location(CHANGE_LICENSE)
        click_at_location(change_license, 1)

        # -> Click to enter license
        enter_license = get_location(ENTER_LICENSE)
        click_at_location(enter_license, 1)

        # -> Write the license key
        pyautogui.write(license_key)
        time.sleep(1)

        # -> Click to continue process
        continue_process = get_location(CONTINUE_PROCESS)
        click_at_location(continue_process, 10)

        # -> Check for error message
        error_message = get_location(ERROR_MESSAGE)
        if error_message:
            accept_error = get_location(ACCEPT_ERROR)
            click_at_location(accept_error, 0)
            continue

except Exception as e:
    print(f"[+] Error: {e}")
