# ExploringWorldHappiness
This repository holds the files used for the data transformation required for the visualizations made in Tableau: 
https://public.tableau.com/app/profile/daniel5014/viz/ExploringWorldHappiness/WorldHappiness

The data_transformation.py file reads the original data from the .csv files, imputes missing values and performs multiple t-tests between various regions and for each factor of relevance involving the happiness level of a country. It then stores the original data, as well as the t-scores and p-values from the t-tests in the .xlsx file to be used in creating the visualizations that can be found through the Tableau link above.
