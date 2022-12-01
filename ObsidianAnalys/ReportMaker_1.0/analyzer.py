import pandas as pd
import datetime
import configparser

class WeekAnalyzerManager():

    def __init__(self) -> None:
        self.log = []
        self.analyst_log = []
        self.analyst_result = {}

    def setAnalyst(self, startdate, lastdate, deep, analyst, settingspath):
        '''Настройка анализатора'''
        self.start_date = startdate
        self.last_date = lastdate
        self.deep = deep
        self.analyst = analyst
        self.settings_path = settingspath
        self.config = configparser.ConfigParser()
        self.config.read('D:\\3. Михайлов\\Develop\\PythonTraining\\PythonTraining\\ObsidianAnalys\\ReportMaker_1.0\\' + self.settings_path)
        self.norma_pom = self.config['analyst']['norma_pom']

        self.analyst_result = {
            'start_date': self.start_date,
            'last_date': self.last_date,
            'deep': self.deep,
            'themes': [],
            'lost_dates': [],
            'total_pom': 0
            }

    def getDatesList(self):
        '''Определитель списка дат 
        Получает начальую дату и конечную дату
        Возвращет все даты из указанного диапазона
        '''
        start_date = datetime.date.fromisoformat(self.start_date)
        end_date = datetime.date.fromisoformat(self.last_date)
        return pd.date_range(
            min(start_date, end_date),
            max(start_date, end_date)
            ).strftime('%Y-%m-%d').tolist()

    def lineAnalyst(self, line):
        '''Разбиение и преобразование строки с помидорками'''
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
        '''Подсчет помидорок в одном файле'''
        themes = []
        result = {'date': date}
        pomidor = 0
        for line in lines:
            if ('#' in line) & (pomidor == 1):pomidor = 0
            if((pomidor == 1) & (line[0] != '\n')): 
                theme, project, time = self.lineAnalyst(line)
                if theme not in themes:
                    themes.append(theme)
                try:
                    result[theme][project] += time
                except:
                    try:
                        result[theme][project] = time
                    except:
                        result[theme] = {}
                        result[theme][project] = time
            if '#Помидорки' in line:
                pomidor = 1
        result['themes'] = themes
        return result

    def aggregate(self):
        '''Обобщает данные полученные из файлов'''
        self.analyst_result['days'] = (datetime.datetime.strptime(self.last_date, '%Y-%m-%d').date() - datetime.datetime.strptime(self.start_date, '%Y-%m-%d').date()).days + 1
        self.analyst_result['days_analyst'] = len(self.analyst_log)
        total_pom = 0
        # Подсчет помидорок по эпикам
        for portion in self.analyst_log:
            for theme in portion['themes']:
                if theme not in self.analyst_result['themes']:
                    self.analyst_result['themes'].append(theme)
                    self.analyst_result[theme] = {}
                for project in portion[theme].keys():
                    if project not in self.analyst_result[theme].keys():
                        self.analyst_result[theme][project] = portion[theme][project]
                        total_pom += portion[theme][project]
                    else:
                        self.analyst_result[theme][project] += portion[theme][project]
                        total_pom += portion[theme][project]
        self.analyst_result['total_pom'] = total_pom
        self.analyst_result['max_pom_all_days'] = self.analyst_result['days'] * int(self.norma_pom)
        self.analyst_result['max_pom_know_days'] = len(self.analyst_log) * int(self.norma_pom)
        self.analyst_result['effective_all_days'] = round(total_pom*100.0/float(self.analyst_result['max_pom_all_days']),2)
        self.analyst_result['effective_know_days'] = round(total_pom*100.0/float(self.analyst_result['max_pom_know_days']),2)

    def startAnalyst(self):
        '''Запуск анализа'''
        dates_list = self.getDatesList()
        daily_notes_path = self.config['local_path']['daily_notes']
        for analyzed_date in dates_list:
            try:
                with open(daily_notes_path + '\\' + analyzed_date +'.md', encoding="utf-8") as f:
                    lines = f.readlines()
                    self.analyst_log.append(self.parser(lines, analyzed_date))
            except: 
                self.log.append('Дата ' + analyzed_date + ' отсутствует')
                self.analyst_result['lost_dates'].append(analyzed_date)
        self.aggregate()

    def getLog(self):
        return self.log

    def getAnalystLog(self):
        return self.analyst_log
    
    def getResult(self):
        return self.analyst_result

