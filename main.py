from pytube import YouTube

def download_mp3_or_mp4_from_youtube(youtube_link, format_choice):
    try:
        yt = YouTube("ytsearch:" + youtube_link)

        print("Titolo: ", yt.title)

        if format_choice.lower() == "mp3":
            stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        elif format_choice.lower() == "mp4":
            stream = yt.streams.filter(file_extension='mp4').first()
        else:
            print("Formato non supportato.")
            return

        if stream is not None:
            new_filename = input("Inserisci il nome del file (senza estensione): ")
            filename = new_filename + '.' + format_choice.lower()

            # Starting download
            print(f"Downloading {format_choice.upper()} as '{filename}'...")
            stream.download(filename=filename)
            print(f"{format_choice.upper()} download completato!!")
        else:
            print(f"{format_choice.upper()} non trovato.")
    except Exception as e:
        print("Errore:", str(e))

if __name__ == "__main__":
    youtube_link = input("Inserisci il link di YouTube: ")
    format_choice = input("Vuoi scaricare in MP3 o MP4? (Inserisci 'mp3' o 'mp4'): ")
    download_mp3_or_mp4_from_youtube(youtube_link, format_choice)
