import matplotlib.pyplot as plt
from main import df

# Создание визуализаций matplotlib
graf1 = df[[x for x in df.columns if 'Sales' in x] +
                ['Year_of_Release']].groupby('Year_of_Release').sum().plot()


df[[x for x in df.columns if 'Sales' in x] +
   ['Year_of_Release']].groupby('Year_of_Release').sum().plot(kind='bar', rot=45)
plt.show()