import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys

sys.path.insert(0 , sys.path[0] + '/exercises')

from videoProcessing import *
from exercises.sample1 import ArmStretch
from exercises.lateralRaises2 import LateralRaises
# from exercises.sample3 import legStretch

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Workout Tracker")
        self.configure(bg="lightblue")
        self.geometry("960x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, ExercisePage, ExerciseDetailsPage):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def set_background_image(self, frame, image_path):
        img = Image.open(image_path)
        background_image = ImageTk.PhotoImage(img)
        canvas = tk.Canvas(frame, width=img.width, height=img.height)
        canvas.pack(fill="both", expand=True)

        for child in frame.winfo_children():
            if child != canvas:
                child.lift()

        canvas.create_image(0, 0, image=background_image, anchor="nw")
        canvas.image = background_image

class StartPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="lightblue")
        title_label = tk.Label(self, text="WORKOUT TRACKER", font=("Arial", 32), bg="lightblue")
        title_label.place(relx=0.5, rely=0.3, anchor="center")
        start_exercise_button = tk.Button(self, text="Start Exercise", command=lambda: parent.show_frame(ExercisePage),
                                          font=("Arial", 16), bg="red", fg="white", height=2, width=20)
        start_exercise_button.place(relx=0.5, rely=0.5, anchor="center")

class ExercisePage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="lightblue")
        header = tk.Label(self, text="Workout Tracker", font=("Arial", 24), bg="lightblue")
        header.place(relx=0.5, rely=0.1, anchor="center")

        exercise_title = tk.Label(self, text="Select Your Exercise", font=("Arial", 16), bg="lightblue")
        exercise_title.place(relx=0.5, rely=0.3, anchor="center")

        exercises = ["Lateral Raises", "Arm Curl"]
        self.exercise_variable = tk.StringVar(self)
        self.exercise_variable.set(exercises[0])
        exercise_dropdown = tk.OptionMenu(self, self.exercise_variable, *exercises)
        exercise_dropdown.place(relx=0.5, rely=0.4, anchor="center")

        rep_label = tk.Label(self, text="Enter Desired Reps", font=("Arial", 16), bg="lightblue")
        rep_label.place(relx=0.5, rely=0.5, anchor="e")

        self.rep_count = tk.StringVar()
        rep_entry = tk.Entry(self, textvariable=self.rep_count)
        rep_entry.place(relx=0.5, rely=0.5, anchor="w")

        back_button = tk.Button(self, text="Back", command=lambda: parent.show_frame(StartPage),
                                font=("Arial", 16), bg="red", fg="white", height=2, width=20)
        back_button.place(relx=0.5, rely=0.7, anchor="center")

        start_button = tk.Button(self, text="Start Exercise", command=self.start_exercise,
                                 font=("Arial", 16), bg="green", fg="white", height=2, width=20)
        start_button.place(relx=0.5, rely=0.6, anchor="center")

    def start_exercise(self):
        selected_exercise = self.exercise_variable.get()
        rep_count = self.rep_count.get()

         # Check the value of the rep count
        if not rep_count.isdigit() or int(rep_count) < 1 or int(rep_count) > 30:
            messagebox.showerror("Invalid Rep Count", "Please enter the number of reps between 1-30")
            return

        # Print the values on the terminal
        print("Selected Exercise:", selected_exercise)
        print("Number of Reps:", rep_count)

        exercise_details = (selected_exercise, rep_count)
        self.master.frames[ExerciseDetailsPage].update_details(exercise_details)
        self.master.show_frame(ExerciseDetailsPage)

class ExerciseDetailsPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.exercise_label = tk.Label(self, text="", font=("Arial", 16), bg="lightblue")
        self.exercise_label.place(relx=0.5, rely=0.3, anchor="center")

        self.rep_label = tk.Label(self, text="", font=("Arial", 16), bg="lightblue")
        self.rep_label.place(relx=0.5, rely=0.4, anchor="center")

        back_button = tk.Button(self, text="Back", command=lambda: parent.show_frame(ExercisePage),
                                font=("Arial", 16), bg="red", fg="red", height=2, width=20)
        back_button.place(relx=0.5, rely=0.7, anchor="center")

    def update_details(self, exercise_details):
        selected_exercise, rep_count = exercise_details
        self.exercise_label.configure(text=f"Selected Exercise: {selected_exercise}")
        self.rep_label.configure(text=f"Number of Reps: {rep_count}")

if __name__ == "__main__":
    app = Application()
    app.set_background_image(app.frames[StartPage], "images/bg.jpg")
    app.set_background_image(app.frames[ExercisePage], "images/bg.jpg")
    app.set_background_image(app.frames[ExerciseDetailsPage], "images/bg.jpg")
    app.mainloop()