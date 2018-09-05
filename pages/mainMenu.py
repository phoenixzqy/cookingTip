#-*- coding: utf-8 -*-
import settings
import routers
import pages.page
import sys

class MainMenu(pages.page.Page):
    __options = settings.config['options']['main_menu']
    # TODO: 随机推荐菜品功能，需要对数据做更细化的分类，例如荤菜素菜汤羹甜品等做详细分类，否则很难推荐精准。
        

    def render(self):
        self.gui.clearScreen()
        self.gui.addStr("客官您上座～ 请问您想要点啥？", [0, 0])
        selection = self.gui.multiSelection(self.__options, [4, 3], ". ", True)

        # confirm selection
        if [0, 0] in selection:
            routers.getPage("source_menu", self.stdscr)   
        elif [1, 0] in selection:
            routers.getPage("recipe", self.stdscr)
        else:
            sys.exit()
