import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Gotowe!", text_color="green")
    except:
        title.configure(text="")
        progressBar.set(0)
        pPercentage.configure(text='0%')
        finishLabel.configure(text="Niepoprawny link", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #Update porgress bar
    progressBar.set(float(percentage_of_compeletion) / 100)

#def optionmenu_callback(choice):
#    print("optionmenu dropdown clicked:", choice)

#System Settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk()
app.geometry("620x280")
app.title("YouTube Downloader v0.1")

#Adding UI Elements
title = customtkinter.CTkLabel(app, text="Wprowadź link YouTube: ")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Resolution Button
#resolution = customtkinter.CTkOptionMenu(master=app,
#                                       values=["Wysoka Jakość", "Niska Jakość"],
#                                       command=optionmenu_callback)
#resolution.pack(padx=20, pady=10)
#resolution.set("Wysoka Jakość")  # set initial value


#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Progress percentege
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()


#Download Button
download = customtkinter.CTkButton(app, text="Rozpocznij pobieranie!", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()