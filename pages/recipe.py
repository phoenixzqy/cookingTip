#-*- coding: utf-8 -*-
import settings
import routers
import pages.page
from utils.dbHelper import DbHelper
from utils.helpers import *



class Recipe(pages.page.Page):
    def render(self):
        self.gui.clearScreen()
        self.gui.showCursor()
        self.gui.addStr("请输入菜名（按[回车]键结束编辑。）: ", [0, 0])
        input = self.gui.rawInput([4, 2])
        self.gui.hideCursor()

        jh = DbHelper()
        result = jh.searchByName(input)

        self.gui.clearScreen()
        editedResult = []
        for i in result:
            editedResult.append("菜名： " + i["name"])
            editedResult.append("评分： " + str(i["score"]))
            editedResult.append("食材： " + i["source"])
            editedResult.append(
                "链接： " + settings.config['base_url'] + i["url"])
            editedResult.append(" ")
        self.gui.scrollableTextArea(
            "查询结果：",
            editedResult,
            3,
            self.stdscr.getmaxyx()[0] - 3,
            5
        )
        # back to main menu
        routers.getPage("main_menu", self.stdscr)
