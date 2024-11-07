import os
from youtubesearchpython import VideosSearch
import yt_dlp

music_list = [
    "DAO - Her",
    "IDLES - Never Fight A Man With a Perm",
    "Low Roar - I'll Keep Coming",
    "Rodrigo Ogi - Hahaha"
]

def search_youtube(query):
    videos_search = VideosSearch(query, limit=1)
    result = videos_search.result()["result"]
    if result:
        return result[0]['link']
    return None

def download_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

output_directory = "musicas_baixadas"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for i, music in enumerate(music_list, start=1):
    print(f"Buscando música: {music}")
    video_url = search_youtube(music)
    
    if video_url:
        print(f"Baixando: {music}")
        output_path = os.path.join(output_directory, f"{i} - {music}")
        download_audio(video_url, output_path)
    else:
        print(f"Vídeo não encontrado para: {music}")

print("Download concluído!")
