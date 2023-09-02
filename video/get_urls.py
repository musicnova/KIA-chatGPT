import requests
import json

response = requests.get("https://www.kia.ru/ajax/page/mediacenter/reviews/more?limit=100&page=1&with_tags=0")
data = response.json()

videoDict = {}

for el in data['content']['video_bank']['videos']:
    original_link = el['video_link']
    video_link = f"https://youtu.be/{original_link.split('/')[-1].split('?')[0]}"
    videoDict[original_link] = video_link

print(videoDict)
print(f"Количество записей в словаре: {len(videoDict)}")
