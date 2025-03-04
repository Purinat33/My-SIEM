import tkinter as tk
import psutil


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
        self.home_btn = tk.Button(self.option_frame, text="Home", font=(
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
