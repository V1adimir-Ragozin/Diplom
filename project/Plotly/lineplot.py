from plotl import years_df, px

# Создание line plot с использованием Plotly
fig = px.line(years_df.reset_index(), x='Year_of_Release', y=['Global_Sales', 'Number_of_Games'],
              title='Global Sales and Number of Games Released Over the Years',
              labels={'value': 'Sales/Number', 'variable': 'Metric'})

# Отображение графика
fig.show()