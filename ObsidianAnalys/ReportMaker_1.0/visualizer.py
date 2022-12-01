'''
На визуализаторах можно потренировать наследование
'''

# визуализотор MarkDown
'''
Получает словарь с результатами
Получает путь до папки с результатами
Получает настройки полноты

Формирует текст заголовка
Формирует части в соответствии с настройками полноты
Объединяет части 
Сохраняет части в файл по пути
'''

# визуализотор JSON
'''
Получает словарь с результатами
Получает путь до папки с результатами
Получает настройки полноты

Отбирает необходимые части из словаря результатов
Сохраняет в JSON виде в нужный файл
'''

# визуализотор JSON
'''
Получает словарь с результатами
Получает путь до папки с результатами
Получает настройки полноты

Отбирает необходимые части из словаря результатов
Формирует текст заголовка
Формирует части в соответствии с настройками полноты для вывода экран
Объединяет части 
Выводит на экран
'''

# Менеджер визуализации
'''
Получает 
    настройки визуализации
    локальные пути
    словарь с результатами
Запускает визуализотор MarkDown
Запускает визуализотор JSON
Запускает визуализотор на экран
'''

class VisualizerManager:

    def __init__(self):
        pass

    def setVisual(self, vis_type, vis_out, data):
        self.vis_type = vis_type
        self.vis_out = vis_out
        self.data = data
        self.output = []

        # Разбить макет на титул, общее, подробное
    
    def makeMaket(self):
        
        self.output.append(f"# Еженедельный отчет за период с {self.data['start_date']} по {self.data['last_date']}\n")
        self.output.append(f'\n')
        self.output.append(f'\n')
        self.output.append(f"Количество дней в периоде: {self.data['days']}\n")
        self.output.append(f"Количество проанализированных дней: {self.data['days_analyst']}\n")
        self.output.append(f"Даты, для которых не найдена заметка: {self.data['lost_dates']}\n")
        self.output.append(f"Темы недели: {self.data['themes']}\n")
        self.output.append(f"Всего осмысленных помидорок: {self.data['total_pom']}\n")
        self.output.append(f"Процент учтенных осмысленных помидорок относительно максимально возможного за период: {self.data['effective_all_days']}\n")
        self.output.append(f"Процент учтенных осмысленных помидорок относительно проанализированных дней: {self.data['effective_know_days']}\n")
        self.output.append(f"Учет помидорок для тем по проектам:\n")
        for theme in self.data['themes']:
            self.output.append(f"{theme}\n")
            for project in self.data[theme].keys():
                self.output.append(f"{project}\t-\t{self.data[theme][project]}\n")
            self.output.append(f'\n')
        

    def startVisual(self):
        
        self.makeMaket()


