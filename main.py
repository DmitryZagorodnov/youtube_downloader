from pytube import YouTube

url = input("Введите ссылку на видео: \n")
yt = YouTube(url)

stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
print("Начинаю скачивание...")
stream.download()
print(f'Готово! Скачал {stream.title} в качестве {stream.resolution}')