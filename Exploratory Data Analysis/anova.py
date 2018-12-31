import pandas as pd 
import scipy.stats as stats

df = pd.read_excel('automobile.xlsx')
df_anova = df[['make','price']]
grouped_anova = df_anova.groupby('make')
print(grouped_anova.groups)

anova_results_l=stats.f_oneway(grouped_anova.get_group('honda')['price'],grouped_anova.get_group('subaru')['price'])
print(anova_results_l)

print()

anova_results_l=stats.f_oneway(grouped_anova.get_group('honda')['price'],grouped_anova.get_group('jaguar')['price'])
print(anova_results_l)