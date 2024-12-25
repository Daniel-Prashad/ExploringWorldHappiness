# ExploringWorldHappiness

## Introduction
Although happiness is one of the few basic human emotions, the pursuit of true happiness can be quite complex and mysterious. A quick solution in the pursuit of happiness that has become commonplace today are cheap dopamine rushes throughout our day. However, this does not last; there must be more to true happiness. Perhaps, if we zoom outwards from the individual and consider countries as an entirety, we could gain some insight on what factors can lead to happiness. This project uses a Tableau story to demonstrate how factors such as economic production, social support, freedom, life expectancy, generosity and absence of government corruption contribute to the average happiness within a nation. With the insights gained from this analysis, we could then replicate the "formula" for happiness on a smaller scale and apply it to our own lives where possible.

## Find The Tableau Story Here:
https://public.tableau.com/app/profile/daniel5014/viz/ExploringWorldHappiness/WorldHappiness

## Additional Note
The data_transformation.py file reads the original data from the .csv files, imputes missing values and performs multiple t-tests between various regions and for each factor of relevance involving the happiness level of a country. It then stores the original data, as well as the t-scores and p-values from the t-tests in the .xlsx file to be used in creating the visualizations that can be found through the Tableau link above.
