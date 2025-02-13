# SyncFix

SyncFix is a simple Python program designed to hide or unhide folders on Windows. This can be useful for making folders invisible to other users on the system, enhancing privacy and organization.

## Features

- Hide folders to make them invisible to other users.
- Unhide folders to make them visible again.

## Requirements

- Windows operating system.
- Python 3.x installed on your system.

## Installation

1. Clone the repository or download the `syncfix.py` file to your local machine.

```bash
git clone https://github.com/yourusername/syncfix.git
```

2. Navigate to the directory where the `syncfix.py` file is located.

```bash
cd syncfix
```

## Usage

To use SyncFix, open a command prompt and navigate to the directory containing `syncfix.py`. Use the following commands:

- To hide a folder:

```bash
python syncfix.py hide "C:\path\to\your\folder"
```

- To unhide a folder:

```bash
python syncfix.py unhide "C:\path\to\your\folder"
```

Replace `"C:\path\to\your\folder"` with the actual path of the folder you wish to hide or unhide.

## Disclaimer

This program modifies folder attributes using the `attrib` command on Windows. Use it with caution and ensure you have appropriate permissions to modify the folder attributes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.