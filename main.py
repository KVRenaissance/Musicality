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

def play_song():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_song():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_song():
    global current_song, paused

    try:
        songlist.selection_clear(0, END) # Clear the current selection
        songlist.selection_set(songs.index(current_song) + 1) # Select the next song
        current_song = songs[songlist.curselection()[0]] # Get the next song in the list
        play_song() # Play the next song
    except:
        pass

def previous_song():
    global current_song, paused

    try:
        songlist.selection_clear(0, END) # Clear the current selection
        songlist.selection_set(songs.index(current_song) - 1) # Select the previous song
        current_song = songs[songlist.curselection()[0]] # Get the previous song in the list
        play_song() # Play the previous song
    except:
        pass

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

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_song)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_song)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_song)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0, command=previous_song)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()