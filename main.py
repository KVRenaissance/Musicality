from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title("Musicality")
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

# Song list setup
songs = []
current_song = ""
accepted_extensions = [".mp3", ".wav", ".flac", ".ogg"] # Multiple ways to play a song!
paused = False

def add_folder():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext in accepted_extensions:
            songs.append(song)
    
    for song in songs:
        songlist.insert("end", song)
    
    songlist.selection_set(0) # Select the first song in the playlist
    current_song = songs[songlist.curselection()[0]] # Get the first song in the list

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label="Add Folder", command=add_folder)
menubar.add_cascade(label="Organise", menu=organise_menu)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file="play.png")
pause_btn_image = PhotoImage(file="pause.png")
next_btn_image = PhotoImage(file="next.png")
prev_btn_image = PhotoImage(file="prev.png")

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()