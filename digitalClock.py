# Import Libraries
import time as tm
import tkinter as tk
from tkinter import simpledialog
import math
import pygame as pg

# Digital Clock
class DigitalClock:
    # Initiate the window and object attribute
    def __init__(self, window):
        self.window = window
        self.window.title('Digital Clock') # Window title
        self.f = tk.Frame(self.window)
        self.label = tk.Label(self.window, font='cambria 80', bg='black', fg='cyan') # Live Clock Label
        self.label.grid(row=0, column=0, columnspan=2) # Label position

        # Buttons to switch mode
        self.stopwatch_button = tk.Button(self.window, text='Switch to Stopwatch', command=self.stopwatch_mode)
        self.stopwatch_button.grid(row=1, column=0)

        # Alarm Feature
        self.alarm_time = "00:00:00"
        self.set_alarm_button = tk.Button(self.window, text='Set Alarm', width=10, command=self.set_alarm)
        self.set_alarm_button.grid(row=1, column=1)
        pg.init()
        self.alarm_sound = pg.mixer.Sound("alarm_sound.wav")

        self.show_time() # Run the show_time function

    # Function to show the live time
    def show_time(self):
        self.time = tm.strftime('%H:%M:%S')
        self.label['text'] = self.time
        self.window.after(200, self.show_time)
        if self.time == self.alarm_time:
            self.alarm_sound.play()
    
    # Function to run the Stop Watch Window
    def stopwatch_mode(self):
        self.window.destroy()
        stopwatch_window()
    
    # Function to set the alarm
    def set_alarm(self):
        input = simpledialog.askstring("Set Alarm", "Enter alarm time (HH:MM:SS):")
        if input:
            self.alarm_time = input

# Stop Watch
class Stopwatch:
    # Initiate the window and object attribute
    def __init__(self, window):
        self.window = window
        self.window.title('Stopwatch') # Window title
        self.f = tk.Frame(self.window)
        self.label = tk.Label(self.window, font='cambria 80', bg='black', fg='cyan') # Live Stopwatch label
        self.label.grid(row=0, column=0, columnspan=4) # Label position

        # Button and stopwatch attribute
        self.mode_button = tk.Button(self.window, text='Switch to Digital Clock', command=self.switch_mode)
        self.mode_button.grid(row=1, column=0)
        self.run = False
        self.reset_bool = True
        self.start_time = 0
        self.elapsed_time = 0

        # Buttons
        start_button = tk.Button(self.window, text='Start', width=6, command=self.start)
        stop_button = tk.Button(self.window, text='Stop', width=6, command=self.stop)
        reset_button = tk.Button(self.window, text='Reset', width=6, command=self.reset)

        # Buttons Position
        start_button.grid(row=1, column=1)
        stop_button.grid(row=1, column=2)
        reset_button.grid(row=1, column=3)

        self.update_display() # Run update_display function
    
    # Function to start the stopwatch
    def start(self):
        self.run = True
        if self.elapsed_time == 0:
            self.start_time = tm.time()
        else:
            self.start_time = tm.time() - self.elapsed_time
        self.update_stopwatch()
    
    # Function to stop the stopwatch
    def stop(self):
        self.run = False
    
    # Function to reset the stopwatch time
    def reset(self):
        self.reset_bool = False
        if self.run:
            self.stop()
        self.elapsed_time = 0
        self.reset_bool = True
        self.update_display()

    # Function to update the stopwatch
    def update_stopwatch(self):
        while self.run and self.reset_bool:
            self.elapsed_time = tm.time() - self.start_time
            self.update_display()
            self.window.update()
    
    # Function to display the stopwatch and contains the time algorithm
    def update_display(self):
        hour = int(self.elapsed_time) // 3600
        mins = int(self.elapsed_time) // 60 - 60*hour
        sec = int(self.elapsed_time) % 60
        ms = 100*(self.elapsed_time - math.floor(self.elapsed_time))
        self.label['text'] = ('%02d:%02d:%02d:%02d' % (hour, mins, sec, ms))

    # FUnction to switch mode to digital clock
    def switch_mode(self):
        self.window.destroy()
        main_window()

# Function to run the Digital CLock Window
def main_window():
    window = tk.Tk()
    clock = DigitalClock(window)
    window.mainloop()

# Function to run the Stop Watch Window
def stopwatch_window():
    window = tk.Tk()
    stopwatch = Stopwatch(window)
    window.mainloop()

# Execute the program starts from Digital Clock
if __name__ == "__main__":
    main_window()
