import os
import pandas as pd

# Получаем абсолютный путь к файлу
file_path = os.path.join(os.path.dirname(__file__), 'Video_Games_Sales_as_at_22_Dec_2016.csv')

# Загрузка данных из CSV файла и их обработка
df = pd.read_csv(file_path).dropna()

df['User_Score'] = df.User_Score.astype('float64')
df['Year_of_Release'] = df.Year_of_Release.astype('int64')
df['User_Count'] = df.User_Count.astype('int64')
df['Critic_Count'] = df.Critic_Count.astype('int64')

useful_cols = ['Name', 'Platform', 'Year_of_Release', 'Genre',
               'Global_Sales', 'Critic_Score', 'Critic_Count',
               'User_Score', 'User_Count', 'Rating'
              ]




