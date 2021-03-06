from services.user_service import UserService
from tkinter import *
import tkinter
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
matplotlib.use("TkAgg")


class MatplotlibUI:
    def __init__(self, root, email):
        self._email = email
        self._root = root
        self._user_serv = UserService()
        self._frame = None
        self.padding = {"padx": 5, "pady": 5}
        self._font = ("Roboto", 12)

    def _mathplotframe(self):
        self._frame = Toplevel(self._root)
        matplotlib.style.use("ggplot")
        self._frame.title("Weight track")
        datelist, weightlist = self._user_serv.fetch_weights_to_frame(
            self._email)
        figure = Figure(figsize=(10, 10), dpi=100)
        add = figure.add_subplot(111)
        add.plot(weightlist, datelist, color="red", linestyle="dashed")
        add.set_xlabel("Dates")
        add.set_ylabel("Weights (kg)")
        add.set_title("Weight track")
        figure.autofmt_xdate(rotation=45, ha="center")
        canvas = FigureCanvasTkAgg(figure, self._frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew", **self.padding)
        close_btn = Button(self._frame, text="Close",
                           command=self._destroy, font=self._font)

        close_btn.bind("<Return>", lambda click: [self._destroy()])
        close_btn.grid(row=0, column=0, **self.padding)

    def _destroy(self):
        self._frame.destroy()
