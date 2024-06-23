import pygame
import schedule
import time
import threading
import webbrowser
import tkinter as tk
from tkinter import messagebox

def set_alarm():
    alarm_time = entry.get() # 기입창의 텍스트를 문자열로 반환
    schedule.every().day.at(alarm_time).do(play_alarm)
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

def play_alarm():
    pygame.mixer.music.load("alarm_sound.wav")
    pygame.mixer.music.play(loops=4)
    stop_button.config(state=tk.NORMAL)

def stop_alarm():
    pygame.mixer.music.stop()
    stop_button.config(state=tk.DISABLED)
    open_web_page()

def open_web_page():
    webbrowser.open("https://www.youtube.com/watch?v=FAcIUOaQJn4")

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

pygame.mixer.init()

root = tk.Tk()
root.title("Alarm Clock")

tk.Label(root, text="Set Alarm Time (HH:MM):").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Set Alarm", command=set_alarm).pack()

stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm, state=tk.DISABLED)
stop_button.pack()

threading.Thread(target=run_schedule).start()

root.mainloop()