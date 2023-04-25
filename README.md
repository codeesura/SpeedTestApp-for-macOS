# SpeedTestApp for macOS

This application allows you to measure and display your internet speed on the macOS menu bar using Python and the rumps package. It uses Ookla's Speedtest API to measure your internet speed.

## Features

- Real-time speed test on the macOS menu bar
- Display download and upload speeds
- Speed test status with progress notification
- Display speed test results as a notification

## Requirements

- Python 3.6+
- rumps package
- speedtest-cli package

## Installation

1. Clone or download the repo:


```bash
git clone https://github.com/codeesura/SpeedTestApp-for-macOS.git
```


2. Install required packages:

```bash
pip install rumps speedtest-cli
```


3. Run the application:


```bash
python SpeedTestApp.py
```


## Usage

- Start the application by clicking on the "📶" icon in the menu bar.
- Start the speed test by clicking on the "Speed Test" item.
- During download and upload speed tests, the progress percentage will be displayed in the menu bar.
- When the test is complete, the results will be displayed as a notification and in the menu bar.

## License

MIT License - See the `LICENSE` file for more information.
