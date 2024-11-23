import matplotlib.pyplot as plt
from main import df

# Создание визуализаций matplotlib
graf1 = df[[x for x in df.columns if 'Sales' in x] +
                ['Year_of_Release']].groupby('Year_of_Release').sum().plot()


df[[x for x in df.columns if 'Sales' in x] +
   ['Year_of_Release']].groupby('Year_of_Release').sum().plot(kind='bar', rot=45)

# Группировка данных по годам и суммирование продаж
yearly_sales = df.groupby('Year_of_Release')['Global_Sales'].sum()

# Определение пиков и впадин
peaks = yearly_sales[yearly_sales > yearly_sales.quantile(0.75)]
valleys = yearly_sales[yearly_sales < yearly_sales.quantile(0.25)]

# Создание временного ряда с пиками и впадинами
plt.figure(figsize=(12, 6))
plt.plot(yearly_sales.index, yearly_sales.values, label='Продажи по годам')
plt.scatter(peaks.index, peaks.values, color='red', label='Пики')
plt.scatter(valleys.index, valleys.values, color='green', label='Впадины')
plt.title('Динамика продаж игр по годам с выделением пиков и впадин')
plt.xlabel('Год выпуска')
plt.ylabel('Общие продажи (в млн. копий)')
plt.legend()
plt.grid(True)
plt.show()