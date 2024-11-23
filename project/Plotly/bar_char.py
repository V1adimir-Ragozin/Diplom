from plotl import platforms_df, px

# Создание bar chart с использованием Plotly
fig = px.bar(platforms_df.reset_index(), x='Platform', y=['Global_Sales', 'Number_of_Games'],
             title='Global Sales and Number of Games by Platform',
             labels={'value': 'Sales/Number', 'variable': 'Metric'},
             barmode='group',
             color_discrete_sequence=["#1f77b4", "#ff7f0e"])  # Установка цветов столбцов

# Настройка внешнего вида графика
fig.update_layout(
    title_font_size=24,  # Размер шрифта заголовка
    title_font_color="black",  # Цвет шрифта заголовка
    xaxis_title_font_size=18,  # Размер шрифта заголовка оси X
    yaxis_title_font_size=18,  # Размер шрифта заголовка оси Y
    xaxis_tickfont_size=14,  # Размер шрифта меток оси X
    yaxis_tickfont_size=14,  # Размер шрифта меток оси Y
    legend_title_font_size=16,  # Размер шрифта заголовка легенды
    legend_font_size=14,  # Размер шрифта текста легенды
    plot_bgcolor='white',  # Цвет фона графика
    paper_bgcolor='white',  # Цвет фона области вокруг графика
    margin=dict(l=50, r=50, t=80, b=50)  # Отступы вокруг графика
)

# Настройка столбцов
fig.update_traces(
    marker_line_color='rgb(8,48,107)',  # Цвет границ столбцов
    marker_line_width=1.5,  # Толщина границ столбцов
    opacity=0.8  # Прозрачность столбцов
)

# Отображение графика
fig.show()
