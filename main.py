import tkinter as tk


class app:
    def __init__(self, master_frame: tk.Tk):
        self.master = master_frame  # The frame that will be destroyed
        # Option bar
        # Design
        # https://youtu.be/95tJO7XJlko?si=E_P8k0TmksxL1fZb
        self.option_frame = tk.Frame(master_frame, bg="#c3c3c3")
        self.option_frame.pack(side=tk.LEFT)
        self.option_frame.pack_propagate(False)
        self.option_frame.configure(width=100, height=400)
        # main_frame
        self.main_frame = tk.Frame(
            master_frame, highlightbackground='black', highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=400, width=500)

        # Buttons
        self.home_btn = tk.Button(self.option_frame, text="Home", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.home)
        self.home_btn.place(x=10, y=50)

        # Buttons
        self.file_integrity = tk.Button(self.option_frame, text="FIM", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.fim)
        self.file_integrity.place(x=10, y=100)

        # Buttons
        self.application = tk.Button(self.option_frame, text="Process", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.process)
        self.application.place(x=10, y=150)

        # Buttons
        self.log = tk.Button(self.option_frame, text="Log", font=(
            "Bold", 15), fg="#158aff", bd=0, bg="#c3c3c3", command=self.log)
        self.log.place(x=10, y=200)

    def home(self):
        # Clear MainFrame
        for i in self.main_frame.winfo_children():
            i.destroy()

    def fim(self):
        pass

    def process(self):
        pass

    def log(self):
        pass


root = tk.Tk()
root.geometry("600x400")
root.title("My SIEM")
app(master_frame=root)
root.mainloop()
