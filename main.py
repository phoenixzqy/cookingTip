import curses
from pages.mainMenu import MainMenu

# start curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
stdscr.keypad(True)


def main(stdscr):
    # Clear screen
    stdscr.clear()
    page = MainMenu(stdscr)
    page.render()


curses.wrapper(main)

# end curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
