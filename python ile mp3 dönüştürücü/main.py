import youtube_dl as yd

videoUrl=input("Link giriniz : ")

videoInfo=yd.YoutubeDL().extract_info(
    url=videoUrl,download=False)
fileName=f"{videoInfo['title']}.mp3"
settings={
    'format': 'bestaudio/best',
    'keepvideo':False,
    'outtmpl':fileName,
}

with yd .YoutubeDL(settings) as ydl:
    ydl.download([videoInfo['webpage_url']])

print(f"indirme tamamlandı...{fileName}")