from pytube import YouTube
import configparser
import os

def check_and_create_download_path(path):
    """Проверяет наличие указанной директории и, если она не существует, создаёт её."""
    if not os.path.exists(path):
        os.makedirs(path)

# Читаем файл конфигурации
config = configparser.ConfigParser()
config.read('config.ini')
download_path = config['DOWNLOAD']['path']

# Проверяем и создаем папку для загрузки, если она не существует
check_and_create_download_path(download_path)

os.system('clear')  # Для UNIX-подобных систем, включая Linux и macOS или os.system('cls') для Windows

def download_best_mp4_video(link):
    yt = YouTube(link)
    print(f"🎦 Видео для скачивания: {yt.title}")


def is_valid_youtube_url(url):
    if "youtube.com" in url or "youtu.be" in url:
        return True
    return False

my_url = input("🌐 Введите ссылку на YouTube видео: ")


if is_valid_youtube_url(my_url):
    download_best_mp4_video(my_url)
else:
    print("🔞 Пожалуйста, введите корректную ссылку на YouTube видео.")
