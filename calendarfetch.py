from datetime import datetime
import time
import os
import sys


def get_system_timezone():
    # Windows
    if sys.platform == "win32":
        try:
            import winreg

            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"SYSTEM\CurrentControlSet\Control\TimeZoneInformation"
            )

            windows_tz, _ = winreg.QueryValueEx(key, "TimeZoneKeyName")
            winreg.CloseKey(key)

            windows_to_iana = {
                "UTC": "Etc/UTC",
                "GMT Standard Time": "Europe/London",
                "W. Europe Standard Time": "Europe/Berlin",
                "FLE Standard Time": "Europe/Helsinki",
                "E. Europe Standard Time": "Europe/Bucharest",
                "Russian Standard Time": "Europe/Moscow",
                "Turkey Standard Time": "Europe/Istanbul",
                "Central Europe Standard Time": "Europe/Budapest",
                "Romance Standard Time": "Europe/Paris",
                "Central European Standard Time": "Europe/Warsaw",
                "Eastern Standard Time": "America/New_York",
                "Central Standard Time": "America/Chicago",
                "Mountain Standard Time": "America/Denver",
                "Pacific Standard Time": "America/Los_Angeles",
                "Alaskan Standard Time": "America/Anchorage",
                "Hawaiian Standard Time": "Pacific/Honolulu",
                "Tokyo Standard Time": "Asia/Tokyo",
                "Korea Standard Time": "Asia/Seoul",
                "China Standard Time": "Asia/Shanghai",
                "India Standard Time": "Asia/Kolkata",
                "Singapore Standard Time": "Asia/Singapore",
                "AUS Eastern Standard Time": "Australia/Sydney",
                "New Zealand Standard Time": "Pacific/Auckland",
            }

            return windows_to_iana.get(windows_tz, windows_tz)

        except Exception:
            return datetime.now().astimezone().tzname()

    # Linux / macOS
    try:
        with open("/etc/timezone", "r") as f:
            timezone = f.read().strip()
            if timezone:
                return timezone
    except (FileNotFoundError, PermissionError):
        pass

    try:
        localtime = os.path.realpath("/etc/localtime")
        marker = "/zoneinfo/"

        if marker in localtime:
            return localtime.split(marker, 1)[1]
    except OSError:
        pass

    return datetime.now().astimezone().tzname()


print("\033[31m" r"""
                                                                          
            ▄▄                ▄▄               ▄▄                   ▄▄    
            ██                ██              ██         ██         ██    
▄████  ▀▀█▄ ██ ▄█▀█▄ ████▄ ▄████  ▀▀█▄ ████▄ ▀██▀ ▄█▀█▄ ▀██▀▀ ▄████ ████▄ 
██    ▄█▀██ ██ ██▄█▀ ██ ██ ██ ██ ▄█▀██ ██ ▀▀  ██  ██▄█▀  ██   ██    ██ ██ 
▀████ ▀█▄██ ██ ▀█▄▄▄ ██ ██ ▀████ ▀█▄██ ██     ██  ██▄█▀  ██   ▀████ ██ ██ 
                                                                          
                                                                """ "\033[0m")


timezone = get_system_timezone()

print(f"Time Zone: {timezone}")

while True:
    now = datetime.now().astimezone()

    print(
        f"\rDate & Time: {now:%Y-%m-%d %H:%M:%S}",
        end="",
        flush=True
    )

    time.sleep(1)
