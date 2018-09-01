import pages.page


class SourceMenu(pages.page.Page):
    __options = [
        ["猪", ["猪肉", "排骨", "猪耳朵", ]],
        ["牛", ["牛肉", "牛排", "牛筋", "牛肚", ]],
        ["羊", ["羊肉", "羊排", "羊腿", ]],
        ["鸡", ["鸡肉", "鸡翅", "鸡腿", ]],
        ["蔬菜", ["白菜", "油菜", "菠菜", ]],
        ["菌类", ["木耳", "金针菇",]],
        ["面食", ["手擀面", "挂面", "大饼", ]],
        ["鱼类", ["三文鱼", "龙利鱼", "黑鱼", ]],
        ["海鲜", ["青口", "蛏子", "生蚝", ]],
        ["其他", ["输入自定义食材"]]
    ]

    def render(self):
        self.gui.clearScreen()
        self.gui.addStr("请问客官您都有什么食材？", [0, 0])
        selection = self.gui.multiSelection(self.__options, [4, 3], ": ")

        if [9, 0] in selection:
            self.gui.showCursor();
            self.gui.addStr("请输入自定义食材（不同食材之间使用[空格]区分，按[回车]键结束编辑。）: ", [0, 14])
            input = self.gui.rawInput([4, 15])
            self.gui.hideCursor()
