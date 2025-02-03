# NeoSoft

NeoSoft is a Python-based application that synchronizes the system time on Windows machines with internet atomic clocks. It uses the Network Time Protocol (NTP) to ensure accurate timekeeping by connecting to global NTP servers.

## Features

- Synchronizes system time with atomic clocks using NTP.
- Specifically designed for Windows operating systems.
- Simple and easy-to-use command-line interface.

## Requirements

- Python 3.x
- `ntplib` library

## Installation

1. Clone the repository or download the `neosync.py` file.
2. Ensure that Python is installed on your machine.
3. Install the `ntplib` library, if not already installed:

   ```bash
   pip install ntplib
   ```

## Usage

Run the script using Python:

```bash
python neosync.py
```

The program will attempt to connect to an NTP server and update the system time accordingly. Make sure to run the script with administrative privileges on Windows to allow changes to the system time.

## Limitations

- Currently supports only Windows operating systems.
- Requires administrative privileges to change system time.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.