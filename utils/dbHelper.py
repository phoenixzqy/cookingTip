# -*- coding: utf-8 -*-

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
            if name in dish['name'] and float(dish["score"]) >= 7:
                result.append(dish)
        return result

    def searchBySource(self, sourceArr):
        result = []
        for dish in self.data:
            if float(dish["score"]) >= 7 and dish['source'] != "" and self.__isSubset(
                    self.__applySourceFilter(dish['source'].split(',')),
                    sourceArr):
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

    def __isSubset(self, arrA, arrB):
        if len(arrA) <= 0 or len(arrB) <= 0:
            return False
        if arrA in arrB:
            return True

        for A in arrA:
            isMatched = False
            for B in arrB:
                # 模糊搜素，类似 里脊 猪里脊肉。尽量做到匹配
                if A in B or B in A:
                    isMatched = True
                    continue
            if not isMatched:
                return False
        return True
