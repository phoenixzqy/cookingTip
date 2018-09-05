#-*- coding: utf-8 -*-

import settings
settings.init()
import routers
import curses
import sys

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
        routers.getPage("main_menu", stdscr).render()
    except KeyboardInterrupt:
        # When user press ctrl + c. then just exit the app
        sys.exit()

# init app with curses exception handler
curses.wrapper(main)

# end curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
