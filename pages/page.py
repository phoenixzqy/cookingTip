from utils.gui import GUI
class Page:

    # constructor
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.gui = GUI(self.stdscr)
    # setter and getter
