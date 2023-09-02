from pytube import YouTube, exceptions
import configparser
import os

def check_and_create_download_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_best_mp4_video(link):
    try:
        yt = YouTube(link)
        print(f"🎦 Видео для скачивания: {yt.title}")
        return yt.title
    except exceptions.VideoUnavailable:
        print(f"🔞 Видео недоступно: {link}")
    except exceptions.VideoPrivate:
        print(f"🔞 Видео приватное: {link}")
    except KeyError:
        print(f"🔞 Не удалось получить информацию о видео: {link}")
    return None

def is_valid_youtube_url(url):
    if "youtube.com" in url or "youtu.be" in url:
        return True
    return False

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_titles_to_file(titles, file_path):
    with open(file_path, 'w') as file:
        for title in titles:
            if title:  # Пропустить None значения
                file.write(f"{title}\n")

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')
    download_path = config['DOWNLOAD']['path']

    check_and_create_download_path(download_path)
    os.system('clear')

    urls = read_urls_from_file("urls.txt")
    video_titles = []

    for url in urls:
        # url = url.strip()
        if is_valid_youtube_url(url):
            title = download_best_mp4_video(url)
            if title:  # Добавить только непустые названия
                video_titles.append(title)

    write_titles_to_file(video_titles, "video_titles.txt")
