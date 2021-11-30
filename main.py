from pytube import YouTube
import os

url = input("Введите ссылку на видео: \n")
yt = YouTube(url)
stream_list = yt.streams.order_by('resolution')
print(f"{stream_list[0].title} доступно в следующих разрешениях: ")
for stream in stream_list:
    a = "с аудио" if stream.includes_audio_track else "без аудио"
    b = "с видео" if stream.includes_video_track else "без видео"
    print(f"Качество: {stream.resolution}, fps: {stream.fps}, {a}/{b}, id: {stream.itag}")
tag = input("Введите id видео для загрузки: \n")
stream = yt.streams.get_by_itag(tag)

default_path = os.path.normpath(os.path.expanduser("~/Desktop"))
user_path = input("Введите путь для сохранения видео: \n")
path = user_path if os.path.exists(user_path) and os.path.isdir(user_path) else default_path;
print(f"Путь некорректен, видео будет сохранено в {default_path}")

print("Начинаю скачивание...")
stream.download(output_path=path)
print(f'Готово! Скачал {stream.title} в качестве {stream.resolution}')
