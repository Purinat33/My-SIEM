import math
import tkinter as tk
import psutil
import os
import subprocess
import json
import sys
import platform

# https://umeey.medium.com/system-monitoring-made-easy-with-pythons-psutil-library-4b9add95a443
total_mem = psutil.virtual_memory().total / (1024.0 ** 3)


class app:
    def __init__(self, master_frame: tk.Tk):
        self.master = master_frame  # The frame that will be destroyed
        # Option bar
        # Design
        # https://youtu.be/95tJO7XJlko?si=E_P8k0TmksxL1fZb
        self.option_frame = tk.Frame(master_frame, bg="#c3c3c3")
        self.option_frame.pack(side=tk.LEFT)
        self.option_frame.pack_propagate(False)
        self.option_frame.configure(width=200, height=500)
        # main_frame
        self.main_frame = tk.Frame(
            master_frame, highlightbackground='black', highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=500, width=1000)

        # Buttons
        self.home_btn = tk.Button(self.option_frame, text="Overview", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.home)
        self.home_btn.place(x=10, y=50)

        # Buttons
        self.file_integrity = tk.Button(self.option_frame, text="File Integrity", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.fim)
        self.file_integrity.place(x=10, y=100)

        # Buttons
        self.application = tk.Button(self.option_frame, text="Process Monitoring", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.process)
        self.application.place(x=10, y=150)

        # Buttons
        self.log = tk.Button(self.option_frame, text="Log Analysis", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.log)
        self.log.place(x=10, y=200)

        self.home()

    def clear(self):
        # Clear MainFrame
        for i in self.main_frame.winfo_children():
            i.destroy()

    def home(self):
        self.clear()
        self.intro = tk.Label(
            self.main_frame, text="System Overview", font=("Helvatica", 18))
        self.intro.pack()
        # https://umeey.medium.com/system-monitoring-made-easy-with-pythons-psutil-library-4b9add95a443
        self.os = platform.system()
        self.platform = tk.Label(
            self.main_frame, text=f"Operating System: {self.os}", font=("Ariel", 14))
        self.platform.pack()

        self.version = tk.Label(
            self.main_frame, text=f"Version: {platform.version()}", font=("Ariel", 14))
        self.version.pack()

        self.architecture = tk.Label(
            self.main_frame, text=f"Architecture: {platform.architecture()[0]}", font=("Ariel", 14)
        )
        self.architecture.pack()

        ############################
        self.total_mem = tk.Label(
            self.main_frame, text=f"Total Memory: {(round(total_mem, 3))} GB", font=("Ariel", 14)
        )
        self.total_mem.pack(pady=10)

    def fim(self):
        self.clear()

    def process(self):
        self.clear()
        # https://www.tutorialspoint.com/how-to-get-the-list-of-running-processes-using-python
        self.processes = psutil.process_iter()
        # for process in self.processes:
        #     # Sort process with the most CPU usage and/or ram usage
        #     print(f"PID: {process.pid}, Name: {process.name()}")

    def log(self):
        self.clear()


root = tk.Tk()
root.geometry("1000x500")
root.title("My SIEM")
# Removing resizing because scaling everything takes a lot of efforts
root.resizable(False, False)
app(master_frame=root)
root.mainloop()
