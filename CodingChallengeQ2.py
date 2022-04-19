import pandas as pd
import matplotlib
BaseNursingHomeData = pd.read_pickle(r'\\wsl$\fedora\home\phil\Nursing Home Data 2021\NursingHomeData2021pkl\EnsignNursingHomeData2021Vacc.pkl',)

BaseNursingHomeData['Week Ending'] = pd.to_datetime(BaseNursingHomeData['Week Ending'])
    #Converted Week Ending column to datetime objects

Cases = BaseNursingHomeData[['Week Ending', 'Provider Name', 'Residents Weekly Confirmed COVID-19']]
Cases.drop_duplicates(inplace=True)
Cases.sort_values(['Provider Name', 'Week Ending'], ascending=[True, True], inplace=True)
Cases.rename(columns={'Residents Weekly Confirmed COVID-19':'C_Cases'}, inplace=True)
Cases['C_Cases_Shifted'] = Cases['C_Cases'].shift()
Cases['cumsum'] = Cases['C_Cases'] != Cases[C_Cases_Shifted]
Casesgrp = Cases.groupby(['Provider Name'])
Case_Cumsum_Grp = Casesgrp['Provider Name','cumsum'].apply(lambda x: x.cumsum())