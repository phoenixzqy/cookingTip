import json


class JsonHelper:
    def __init__(self):
        # read database
        with open('database_backup/item_list.json', 'r') as f:
            self.data = json.load(f)[2]['data']

    def searchByName(self, name):
        result = []
        for dish in self.data:
            if name in dish['name']:
                result.append(dish)
        return result

    def searchBySource(self, sourceArr):
        result = []
        for dish in self.data:
            temp = self.__removeExcludeItems(dish['source'].split(','))
            isSubset = True
            for t in temp:
                if t not in sourceArr:
                    isSubset = False
                    break
            if isSubset and len(temp) != 0:
                result.append(dish)
        return result

    def __removeExcludeItems(self, arr):
        excludeItems = ["糖", "盐", "醋", "油", "抽",
                        "酱", "葱", "姜", "蒜", "花椒",
                        "八角", "味精", "鸡精", "十三香", "大料",
                        "孜然", "干辣椒", "胡椒"]
        result = []
        for item in arr:
            shouldRemove = False
            for test in excludeItems:
                if test in item:
                    shouldRemove = True
                    break
            if not shouldRemove:
                result.append(item)
        return result
