import ntplib
import time
import os
import ctypes
from datetime import datetime

class NeoSoft:
    def __init__(self):
        self.client = ntplib.NTPClient()
        self.ntp_server = 'pool.ntp.org'

    def synchronize_time(self):
        try:
            print("Connecting to NTP server...")
            response = self.client.request(self.ntp_server, version=3)
            if response:
                print("NTP server response received.")
                self.set_system_time(response.tx_time)
                print("System time synchronized successfully.")
            else:
                print("Failed to get response from NTP server.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def set_system_time(self, ntp_time):
        # Convert NTP time to local time
        local_time = time.localtime(ntp_time)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
        print(f"Setting system time to: {formatted_time}")

        # Set system time on Windows
        if os.name == 'nt':
            self.set_windows_time(local_time)
        else:
            print("This script currently only supports Windows systems.")

    def set_windows_time(self, local_time):
        # Create SYSTEMTIME structure
        class SYSTEMTIME(ctypes.Structure):
            _fields_ = [
                ("wYear", ctypes.c_ushort),
                ("wMonth", ctypes.c_ushort),
                ("wDayOfWeek", ctypes.c_ushort),
                ("wDay", ctypes.c_ushort),
                ("wHour", ctypes.c_ushort),
                ("wMinute", ctypes.c_ushort),
                ("wSecond", ctypes.c_ushort),
                ("wMilliseconds", ctypes.c_ushort),
            ]

        # Initialize SYSTEMTIME structure with local time
        system_time = SYSTEMTIME(
            wYear=local_time.tm_year,
            wMonth=local_time.tm_mon,
            wDay=local_time.tm_mday,
            wHour=local_time.tm_hour,
            wMinute=local_time.tm_min,
            wSecond=local_time.tm_sec,
            wMilliseconds=0
        )

        # Set the system time
        ctypes.windll.kernel32.SetSystemTime(ctypes.byref(system_time))

if __name__ == "__main__":
    print("NeoSoft Time Synchronizer")
    neosoft = NeoSoft()
    neosoft.synchronize_time()