from pair_disp_joint import df, sns, plt


# Создаем catplot для отображения распределения продаж по жанрам и платформам
g = sns.catplot(data=df, x='Platform', y='Global_Sales', col='Genre', kind='box',
                col_wrap=3, height=4, aspect=1.5, sharey=False, palette='viridis')
g.set_axis_labels('Платформа', 'Глобальные продажи (млн)')
g.set_titles(col_template="{col_name}")
g.fig.suptitle('Распределение глобальных продаж по жанрам и платформам', y=1.02)

# Поворачиваем метки оси x для лучшей читаемости
for ax in g.axes.flat:
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()