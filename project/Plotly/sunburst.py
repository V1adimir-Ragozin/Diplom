import plotly.express as px
from main import df, useful_cols

df_useful = df[useful_cols]

fig4 = px.sunburst(df_useful, path=['Genre', 'Platform'], values='Global_Sales', title='Иерархия жанров и платформ по продажам')
fig4.show()

fig5 = px.scatter_3d(df_useful, x='Global_Sales', y='Critic_Score', z='Year_of_Release', color='Genre',
                     title='Взаимосвязь между продажами, оценками критиков и годом выпуска')
fig5.show()