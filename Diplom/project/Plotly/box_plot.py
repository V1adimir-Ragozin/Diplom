from plotl import go, data

# Создаем фигуру с box plot
fig = go.Figure(data=data)

# Настройка внешнего вида графика
fig.update_layout(
    title='Distribution of Critic Scores by Genre',
    yaxis=dict(title='Critic Score'),
    xaxis=dict(title='Genre'),
    boxmode='group',  # Группировка box plot по жанрам
    plot_bgcolor='white',  # Цвет фона графика
    paper_bgcolor='white',  # Цвет фона области вокруг графика
    margin=dict(l=50, r=50, t=80, b=50)  # Отступы вокруг графика
)

# Настройка box plot
fig.update_traces(
    marker_line_color='rgb(8,48,107)',  # Цвет границ box plot
    marker_line_width=1.5,  # Толщина границ box plot
    opacity=0.8  # Прозрачность box plot
)

# Отображение графика
fig.show()