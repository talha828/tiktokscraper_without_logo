
![CheatBoard](https://github.com/user-attachments/assets/9d6ba3c5-62fe-4838-aecf-6047064cbdab)


# TikTok Video Scraper 🎥

Welcome to the **TikTok Video Scraper** project! 🚀 This tool is designed to help you effortlessly scrape and download TikTok videos from any profile. Whether you're an enthusiast looking to archive your favorite content or a developer in need of bulk video data, this script has you covered!

## Benefits 🌟

- **Easy to Use**: Just run the script, sit back, and let it do the work for you.
- **Automated Download**: Automatically scrolls through the TikTok profile and downloads videos.
- **Customizable**: Modify the script to fit your specific needs.
- **Efficient**: Handles special characters in video titles and ensures smooth downloads.

## How to Use 📋

### Prerequisites

Before you start, ensure you have the following installed:

- Python 3.x
- Selenium
- BeautifulSoup
- Requests

You can install the necessary packages using pip:

```sh
pip install selenium beautifulsoup4 requests
```

### Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/talha828/tiktokscraper_without_logo.git
   cd tiktokscraper_without_logo
   ```

2. **Download the ChromeDriver**:
   - Ensure you have the correct version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your Chrome browser.

3. **Run the Script**:
   - Open the script file and update the TikTok profile URL to the one you wish to scrape.
   - Execute the script:
     ```sh
     python tiktok_scraper.py
     ```

### Script Details

The script follows these steps:

1. **Open Chrome Browser**:
   ```python
   driver = webdriver.Chrome()
   driver.get("https://www.tiktok.com/@6xturi")
   ```

2. **Scroll Through the Page**:
   ```python
   while True:
       driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
       # Check if we've reached the bottom of the page
   ```

3. **Extract Video Links**:
   ```python
   soup = BeautifulSoup(driver.page_source, "html.parser")
   videos = soup.find_all("div", {"class": "tiktok-1s72ajp-DivWrapper e1cg0wnj1"})
   ```

4. **Download Videos**:
   ```python
   for index, video in enumerate(videos):
       downloadVideo(video.a["href"], index)
   ```

## Collaboration 🤝

We welcome contributions from the community! Feel free to fork the repository, create a new branch, and submit a pull request with your improvements.

### Ways to Contribute

- **Bug Reports**: Found a bug? Please report it by opening an issue.
- **Feature Requests**: Have an idea to enhance the script? Let us know!
- **Code Improvements**: Optimizations and refactoring are always appreciated.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Enjoy scraping TikTok videos with ease! If you have any questions or need assistance, feel free to reach out. Happy scraping! 🎉
