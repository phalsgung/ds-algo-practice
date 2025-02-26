import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# SampleDf = pd.read_json(SampeleJsonDict,  orient='columns', dtype=None, columns=['ID', 'Country', 'CountryCode', 'Province', 'City', 'CityCode', 'Lat', 'Lon', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Date']);
SampleDf = pd.read_json('https://api.covid19api.com/live/country/united-states/status/confirmed');



# Province Having most Confirmed cases
print( SampleDf[SampleDf['Confirmed']==SampleDf['Confirmed'].max()] )

# Province Having least Confirmed cases
print( SampleDf[SampleDf['Confirmed']==SampleDf['Confirmed'].min()] ) 

# Average number of Active cases
print( SampleDf['Active'].mean() )



