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
    try:
        page = MainMenu(stdscr)
        page.render()
    except KeyboardInterrupt:
        # When user press ctrl + c. then just exit the app
        exit()

curses.wrapper(main)

# end curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
