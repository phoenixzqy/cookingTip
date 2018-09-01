import pages.page
from pages.sourceMenu import SourceMenu
from pages.randomMenu import RandomMenu
from pages.recipe import Recipe


class MainMenu(pages.page.Page):
    __options = [
        ["1", ["我这有这些食材，小二你看能给做点什么菜？"]],
        ["2", ["你随便给我推荐几道菜吧！"]],
        ["3", ["你给我说说这道菜怎么做？"]],
        ["4", ["下次再说吧"]],
    ]

    def render(self):
        self.gui.clearScreen()
        self.gui.addStr("客官您上座～ 请问您想要点啥？", [0, 0])
        selection = self.gui.multiSelection(self.__options, [4, 3], ". ", True)

        # confirm selection
        if [0, 0] in selection:
            SourceMenu(self.stdscr).render()
        elif [1, 0] in selection:
            RandomMenu(self.stdscr).render()
        elif [2, 0] in selection:
            Recipe(self.stdscr).render()
        else:
            exit()
