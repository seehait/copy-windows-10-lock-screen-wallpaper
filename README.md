# Copy Windows 10 Lock Screen Wallpaper

[![Travis](https://travis-ci.com/seehait/copy-windows-10-lock-screen-wallpaper.svg?branch=master)](https://travis-ci.com/seehait/copy-windows-10-lock-screen-wallpaper)
[![GitHub license](https://img.shields.io/github/license/seehait/copy-windows-10-lock-screen-wallpaper.svg)](https://github.com/seehait/copy-windows-10-lock-screen-wallpaper/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/copy-windows-10-lock-screen-wallpaper.svg)](https://pypi.org/project/copy-windows-10-lock-screen-wallpaper)

Copy Windows 10 current lock screen wallpaper to destination directory.

## Table of Contents

- [Requirement](#requirement)
- [Installation](#installation)
  - [Installing from PyPI](#installing-from-pypi)
  - [Installing from Git](#installing-from-git)
- [Usage](#usage)
- [License](#license)

## Requirement

- Microsoft Windows 10
- Python 3.6+

## Installation

### Installing from PyPI

```sh
pip3 install copy-windows-10-lock-screen-wallpaper
```

### Installing from Git

1. Clone this repository
2. Run `python3 setup.py install`.

## Usage

```sh
copy-lock-screen-wallpaper [--destination {destination_directory}]
```

### Example

```sh
copy-lock-screen-wallpaper
```

```sh
copy-lock-screen-wallpaper --destination C:\
```

## License

(C) 2019 Seehait Chockthanyawat.

*Copy Windows 10 Lock Screen Wallpaper* is licensed under [MIT License](LICENSE)
