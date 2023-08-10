import pandas as pd
import numpy as np
import scipy.stats as stats


# read and store the raw data from each year
data_2015 = pd.read_csv("2015.csv")
data_2016 = pd.read_csv("2016.csv")
data_2017 = pd.read_csv("2017.csv")
data_2018 = pd.read_csv("2018.csv")
data_2019 = pd.read_csv("2019.csv")

# create a dictionary which maps each country to its corresponding region
country_region_dict = dict(zip(data_2015.Country, data_2015.Region))
country_region_dict['Belize'] = data_2016['Region'].loc[data_2016['Country'] == 'Belize'].values[0]
country_region_dict['Somalia'] = data_2016['Region'].loc[data_2016['Country'] == 'Somalia'].values[0]
country_region_dict['Namibia'] = data_2016['Region'].loc[data_2016['Country'] == 'Namibia'].values[0]
country_region_dict['South Sudan'] = data_2016['Region'].loc[data_2016['Country'] == 'South Sudan'].values[0]
country_region_dict['Gambia'] = 'Sub-Saharan Africa'

# use the dictionary created above to impute the missing values for the region column in 2017, 2018 and 2019
data_2017['Region'] = data_2017['Country'].map(country_region_dict)
data_2018['Region'] = data_2018['Country'].map(country_region_dict)
data_2019['Region'] = data_2019['Country'].map(country_region_dict)

# define a list of relevant factors to perform the t-tests on, sourced from the columns of the raw data 
columns = list(data_2015.columns)
factors = [column for column in columns if column not in ('Country', 'Region', 'Happiness Rank')]

# set the data used for x1 of the t-test to be from Western Europe and define a list of all other regions to be the data used for x2
x1_data = data_2015.loc[data_2015['Region'] == 'Western Europe']
regions = data_2015['Region'].unique()
regions = np.delete(regions, np.where(regions == 'Western Europe'))

# create empty lists to store the t-scores and p-values of the t-tests
t_scores = dict(zip(regions, ([] for _ in regions)))
p_values = dict(zip(regions, ([] for _ in regions)))

# for each region (excluding Western Europe), calculate and store the t-score and p-value for each factor
for region in regions:
    x2_data = data_2015.loc[data_2015['Region'] == region]
    for factor in factors:
        results = stats.ttest_ind(x1_data[factor], x2_data[factor], equal_var=False)
        t = results[0]
        t_scores[region].append(t)
        p = results[1]
        p_values[region].append(p)

# store the results into separate dataframes, sorted by the lowest to highest of the absolute value of the t-score
t_scores_df = pd.DataFrame(t_scores, index=factors).transpose()
t_scores_df = t_scores_df.reindex(t_scores_df['Happiness Score'].abs().sort_values().index)
p_values_df = pd.DataFrame(p_values, index=factors).transpose()
p_values_df = p_values_df.reindex(t_scores_df['Happiness Score'].abs().sort_values().index)

# write the data of each year and the calculated results of the t-tests into an excel workbook
with pd.ExcelWriter('World Happiness Data.xlsx') as writer:
    data_2015.to_excel(writer, sheet_name='2015', index=False)
    data_2016.to_excel(writer, sheet_name='2016', index=False)
    data_2017.to_excel(writer, sheet_name='2017', index=False)
    data_2018.to_excel(writer, sheet_name='2018', index=False)
    data_2019.to_excel(writer, sheet_name='2019', index=False)
    t_scores_df.to_excel(writer, sheet_name='t_scores', index=True)
    p_values_df.to_excel(writer, sheet_name='p_values', index=True)
