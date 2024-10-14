# Video Downloader with Selenium, yt-dlp, and Tkinter

## Overview

This project is a **Video Downloader** tool that allows users to extract video links from the popular streaming platform [Kick](https://kick.com/) and download the videos using `yt-dlp`. The application is built using **Selenium** for web scraping, **yt-dlp** for video downloads, and **Tkinter** for the graphical user interface (GUI).

### Features:

- **Extract video links** from a user's profile page.
- **Select specific videos** to download or choose to download all videos.
- **Download videos** via `yt-dlp` with ease.
- **Simple GUI** for ease of use.

## Requirements

Make sure you have the following installed before running the application:

1. **Python 3.7+**
2. **Selenium** for web scraping.
   - Install Selenium using:
     ```bash
     pip install selenium
     ```
   - You will also need to download a compatible WebDriver (like **ChromeDriver**). Ensure the driver is either in your system's `PATH` or provide the path explicitly in the script.

3. **yt-dlp** for downloading videos.
   - Install yt-dlp using:
     ```bash
     pip install yt-dlp
     ```

4. **Tkinter** for the graphical user interface.
   - Tkinter comes pre-installed with Python on most systems.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/video-downloader.git
   cd video-downloader
   ```

2. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Download and place the **ChromeDriver** (or appropriate WebDriver for your browser) in your system's `PATH` or update the script to point to the WebDriver location.

## Usage

1. **Run the application**:

   ```bash
   python video_downloader.py
   ```

2. The GUI will prompt you to enter a **Kick.com username**. Click **Show Video Links** to fetch all available video links from that user's profile.

3. Select the videos you want to download from the list, or click **Select All** to select all available videos.

4. Click **Launch Download** to start downloading the selected videos using `yt-dlp`.

## Logging

The application includes detailed logging for debugging purposes. The log outputs include:
- Information about video link extraction.
- Errors encountered during the download process.
- Debug logs for internal states and processes.

You can modify the logging level in the script based on your preference. The logs will help identify issues if video extraction or download fails.

## Notes

- **Selenium WebDriver** will open an actual browser session (Chrome) to extract video links from Kick.com.
- **yt-dlp** is a powerful video downloader that supports various platforms, including YouTube and Kick.com. It will download the videos from the selected links.

## Contribution

Feel free to submit issues, fork this repository, and submit pull requests. Contributions are welcome to improve the tool or add new features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
