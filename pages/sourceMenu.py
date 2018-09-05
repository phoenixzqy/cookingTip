#-*- coding: utf-8 -*-
import settings
import routers
import pages.page
from utils.dbHelper import DbHelper



class SourceMenu(pages.page.Page):
    __options = settings.config['options']['source_menu']

    def render(self):
        self.gui.clearScreen()
        self.gui.addStr("请问客官您都有什么食材？", [0, 0])
        selection = self.gui.multiSelection(self.__options, [4, 3], ": ")
        menuLen = len(settings.config['options']['source_menu'])
        input = None
        if [menuLen - 1, 0] in selection:
            self.gui.showCursor()
            self.gui.addStr(
                "请输入自定义食材（不同食材之间使用[空格]区分，按[回车]键结束编辑。）: ", [0, menuLen + 4])
            input = self.gui.rawInput([4, menuLen + 5])
            self.gui.hideCursor()

        sources = []
        for s in selection:
            sources.append(self.__options[s[0]][1][s[1]])
        if(input != None):
            for s in input.split(' '):
                sources.append(s)
        jh = DbHelper()
        result = jh.searchBySource(sources)
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
            "查询到" + str(len(editedResult)) + "个结果：",
            editedResult,
            3,
            self.stdscr.getmaxyx()[0] - 3,
            5
        )
        # back to main menu
        routers.getPage("main_menu", self.stdscr)
