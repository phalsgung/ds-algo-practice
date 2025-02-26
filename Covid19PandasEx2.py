import pandas as pd
import COVID19Py

covid19 = COVID19Py.COVID19(data_source = "csbs")

# print(dir(covid19))

# LatestInfo = covid19.getAll()
# print(LatestInfo)

USlocationData = covid19.getLocationByCountryCode("US")

country_code = []
province = []
latest_confirmed = []

for item in USlocationData:
	country_code.append(item['country_code'])
	province.append(item['province'])
	latest_confirmed.append(item['latest']['confirmed'])

FormattedDictforDF = {"Country code": country_code, "State": province, "Total Number of Cases": latest_confirmed}

USlocationDF = pd.DataFrame(FormattedDictforDF)

# df.loc[df['column_name'] == some_value]
# print(USlocationDF.loc[ USlocationDF['State'] == 'Northern Mariana Islands' ])

# print(USlocationDF['State'] = 'Northern Mariana Islands')

print(USlocationDF.groupby('State').sum('Total Number of Cases'))

# print(USlocationDF)





