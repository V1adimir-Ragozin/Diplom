from pair_disp_joint import df, sns, plt

# Ящик
top_platforms = df.Platform.value_counts().sort_values(ascending = False).head(5).index.values
sns.boxplot(y="Platform", x="Critic_Score",
            data=df[df.Platform.isin(top_platforms)], orient="h")

plt.show()