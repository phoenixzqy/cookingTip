import pages.page


class RandomMenu(pages.page.Page):
    __dishSelections = []
    __options1 = [
        ["1", ["不要荤菜"]],
        ["2", ["来一个吧"]],
        ["3", ["来两份"]],
        ["4", ["两份不够来三份"]],
        ["5", ["我可是肉食主义者，四份！"]],
        ["6", ["小瞧我了不是，五份走起！"]],
        ["7", ["我们这是大聚餐，至少来个六份吧"]],
    ]
    __options2 = [
        ["1", ["不吃素菜"]],
        ["2", ["来一个吧"]],
        ["3", ["来两份"]],
        ["4", ["两份不够来三份"]],
        ["5", ["我可是素食食主义者，四份！"]],
        ["6", ["小瞧我了不是，五份走起！"]],
        ["7", ["我们这是大聚餐，至少来个六份吧"]],
    ]
    __options3 = [
        ["1", ["我不喝汤"]],
        ["2", ["来一碗吧"]],
        ["3", ["最多来两种汤品吧"]],
    ]

    def render(self):
        self.gui.clearScreen()
        # subpage 1
        self.gui.addStr("请问客官您荤素如何搭配呢？\n\n先说说荤菜吧:")
        self.__dishSelections.append(
            self.gui.multiSelection(self.__options1, [6, 3], ". ", True))

        self.gui.clearScreen()
        # subpage 2
        self.gui.addStr("请问客官您荤素如何搭配呢？\n\n那您需要几份素菜:")
        self.__dishSelections.append(
            self.gui.multiSelection(self.__options2, [6, 3], ". ", True))

        self.gui.clearScreen()
        # subpage 3
        self.gui.addStr("请问客官您荤素如何搭配呢？\n\n那客官您要不要来碗热汤:")
        self.__dishSelections.append(
            self.gui.multiSelection(self.__options3, [6, 3], ". ", True))
