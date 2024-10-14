import logging
import os
import time
import tkinter as tk
from tkinter import MULTIPLE, Listbox, messagebox

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

"""
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
"""


# Function to extract video links from the given user
def extract_video_links(username):
    logging.info(f"Extracting video links for username: {username}")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")  # Enable headless mode

    # Provide the path to your WebDriver if it's not in the system's PATH
    driver = webdriver.Chrome(options=chrome_options)

    # Open the user's video page
    url = f"https://kick.com/{username}/videos"
    driver.get(url)

    # Wait for some time to let the page fully load
    time.sleep(10)
    """WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, f'a[href^="/{username}/videos/"]')
        )
    )"""

    # Extract all video links using the updated method
    video_elements = driver.find_elements(
        By.CSS_SELECTOR, f'a[href^="/{username}/videos/"]'
    )

    # Extract the href attributes from the video elements
    video_links = [element.get_attribute("href") for element in video_elements]

    logging.info(f"video_links: {video_links}")

    # Write all video links to a text file
    with open("video_links.txt", "w") as file:
        for link in video_links:
            logging.info(link)
            file.write(link + "\n")

    # Close the browser after extraction
    driver.quit()

    return video_links


# Function to start downloads using yt-dlp for selected video links
def start_download(selected_links):
    # Write selected links to a temporary file
    with open("selected_links.txt", "w") as file:
        for link in selected_links:
            file.write(link + "\n")

    # yt-dlp command to download videos
    command = "yt-dlp -a selected_links.txt"

    # Run the yt-dlp command
    os.system(command)

    # Notify user that download has started
    messagebox.showinfo("Download", "Downloads started successfully.")


# Function to handle user input and display links
def show_video_links():

    logging.info("show_video_links()")

    username = entry.get().strip()

    if not username:
        messagebox.showerror("Input Error", "Please enter a valid username.")
        return

    # Extract video links using the entered username
    try:
        video_links = extract_video_links(username)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract video links: {e}")
        return

    # Clear the listbox and add new links
    listbox.delete(0, tk.END)
    for link in video_links:
        listbox.insert(tk.END, link)


# Function to launch downloads for selected videos
def launch_downloads():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning(
            "Selection Error", "Please select at least one video to download."
        )
        return

    selected_links = [listbox.get(i) for i in selected_indices]
    start_download(selected_links)


# Function to select all items in the listbox
def select_all():
    listbox.select_set(0, tk.END)


# Setting up the tkinter UI
root = tk.Tk()
root.title("Video Downloader")

# Input field for username
label = tk.Label(root, text="Enter Username:")
label.pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button to show video links
show_button = tk.Button(root, text="Show Video Links", command=show_video_links)
show_button.pack(pady=10)

# Listbox to display video links
listbox = Listbox(root, selectmode=MULTIPLE, width=80, height=15)
listbox.pack(pady=5)

# Button to select all video links
select_all_button = tk.Button(root, text="Select All", command=select_all)
select_all_button.pack(pady=5)

# Button to launch downloads
download_button = tk.Button(root, text="Launch Download", command=launch_downloads)
download_button.pack(pady=10)

# Start the tkinter main loop
root.mainloop()
