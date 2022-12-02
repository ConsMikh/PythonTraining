'''
Получает содержание файла

Выделение записей про помидорки
Транмформация записей о помидорке к нужному виду с условием глубины анализа

Добавление к дереву нового узла или перезапись существующего узла
Возврат дерева
'''
from anytree import Node, Resolver, RenderTree

class Parser():

    def __init__(self, deep=4):
        self.deep = deep
        self.root = Node('detail', parent=None)
        self.nodes = {}

    def parseFile(self, lines):
        pomidor = 0
        for line in lines:
            if ('#' in line) & (pomidor == 1):pomidor = 0
            if((pomidor == 1) & (line[0] != '\n')): 
                pom_record = self.parseLine(line)
                self.checkNode(pom_record)
            if '#Помидорки' in line:
                pomidor = 1

    def parseLine(self, line):
        line_parts = line.split(':')
        part_num = 1
        pom_rec = []
        timespend = line_parts[-1]
        if len(line_parts) - 1 < self.deep:
            for part in line_parts:
                if (part != timespend) & (part_num < self.deep):
                    pom_rec.append(part.strip())
                    part_num += 1
                else:
                    break
            while part_num <= self.deep:
                pom_rec.append("Без указания")
                part_num += 1
        else:
            for partn in range(0, self.deep):
                pom_rec.append(line_parts[partn].strip())
        if ('+' in timespend): 
            timespend = timespend.count('+')
        pom_rec.append(int(timespend))
        return pom_rec

    def checkNode(self, pom_record):
        parent = self.root
        for node in pom_record[:-1]:
            try:
                if self.nodes[node] in parent.children:
                    parent = self.nodes[node]
            except:
                self.nodes[node] = Node(node, parent = parent)
                parent = self.nodes[node]
            else:
                pass


    def addNode(self):
        pass

    def replaceNode(self):
        pass

    def transformTree(self):
        pass 

    def renderTree(self):
        for pre, _, node in RenderTree(self.root):
            print("%s%s" % (pre, node.name))