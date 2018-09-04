import pages.page
import config
from utils.jsonHelper import JsonHelper

import pages.mainMenu

class SourceMenu(pages.page.Page):
    __options = [
        ["猪", ["瘦猪肉", "排骨", "猪耳朵", ]],
        ["牛", ["牛肉", "牛排", "牛筋", "牛肚", ]],
        ["羊", ["羊肉", "羊排", "羊腿", ]],
        ["鸡", ["鸡肉", "鸡翅", "鸡腿", "鸡蛋" ]],
        ["蔬菜", ["白菜", "油菜", "菠菜", "土豆"]],
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

        input = None
        if [9, 0] in selection:
            self.gui.showCursor()
            self.gui.addStr("请输入自定义食材（不同食材之间使用[空格]区分，按[回车]键结束编辑。）: ", [0, 14])
            input = self.gui.rawInput([4, 15])
            self.gui.hideCursor()
        
        sources = []
        for s in selection:
            sources.append(self.__options[s[0]][1][s[1]])
        if(input != None):
            for s in input.split(' '):
                sources.append(s)
        jh = JsonHelper()
        result = jh.searchBySource(sources)
        self.gui.clearScreen()
        editedResult = []
        for i in result:
            editedResult.append("菜名： " + i["name"])
            editedResult.append("评分： " + str(i["score"]))
            editedResult.append("食材： " + i["source"])
            editedResult.append("链接： " + config.base_url + i["url"])
            editedResult.append(" ")
        self.gui.scrollableTextArea(
            "查询结果：",
            editedResult,
            3,
            self.stdscr.getmaxyx()[0] - 3,
            5
        )
        # back to main menu
        pages.mainMenu.MainMenu(self.stdscr).render()
