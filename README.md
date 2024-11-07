# Python MP3 music downloader directly from YouTube

This project was made with Python to download music from YouTube converting it directly into MP3 format.

## Clone project

```
git clone https://github.com/mcello23/python-music-download.git
```

## Necessary software

<b>1. Homebrew</b>

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

<b>2. Python3</b>

```
brew install python3
```

## Dependencies

<b>3. Youtube download library</b>

```
pip3 install yt-dlp
```

- This is an updated version of ```youtube-dl``` dependecy, which downloads audios and videos from YouTube with metadata.
 
<b>4. YouTube search python</b>

```
pip3 install youtubesearchpython
```

- Allows YT search through a string.

<b>5. ffmpeg</b>
```
brew install ffmpeg
```

- Allows the best conversion rate for the MP3 file.

## How to use the script?

Simply open terminal and execute:

```
python3 baixar_musicas.py
```

It will automatically download the songs inside the music_list array, creating a <b>musicas_baixadas</b> folder where you set the script.

To download other songs, simply change the artists :

```
music_list = [
    "John Lennon - Imagine",
    "Nirvana - In Bloom",
    "Led Zeppelin Stairway to Heaven"
]
```
