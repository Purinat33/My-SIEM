import math
import tkinter as tk
import psutil
import os
import subprocess
import json
import sys
import platform
from tkinter import ttk


# https://umeey.medium.com/system-monitoring-made-easy-with-pythons-psutil-library-4b9add95a443
total_mem = psutil.virtual_memory().total / (1024.0 ** 3)


def get_avail_mem():
    return psutil.virtual_memory().available / (1024.0 ** 3)


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_disk_info():
    partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.mountpoint] = {
            "total_space": partition_usage.total / (1024.0 ** 3),
            "used_space": partition_usage.used / (1024.0 ** 3),
            "free_space": partition_usage.free / (1024.0 ** 3),
            "usage_percentage": partition_usage.percent
        }
    return disk_info


TEXT_FONT = ("Ariel", 14)
HEIGHT = 700
WIDTH = 1000

# CPU
physical_cores = psutil.cpu_count(logical=False)
total_cores = psutil.cpu_count(logical=True)
cpu_speed = psutil.cpu_freq().current


class app:
    def __init__(self, master_frame: tk.Tk):
        self.master = master_frame  # The frame that will be destroyed
        # Option bar
        # Design
        # https://youtu.be/95tJO7XJlko?si=E_P8k0TmksxL1fZb
        self.option_frame = tk.Frame(master_frame, bg="#c3c3c3")
        self.option_frame.pack(side=tk.LEFT)
        self.option_frame.pack_propagate(False)
        self.option_frame.configure(width=WIDTH-800, height=HEIGHT)
        # main_frame
        self.main_frame = tk.Frame(
            master_frame, highlightbackground='black', highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=HEIGHT, width=WIDTH)

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

        self.disks = tk.Button(self.option_frame, text="Disks Overview", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.disk)
        self.disks.place(x=10, y=250)

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
            self.main_frame, text=f"Operating System: {self.os}", font=TEXT_FONT)
        self.platform.pack()

        self.version = tk.Label(
            self.main_frame, text=f"Version: {platform.version()}", font=TEXT_FONT)
        self.version.pack()

        self.architecture = tk.Label(
            self.main_frame, text=f"Architecture: {platform.architecture()[0]}", font=TEXT_FONT
        )
        self.architecture.pack()

        ############################
        self.total_mem = tk.Label(
            self.main_frame, text=f"Total Memory: {(round(total_mem, 3))} GB", font=TEXT_FONT
        )
        self.total_mem.pack(pady=10)

        # Free Memory, will change so we need a refresh button
        self.avail_mem = tk.Label(
            self.main_frame, text=f"Available Memory: {round(get_avail_mem(), 3)} GB", font=TEXT_FONT
        )
        self.avail_mem.pack()

        self.refresh = tk.Button(
            self.main_frame, text="Refresh Available Memory", font=("Ariel", 12), command=lambda: self.updateAvailMem(self.avail_mem)
        )
        self.refresh.pack()

        #######################
        self.total_cpu_phy = tk.Label(
            self.main_frame, text=f"Physical Cores: {physical_cores}", font=TEXT_FONT
        )
        self.total_cpu_phy.pack(pady=10)

        self.total_core = tk.Label(
            self.main_frame, text=f"Total Cores: {total_cores}", font=TEXT_FONT
        )
        self.total_core.pack()

        self.speed = tk.Label(
            self.main_frame, text=f"CPU Speed: {cpu_speed} MHz", font=TEXT_FONT
        )
        self.speed.pack()

        self.cpu_usage = tk.Label(
            self.main_frame, text=f"Average CPU Usage: {round(get_cpu_usage(), 3)} %", font=TEXT_FONT
        )
        self.cpu_usage.pack()

        self.refresh2 = tk.Button(
            self.main_frame, text="Refresh CPU Usage", font=("Ariel", 12), command=lambda: self.updateCPU(self.cpu_usage)
        )
        self.refresh2.pack()

    def updateAvailMem(self, avail_mem):
        avail_mem.config(
            text=f"Available Memory: {round(get_avail_mem(), 3)} GB", font=TEXT_FONT
        )

    def updateCPU(self, use_cpu):
        use_cpu.config(
            text=f"Average CPU Usage: {round(get_cpu_usage(), 3)} %", font=TEXT_FONT
        )

    def disk(self):
        self.clear()
        # Show each disk
        self.intro_disk = tk.Label(
            self.main_frame, text="Disk Overview", font=("Helvatica", 18))
        self.intro_disk.pack()

        self.disk_info = get_disk_info()
        for drive, info in self.disk_info.items():
            self.disk_name = tk.Label(
                self.main_frame, text=f"Drive {drive}", font=("Helvatica", 16)
            )
            self.disk_name.pack(pady=10)
            self.total_space = tk.Label(
                self.main_frame, text=f"Total Space: {round(info['total_space'], 3)} GB", font=TEXT_FONT
            )
            self.total_space.pack()
            self.used_space = tk.Label(
                self.main_frame, text=f"Used Space: {round(info['used_space'], 3)} GB", font=TEXT_FONT
            )
            self.used_space.pack()
            self.free_space_gb = round(info['free_space'], 3)
            self.free_space = tk.Label(
                self.main_frame, text=f"Free Space: {self.free_space_gb} GB", font=TEXT_FONT
            )
            self.free_space.pack()
            self.disk_percent = tk.Label(
                self.main_frame, text=f"Usage: {round(info['usage_percentage'], 3)}%", font=TEXT_FONT
            )
            self.disk_percent.pack()

    def fim(self):
        self.clear()
        # Show disk data
        self.intro_fim = tk.Label(
            self.main_frame, text="File Integrity Overview", font=("Helvatica", 18))
        self.intro_fim.pack()

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
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title("My SIEM")
# Removing resizing because scaling everything takes a lot of efforts
root.resizable(False, False)
app(master_frame=root)
root.mainloop()
