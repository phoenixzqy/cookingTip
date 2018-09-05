#-*- coding: utf-8 -*-

import json
import settings

class DbHelper:
    def __init__(self):
        # read database
        with open(settings.db_path, 'r') as f:
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
            temp = self.__applySourceFilter(dish['source'].split(','))
            isSubset = True
            for t in temp:
                if t not in sourceArr:
                    isSubset = False
                    break
            if isSubset and len(temp) != 0:
                result.append(dish)
        return result

    def __applySourceFilter(self, arr):
        sourceFilter = settings.config["source_filter"]
        result = []
        for item in arr:
            shouldRemove = False
            for test in sourceFilter:
                if test in item:
                    shouldRemove = True
                    break
            if not shouldRemove:
                result.append(item)
        return result
