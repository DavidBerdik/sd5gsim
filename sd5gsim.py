from tkinter import *
from libs.SD5GSim_GUI import SD5GSim_GUI

def main():
    root = Tk()
    my_gui = SD5GSim_GUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
