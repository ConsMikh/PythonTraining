import pandas as pd


# Парсер для глубины 3
'''
Получает содержание файла
Выделяет раздел с описание помидорок
Преобразует записи о помидорках в словарь, установленной глубины
Возвращает словарь
'''

# Агрегатор
'''
Получает 
    словарь лога проверки

Считает сумму помидорок по проектам

Считает обобщенные характеристики
    - сколько всего дней для анализа
    - сколько всего файлов нашлось
    - список дат, для которых не нашлось файлов
    - список рубрик, которые попались
    - список эпиков для каждой рубрики
    - общее количество учтенных полезных помидорок
    - подсчет процента учтенных полезных помидорок относительно нормативного
    - количество неполных записей о помидорке

Возвращает агрегированный словарь
'''

# Менеджер анализатора
'''
Получает 
    список дат
    Локальные пути
    Глубину поиска
    Словарь для хранения результатов анализа

Создает словарь лога проверки

В цикле формирует путь к файлу, пытается его открыть
    Если открылся, то вызывает парсер файла, соответствующий глубине поиска
    Накапливает данные за весь набор дат в словаре лога проверки

Вызывает агрегатор

Возвращает словарь для хранения результатов анализа
'''

import datetime
import configparser

class AnalyzerManager():

    def __init__(self) -> None:
        self.log = []
        self.analyst_log = []

    def setAnalyst(self, startdate, lastdate, deep, analyst, settingspath):
        self.start_date = startdate
        self.last_date = lastdate
        self.deep = deep
        self.analyst = analyst
        self.settings_path = settingspath
        self.config = configparser.ConfigParser()
        self.config.read(self.settings_path)

    def getDatesList(self):
        '''Определитель списка дат 
        Получает начальую дату
        и конечную дату
        Возвращет все даты из указанного диапазона
        '''
        start_date = datetime.date.fromisoformat(self.start_date)
        end_date = datetime.date.fromisoformat(self.last_date)
        return pd.date_range(
            min(start_date, end_date),
            max(start_date, end_date)
            ).strftime('%Y-%m-%d').tolist()

    def lineAnalyst(self, line):
        line_parts = line.split(':')
        theme = line_parts[0]
        project = line_parts[1]
        timespend = line_parts[-1]
        if project == timespend:
            project = 'None'
        # Посчитать затраченное время, если оно вводилось с помощью +
        if ('+' in timespend): 
            timespend = timespend.count('+')
        return theme, project, int(timespend)

    def parser(self, lines, date):
        result = {'date': date}
        themes = []
        for line in lines:
            if ('#' in line) & (pomidor == 1):pomidor = 0
            if((pomidor == 1) & (line[0] != '\n')): 
                theme, project, time = self.lineAnalyst(line)
                try:
                    result[theme][project] += time
                except:
                    result[theme] = {}
                    result[theme][project] = time
            if '#Помидорки' in line: pomidor = 1
        return result

    def startAnalyst(self):
        dates_list = self.getDatesList()
        daily_notes_path = self.config['local_path']['daily_notes']
        for analyzed_date in dates_list:
            print(analyzed_date)
            try:
                with open(daily_notes_path + '\\' + analyzed_date +'.md', encoding="utf-8") as f:
                    print(daily_notes_path + '\\' + analyzed_date +'.md ' + 'open')
                    lines = f.readlines()
                    self.analyst_log.append(self.parser(lines, analyzed_date))
            except: 
                self.log.append('Дата ' + analyzed_date + ' отсутствует')


    def getLog(self):
        return self.log

    def getAnalystLog(self):
        return self.analyst_log

