#-*- coding: utf-8 -*-

import pages.mainMenu
import pages.recipe
import pages.sourceMenu


def getPage(page, stdscr):
    if page == "main_menu":
        pages.mainMenu.MainMenu(stdscr).render()
    elif page == "recipe":
        pages.recipe.Recipe(stdscr).render()
    elif page == "source_menu":
        pages.sourceMenu.SourceMenu(stdscr).render()
