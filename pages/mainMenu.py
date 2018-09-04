import pages.page
from pages.sourceMenu import SourceMenu
# from pages.randomMenu import RandomMenu
from pages.recipe import Recipe
import sys

class MainMenu(pages.page.Page):
    __options = [
        ["1", ["我这有这些食材，小二你看能给做点什么菜？"]],
        ["2", ["你给我说说这道菜怎么做？"]],
        ["3", ["下次再说吧"]],
        # TODO: 随机推荐菜品功能，需要对数据做更细化的分类，例如荤菜素菜汤羹甜品等做详细分类，否则很难推荐精准。
        # ["2", ["你随便给我推荐几道菜吧！"]],
    ]

    def render(self):
        self.gui.clearScreen()
        self.gui.addStr("客官您上座～ 请问您想要点啥？", [0, 0])
        selection = self.gui.multiSelection(self.__options, [4, 3], ". ", True)

        # confirm selection
        if [0, 0] in selection:
            SourceMenu(self.stdscr).render()
        # elif [1, 0] in selection:
        #     RandomMenu(self.stdscr).render()
        elif [1, 0] in selection:
            Recipe(self.stdscr).render()
        else:
            sys.exit()
