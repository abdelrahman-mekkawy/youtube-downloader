from tkinter import*
from yt_dlp import YoutubeDL 

def high_quality():
    try:
        url = entry.get()
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s' 
        }

        with YoutubeDL(ydl_opts) as ydl: 
            ydl.download([url])
            print("The video has been downloaded in high quality.")
    except Exception as e:
        print(f"Error: {e}")

def low_quality():
    try:
        url = entry.get() 
        ydl_opts = {
            'format': 'worst',
            'outtmpl': 'downloads/%(title)s.%(ext)s' 
                            }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("The video has been downloaded in low quality.")
    except Exception as e:
        print(f"Error: {e}")

def get_audio():
    try:
        url = entry.get()
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("The audio has been downloaded.")
    except Exception as e:
        print(f"Error: {e}")

window = Tk()
window.title("YouTube Downloader")
window.geometry("600x400")
window.configure(bg="#3bcc88")

Label(window, text="Add your YouTube link:", bg="#3bcc88", font=("Arial", 12)).place(x=200, y=30)

entry = Entry(window, width=50)
entry.place(x=150, y=100)

high_quality=Button  (window, text="High Quality", command=high_quality, font=("Arial", 10)).place(x=100, y=200)
low_quality=Button ( window, text="Low Quality", command=low_quality, font=("Arial", 10)).place(x=250, y=200)
get_audio=Button ( window, text="Get Audio", command=get_audio, font=("Arial", 10)).place(x=400, y=200)

window.mainloop()
