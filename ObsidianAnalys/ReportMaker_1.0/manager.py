

# Менеджер задачи для недельного отчета
'''
Определение начальной даты анализа
Определение конечной даты анализа
Определение глубины анализа записи о помидорке (в текущей реализации - не глубже 3)
Определение вида представления
Определение локальных настроек с путями
Определение нормативного количества помидорок

Определение параметров представления
    полнота:
    - подробное - вся информация за каждый день
    - краткое - только обобщенные параметры
    - полное - краткое + полное
    
    способ вывода:
    - вывод на экран
    - вывод в json
    - вывод в markdown

Вызов определителя списка дат

Создание словаря для хранения результатов анализа

Вызов анализатора

Создание параметров представления

Вызов Менеджера визуализации
'''

import datetime
import configparser


from analyzer import AnalyzerManager

class WeekManager():
    '''Менеджер для создания недельно отчета'''

    def __init__(self) -> None:
        self.log = [] # log list for writing error in parameters
        self.analyst = {}

    def setTask(self, startdate, lastdate, deep, vistype, visout, settingspath):
        '''Получение параметров для создания отчета'''
        self.startdate = startdate
        self.lastdate = lastdate
        self.deep = deep
        self.vistype = vistype
        self.visout = visout
        self.settingspath = settingspath
    
    def checkDateFormate(self, date):
        '''Проверка формата даты'''
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except:
            self.log.append(f'У даты {date} неверный формат (YYYY-mm-dd)\n')

    def checkPeriod(self):
        '''Проверка того, что стартовая дата раньше конечной'''
        try:
            datetime.datetime.strptime(self.lastdate, '%Y-%m-%d').date() - datetime.datetime.strptime(self.startdate, '%Y-%m-%d').date()
        except:
            self.log.append(f'Дата {self.startdate} и {self.lastdate} не образует диапазон\n')
        else:
            if (datetime.datetime.strptime(self.lastdate, '%Y-%m-%d').date() - datetime.datetime.strptime(self.startdate, '%Y-%m-%d').date()).days < 0:
                self.log.append(f'Конечная дата раньше начальной\n')

    def checkSettings(self):
        try:
            config = configparser.ConfigParser()
            config.read(self.settingspath)
        except:
            self.log.append(f'Файл с настройками недоступен\n')
        else:
            if config.get("local_path","week_report") == '':
                self.log.append(f'Отсутсвует путь до папки с еженедельными отчетами\n')
            if config['local_path']['daily_notes'] == '':
                self.log.append(f'Отсутсвует путь до папки с еженедельными заметками\n')
            if config['local_path']['kbase_notes'] == '':
                self.log.append(f'Отсутсвует путь до папки с заметками\n')
            if config['analyst']['norma_pom'] == '':
                self.log.append(f'Отсутсвует нормативное значение помидорок\n')

    def isTaskValid(self):
        '''Проверка параметров отчета на валидность'''
        self.checkDateFormate(self.startdate)
        self.checkDateFormate(self.lastdate)
        self.checkPeriod()
        self.checkSettings()
        if len(self.log) == 0:
            return True
        else:
            return False

    def startTask(self):
        '''Запуск анализа'''
        analyzer = AnalyzerManager()
        analyzer.setAnalyst(self.startdate, self.lastdate, self.deep, self.analyst, self.settingspath)
        analyzer.startAnalyst()
        print(f'Analyzed: {analyzer.getAnalystLog()}')
        print(f'Log: {analyzer.getLog()}')

    def getLog(self):
        '''Доступ к логу выполнения задачи'''
        return self.log



# Менеджер задачи для проектного отчета
