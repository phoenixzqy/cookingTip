#-*- coding: utf-8 -*-
from utils.helpers import *
import curses
import copy


class GUI:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    # add string to given position coordinates[x,y]
    def addStr(self, myStr, coordinates=[None, None], attr=None):
        
        if coordinates[1] != None and coordinates[0] != None:
            if attr != None:
                self.stdscr.addstr(coordinates[1], coordinates[0], myStr, attr)
            else:
                self.stdscr.addstr(coordinates[1], coordinates[0], myStr)
        else:
            if attr != None:
                self.stdscr.addstr(myStr, attr)
            else:
                self.stdscr.addstr(myStr)

    # a wrapper of functions
    def getKey(self):
        return self.stdscr.getkey()

    def clearScreen(self):
        self.stdscr.clear()

    def refreshScreen(self):
        self.stdscr.refresh()

    def showCursor(self):
        curses.curs_set(1)
    def hideCursor(self):
        curses.curs_set(0)

    # multiple selection, coordinates[x,y]
    def multiSelection(
            self,
            options,
            coordinates=[0, 0],
            label=": ",
            single=False,
            enableKeyMonitor=True):
        _Y = 0
        _X = 1
        cursorPos = [0, 0]
        _TITLE = 0
        _SUBMENU = 1
        keyInput = None
        selections = []
        while not (keyInput == "\n" and len(selections) > 0):
            # options list
            for i, sub in enumerate(options):
                self.stdscr.addstr(i + coordinates[1], coordinates[0],
                                   fixedStrLen(sub[_TITLE], 2) + label)
                for j, op in enumerate(sub[_SUBMENU]):
                    if [i, j] in selections:
                        opStr = '[x]' + fixedStrLen(op, 5)
                    else:
                        opStr = '[ ]' + fixedStrLen(op, 5)
                    if [i, j] == cursorPos:
                        self.stdscr.addstr(opStr, curses.A_BOLD)
                    else:
                        self.stdscr.addstr(opStr)

            self.stdscr.addstr(
                self.stdscr.getmaxyx()[0] - 1,
                0,
                "点击 [空格] 选择，点击 [回车] 确认选择。")
            if enableKeyMonitor:
                self.__keyMonitor(keyInput)

            self.stdscr.refresh()
            keyInput = self.stdscr.getkey()
            # apply selection changes
            if keyInput == "KEY_UP" and cursorPos[_Y] > 0:
                cursorPos[_Y] -= 1
                if cursorPos[_X] >= len(options[cursorPos[_Y]][1]):
                    cursorPos[_X] = len(options[cursorPos[_Y]][1]) - 1
            elif keyInput == "KEY_DOWN" and cursorPos[_Y] < len(options) - 1:
                cursorPos[_Y] += 1
                if cursorPos[_X] >= len(options[cursorPos[_Y]][1]):
                    cursorPos[_X] = len(options[cursorPos[_Y]][1]) - 1
            elif keyInput == "KEY_LEFT" and cursorPos[_X] > 0:
                cursorPos[_X] -= 1
            elif keyInput == "KEY_RIGHT" and cursorPos[_X] < len(options[cursorPos[_Y]][1]) - 1:
                cursorPos[_X] += 1
            elif keyInput == " ":
                if single:
                    selections = []
                    selections.append(copy.deepcopy(cursorPos))
                else:
                    if cursorPos in selections:
                        selections.remove(copy.deepcopy(cursorPos))
                    else:
                        selections.append(copy.deepcopy(cursorPos))

        return selections

    # input area, coordinates[x,y]
    def rawInput(self, coordinates=[0, 0]):
        curses.echo()
        input = self.stdscr.getstr(coordinates[1], coordinates[0])
        curses.noecho()
        return input.decode("utf-8")

    def scrollableTextArea(self, title, arr, y1, y2, x = 4):
        pos = 0
        while True:
            self.stdscr.clear()
            self.stdscr.addstr(title)
            for i in range(0 + pos, y2 - y1 + pos):
                if i >= len(arr):
                    break
                self.stdscr.addstr(y1 + i - pos, x, arr[i])
            self.stdscr.addstr(
                self.stdscr.getmaxyx()[0] - 1,
                0,
                "使用鼠标滚轴翻页，点击[b]键返回主菜单")
            self.stdscr.refresh()
            key = self.stdscr.getkey()
            if  key == "KEY_DOWN" and pos < len(arr) - y2 + y1:
                pos += 1
            elif key == "KEY_UP" and pos > 0:
                pos -= 1
            elif key == "b":
                break
        
    # a helper to display a key monitor at bottom right corner
    def __keyMonitor(self, keyStr=""):
        if keyStr == None:
            keyStr = ""
        if keyStr == "\n":
            keyStr = "KEY_ENTER"
        self.__monitor(-1, "Key Monitor: ", fixedStrLen(keyStr, 10, "right"))

    def __monitor(self, y, title, content):
        self.stdscr.addstr(
            self.stdscr.getmaxyx()[0] + y,
            self.stdscr.getmaxyx()[1] - len(title + content) - 1,
            title + content)
