from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re


def removeSpecialCharacters(title):
    # Define a regular expression pattern to match special characters
    pattern = r'[^\w\s.-]'

    # Check if the title contains any special characters
    if re.search(pattern, title):
        invalid_chars = ['?', '#', '!', '😔', '💔', '🖤', '>','<', ':', '*', '|', '\\', '/', '"']
        for char in invalid_chars:
            title = title.replace(char, "")

        # Remove leading or trailing whitespaces
        title = title.strip()

        # Replace any remaining whitespace with underscores
        title = title.replace(" ", "_")

    return title


def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")
    cookies = {
        '__cflb': '0H28vWmzwPGiuttmnGdD2Q6RZYuaZqg3KdiDRnXsDxR',
        '_gid': 'GA1.2.1152090873.1686384745',
        '_gat_UA-3524196-9': '1',
        '_ga': 'GA1.2.1800756006.1686384745',
        '_ga_0E6L67P48P': 'GS1.1.1686384745.1.1.1686384794.0.0.0',
    }

    headers = {
        'authority': 'tiktokdownload.online',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://tiktokdownload.online/',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://tiktokdownload.online',
        'referer': 'https://tiktokdownload.online/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': '',
    }

    print("STEP 4: Getting the download link")
    print("If this step fails, PLEASE read the steps above")
    response = requests.post('https://tiktokdownload.online/abc', params=params, cookies=cookies, headers=headers, data=data)
    print(response)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    downloadLink = downloadSoup.a["href"]
    videoTitle = removeSpecialCharacters(downloadSoup.p.getText().strip())

    print("STEP 5: Saving the video :)")
    mp4File = urlopen(downloadLink)
    # Feel free to change the download directory
    with open(f"6xturi/{id}-{videoTitle}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break


print("STEP 1: Open Chrome browser")
driver = webdriver.Chrome()

driver.get("https://www.tiktok.com/@6xturi")

time.sleep(20)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

print("STEP 2: Scrolling page")
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source, "html.parser")
videos = soup.find_all("div", {"class": "tiktok-1s72ajp-DivWrapper e1cg0wnj1"})

print(len(videos))
for video in videos:
    print(video.a['href'])


print(f"STEP 3: Time to download {len(videos)} videos")
for index, video in enumerate(videos):
    print(f"Downloading video: {index}")
    if video.a['href'] != "https://www.tiktok.com/":
        downloadVideo(video.a["href"], index)
        time.sleep(10)