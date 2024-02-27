Name = Deniz Aycan

GitHub name = aycande


This project aims to explore historical and current status of countries’ efforts in combatting climate change and it benefits from the contextual concepts and perspective of international development. International climate cooperation is at the heart of our ability to reduce carbon emissions and adapt to new climate conditions, and this project looks at the colonial linkages in climate cooperation. 

The initial research questions that started the project were:

1-	How is international climate finance distributed, historically, regionally and based on goals?

2-	How does United Kingdom’s efforts to provide effective financial support and aid for climate match with country’s goals and claims towards climate adaptation in development context?

Climate finance is a growing part of diplomacy and foreign aid for rich countries. While the debate of ‘historical responsibility’ goes on, it is vital to understand how international climate finance distributed overall in the developing world. Multilateral and bilateral relations with colonial historical origins continue to this day through institutions such as Commonwealth. Climate adaptation as a result of these efforts are to be tracked, which should be also considered together with the Nationally Determined Contributions Framework established at  Conference of Parties in Paris. 

To answer these questions, I have found and used 8 datasets and compiled 1 dataset from pdf parsing and text analysis. These datasets and how they are incorporated into the research can be found below:


| Number | Format | Name                      | Usage                              | Scale              |
|--------|--------|---------------------------|------------------------------------|--------------------|
| 1      | Excel  | ODI_Projects              | Word Cloud                         | Global             |
| 2      | Excel  | ODI_Pledges               | Static Plot                        | Global             |
| 3      | Excel  | UK_ICF                    | Word Cloud                         | UK                 |
| 4      | CSV    | Emissions                 | Interactive/Static Plots, Analysis | Global             |
| 5      | CSV    | Colonial_Emissions        | Interactive/Static Plots, Analysis | Global             |
| 6      | CSV    | Colonial Emissions for Plot| Static Plot                        | Global             |
| 7      | API    | OECD                      | Interactive/Static Plots, Analysis | Selected Commonwealth|
| 8      | API    | WB                        | Interactive/Static Plots, Analysis | Global             |
| 9      | PDF    | Commonwealth Access Hub    | Word Cloud                         | Commonwealth       |

Py file descriptions

I divided my coding into 5 different py files each with different objectives:

| Name                    | Description of the Task |
|-------------------------|-------------------------|
| data_wrangling.py       | As the first part of the project, I have written a py file to open, load, and prepare the datasets for the next steps.                                               | 
| plotting.py             | I used the cleaned and prepared datasets from data_wrangling.py and plotted interactive and static plots to download and present through Shiny interface I've built. | 
| text_processing.py      | I've parsed a pdf file from Commonwealth Access Hub to use later for creating word clouds and finding insights on the discourse revolving around climate finance.    | 
| analysis.py             | Here I investigate the linkages between prosperity, adaptation, historical responsibilities, and status quo of countries as emitters with basic panel data regression.|
| app.py                  | Lastly, I have built a Shiny web platform to publish my interactive plots with users.                                                                                 |

Data Availability in Climate Finance & Word Clouds

As my initial goal was to explore linkages of climate finance, post-colonial relations and climate cooperation, I initiated my work from using Overseas Development Institute’s Climate Finance data and my goal was to merge it with Emissions and Colonial Emissions datas. This did not work out as most of the funds are collected and distrubuted multilaterally by nature. Therefore, it is impossible to calculate the actual amount of fund given by Country A and received by Country B. Most of the time, funds are collected through an agency (which in most cases is Green Climate Fund of UNFCCC). Hence, I was only able to use the first dataset to produce wordclouds and track the change of focus of the projects in each year. This gave me an idea of how climate finance discourse and focus has evolved in global scale. Then, I wanted to explore the same question for Commonwealth countries and for funds that are specifically funded by UK. So, I have used my UK_ICF and Commonwealth Access Hub datasets for the same goal, and you can find sample wordclouds of different years in ‘Images’ tab. 

Static Plots

The second dataset, on the other hand, is helpful to see United Kingdom’s role in international climate cooperation and international climate finance, as this dataset allows us to track the pledges countries made within each multilateral fund. I calculated the percentage rate of UK’s pledges in this data and created plots by plotting against cumulative (first) and per capita (second) colonial emissions countries have created. Here, another dataset I used for these plots is the Colonial_Emissions_for_plot, which has the cumulative data for each country, as opposed to panel data in Colonial_Emissions. Colonial emissions per country, per capita and per year are calculated as a result of an investigation made by CarbonBrief, which can be found in this link. I admire their work a lot and am happy to take the next step and utilize the data they carefully compiled. My second plot is insightful to understand the historical responsibilities of developed countries and where they stand today. Note that this is the log version of the plot, which is done for readability.

<img width="700" alt="image" src="https://github.com/datasci-harris/final-project-deniz/assets/91655573/a331d5af-0c46-4f9c-aaf8-5dac460d5587">

Interactive Plots in Shiny & Analysis

After investigating climate finance datasets with word clouds and static maps, I moved onto compiling my panel dataset including emissions data by Climate Watch, climate adaptation data by OECD, colonial emissions data by Carbon Brief, and GDP per capita data by World Bank. This part of the project further investigates the linkages between prosperity, climate adaptation, historical responsibilities and current statusquo of countries as emitters. Unfortunately, the country list of the OECD dataset is extremely limited, however, for the countries available, it suggests great insights. Therefore, my first inteactive plot in Shiny is exploring country’s progress in different climate goals over time:

<img width="700" alt="image" src="https://github.com/datasci-harris/final-project-deniz/assets/91655573/05e4fb8c-8d99-4fc2-81a9-9c734be62ad6">

For the second interactive plot in Shiny and my analysis, I have compiled my final dataset, panel3. This is a cross-country and longitudinal dataset, filtered for commonwealth countries. My second shiny plot allows users great flexibility in choosing time and over 20 indicators, including emissions, colonial emissions, gdp per capita and climate adaptation scores provided by OECD. An example can be found below:

<img width="700" alt="image" src="https://github.com/datasci-harris/final-project-deniz/assets/91655573/eca3913e-54ab-4566-890e-bfa3aa60659d">

Another example with OECD scores:

<img width="700" alt="image" src="https://github.com/datasci-harris/final-project-deniz/assets/91655573/b97efd75-3803-4180-86b6-454f69ae6010">

Finally, my panel dataset was helpful to be used in the analysis section, which could be further developed. Due to time limitation and scope of this class, these results should be interpreted by caution. However, the current model estimations have some significance in p values:

•	The first panel (on the right) suggests that GDP per capita is positively associated with state's colonial emissions, independency and the international cooperation score.

<img width="700" alt="image" src="https://github.com/datasci-harris/final-project-deniz/assets/91655573/89d21a24-7e73-4061-aeaf-988e2cac55b8">

•	The second panel (on the left) suggests that emissions are positively associated by independency of the state.

<img width="700" alt="image" src="https://github.com/datasci-harris/final-project-deniz/assets/91655573/7656dbb2-a6e7-4551-b155-a1a097218b48">


Overall, this project was interesting to work on and practice the skills we learned this quarter. The limitation of data in time and country variables, especially in climate finance data, narrowed the analysis and required additional datasets to be added to the project. However, it provides insightful results about the Commonwealth countries’ historical linkages and climate cooperation and adaptation results.

Important NOTE = To be able to have a clean final repo, I have mainly worked in my repo https://github.com/aycande/python_final_drafts in the previous days. Therefore, to see past commits and understand the steps I have gone through, please check that repo. I have first gone through steps of the project in py file draft2.py. Then, I have created seperate files for each part as it is asked. 
