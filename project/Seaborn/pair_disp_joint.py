import seaborn as sns
import matplotlib.pyplot as plt
from main import df


# Создание визуализаций seaborn
sns.pairplot(df[['Global_Sales', 'Critic_Score', 'Critic_Count',
                 'User_Score', 'User_Count']])

sns.displot(df.Critic_Score)
sns.jointplot(x='Critic_Score', y='User_Score',
              data=df, kind='scatter')
plt.show()