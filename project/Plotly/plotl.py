import plotly.express as px
import plotly.graph_objects as go
from main import df

# Группировка данных по годам и суммирование продаж, подсчет количества игр
years_df = df.groupby('Year_of_Release')[['Global_Sales']].sum().join(
    df.groupby('Year_of_Release')[['Name']].count())
years_df.columns = ['Global_Sales', 'Number_of_Games']


# Группировка данных по платформам и суммирование продаж, подсчет количества игр
platforms_df = df.groupby('Platform')[['Global_Sales']].sum().join(
    df.groupby('Platform')[['Name']].count()
)
platforms_df.columns = ['Global_Sales', 'Number_of_Games']

# Сортировка данных по суммарным продажам в порядке убывания
platforms_df.sort_values('Global_Sales', ascending=False, inplace=True)


# Создаем список для хранения данных для каждого жанра
data = []

# Проходим по каждому уникальному жанру
for genre in df.Genre.unique():
    # Добавляем box plot для каждого жанра
    data.append(
        go.Box(y=df[df.Genre == genre].Critic_Score, name=genre)
    )