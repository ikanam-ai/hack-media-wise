### Добро пожаловать на кейс MediaWise "Реклама"!
*** 
В представленном архиве вы можете увидеть следующие папки и файлы

1. Файл **train_data.json** --- датасет из наблюдений со следующими полями:
    1.1. *hash* - идентификатор наблюдения;
    1.2. *targetAudience* - параметры аудитории, а именно возраст, пол и доход (доход является комбинацией букв a, b, c, каждая из которых входит не более одного раза);
    1.3. *points* - конкретный набор географических положений наружной рекламы и ее направления;
    1.4. *value* - значение охвата аудитории 
2. Файл **baseline.ipynb** --- базовое решение.

***

##### Вашей задачей будет разработка модели, предсказывающей величину охвата по входным параметрам аудитории и точек, а также решения, которое на основе параметров подбирает лучший набор точек с точки зрения охвата.

На основе имеющихся пар аудитория-точки необходимо построить модель, которая будет прогнозировать охват наружной релкамы. На основе построенной модели необходимо построить систему предсказания наилучшего набора точек с точки зрения охвата при заданных ограничениях на аудиторию и количество точек. Не забудьте про технические и отраслевые критерии. При построении решения желательно исследование применения геоаналитических данных, например, https://www.openstreetmap.org.

Проверка будет осуществляться с помощью метрики **max(1 - RMSE/30, 0) ^ 4**. Степень выбрана для лучшей дифференциации малых изменений метрики. Чем ближе значение к единице - тем лучше.
**ВАЖНО!!!** Решение сдается на автоматическую проверку в формате .csv.
**ВАЖНО!!!** Обязательно проверьте разделители, заголовки и столбцы, они должны быть аналогичны формату sample_submission.csv

# ЖЕЛАЕМ УДАЧИ!

P.S. Не забудьте посетить экспертные сессии и не стесняйтесь задавать вопросы)