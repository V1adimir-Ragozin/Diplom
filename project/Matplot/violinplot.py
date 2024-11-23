from main import df
import matplotlib.pyplot as plt

# Фильтрация данных для игр с известными оценками
filtered_df = df[(df['Critic_Score'].notna()) & (df['User_Score'].notna())]

# Создание графика «скрипками»
plt.figure(figsize=(12, 6))
plt.violinplot([filtered_df[filtered_df['Genre'] == genre]['Critic_Score'] for genre in filtered_df['Genre'].unique()], showmedians=True)
plt.title('График «скрипками» оценок критиков по жанрам')
plt.xlabel('Жанр')
plt.ylabel('Оценка')
plt.xticks(range(1, len(filtered_df['Genre'].unique()) + 1), filtered_df['Genre'].unique(), rotation=45)
plt.grid(True)
plt.show()