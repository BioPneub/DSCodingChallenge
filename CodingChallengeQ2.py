import pandas as pd
import matplotlib
BaseNursingHomeData = pd.read_pickle(r'\\wsl$\fedora\home\phil\Coding Challenge\NursingHomeData2021pkl\EnsignNursingHomeData2021Vacc.pkl',)

BaseNursingHomeData['Week Ending'] = pd.to_datetime(BaseNursingHomeData['Week Ending'])
    #Converted Week Ending column to datetime objects. Thought this might be useful.

Cases = BaseNursingHomeData[['Week Ending', 'Provider Name', 'Residents Weekly Confirmed COVID-19']]
    #Filtering out the rows I don't need here since .read_pickle() does not allow me to filter them out on the read in.

Cases.drop_duplicates(inplace=True)
    #Lots of duplicate dates from the original file. Trimmed down since I'll only be needing 1 of each week for each facility.

Cases.sort_values(['Provider Name', 'Week Ending'], ascending=[True, True], inplace=True)
    #Some organizing so when I want to just skim the data really quickly

Cases.rename(columns={'Residents Weekly Confirmed COVID-19':'C_Cases'}, inplace=True)
    #Shortening of a column name...

Cases['C_Cases_Shifted'] = Cases['C_Cases'].shift()
    #Created C_Cases_Shifted based from the C_Cases column with the .shift() method which when compared returns a True/False value.
    #These True/False values would indicate on which week the value of the C_Cases column changed allowing me to identify streaks of
    #Covid infections with residents or the lack thereof.

Cases['cumsum'] = Cases['C_Cases'] != Cases[C_Cases_Shifted]
    #cumsum column would contain the True/False value provided from the comparison of the above columns

Casesgrp = Cases.groupby(['Provider Name'])
    #Grouping by facility for easier viewing

Case_Cumsum_Grp = Casesgrp['Provider Name','cumsum'].apply(lambda x: x.cumsum())
    #Applying the group to a variable and also using the lambda function to on the cumsum column, reitertaing for each group, for later recall. These last 4 lines were the most difficult. Really required a lot of googling youtube and
    #thinking in different ways to try and approach the problem.



---------------------------

# import pandas as pd
#
# def datareadin(filepath):
#     global basenursinghomedata, cases
#
#     basenursinghomedata = pd.read_pickle(filepath)
#     basenursinghomedata['Week Ending'] = pd.to_datetime(basenursinghomedata['Week Ending'])
#     cases = basenursinghomedata[['Week Ending', 'Provider Name', 'Residents Weekly Confirmed COVID-19']]
#     cases.drop_duplicates(inplace=True)
#     cases.sort_values(['Provider Name', 'Week Ending'], ascending=[True, True], inplace=True)
#     cases.rename(columns={'Residents Weekly Confirmed COVID-19': 'C_Cases'}, inplace=True)

#     return cases
#
# def streaks(facilitydata):
#     global case_cumsum_crp
#
#     cases['C_Cases_Shifted'] = cases['C_Cases'].shift()
#     cases['cumsum'] = cases['C_Cases'] != cases['C_Cases_Shifted']
#     casesgrp = cases.groupby(['Provider Name'])
#     case_cumsum_crp = casesgrp['Provider Name', 'cumsum'].apply(lambda x: x.cumsum())

#     return case_cumsum_crp
#
#
# testdata = (r'\\wsl$\fedora\home\phil\Coding Challenge\NursingHomeData2021pkl\EnsignNursingHomeData2021Vacc.pkl')






