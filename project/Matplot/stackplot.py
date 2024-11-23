from main import df
import matplotlib.pyplot as plt

# Группировка данных по годам и жанрам, суммирование продаж
yearly_genre_sales = df.groupby(['Year_of_Release', 'Genre'])['Global_Sales'].sum().unstack()

# Создание диаграммы площади Unstacked
plt.figure(figsize=(12, 8))
plt.stackplot(yearly_genre_sales.index, yearly_genre_sales.values.T, labels=yearly_genre_sales.columns)
plt.title('Соотношение продаж игр по жанрам на протяжении лет')
plt.xlabel('Год выпуска')
plt.ylabel('Общие продажи (в млн. копий)')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()