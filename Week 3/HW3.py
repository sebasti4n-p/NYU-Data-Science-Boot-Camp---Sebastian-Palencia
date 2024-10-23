import pandas as pd
import matplotlib.pyplot as plt

#### QUESTION 1
# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['day_name'] = df['hour_beginning'].dt.day_name()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
df_weekdays = df[df['day_name'].isin(weekdays)]     #got from ChatGPT
daily_counts = df_weekdays.groupby('day_name')['Pedestrians'].sum()
daily_counts = daily_counts.reindex(weekdays)

# plt.figure(figsize=(12,6))
# daily_counts.plot(kind='line', marker='o',color='red')
# plt.title('Total Pedestrian Count per Weekday')
# plt.xlabel('Day of the Week')
# plt.ylabel('Pedestrian Count')
# plt.grid(True)
# plt.tight_layout()
# plt.show()
#
#
#
#### QUESTION 2
# df['year'] = df['hour_beginning'].dt.year
# df_2019 = df[df['year'] == 2019]
# pedestrian_weather = df_2019.groupby('weather_summary')['Pedestrians'].sum().reset_index()
# pedestrian_weather.columns = ['weather_summary', 'total_pedestrians']
# df_encoded = pd.get_dummies(pedestrian_weather, columns=['weather_summary'], drop_first=True) #got this from ChatGPT
# correlation_matrix = df_encoded.corr()
# print(correlation_matrix)
#
#
#
#### QUESTION 3
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['hour'] = df['hour_beginning'].dt.hour

# Defining function that cateforizes time of the day
def categorize_day(hour):
    morning = [5, 6, 7, 8, 9, 10, 11]
    afternoon = [12, 13, 14, 15, 16]
    evening = [17, 18, 19, 20]
    night = [21, 22, 23, 24, 0, 1, 2, 3, 4]
    if hour in morning:
        return 'Morning'
    elif hour in afternoon:
        return 'Afternoon'
    elif hour in evening:
        return 'Evening'
    elif hour in night:
        return 'Night'

# Call the function for every row in 'hour' column and place return value in new column 'time_of_day'   
df['time_of_day'] = df['hour'].apply(categorize_day)

# Counts pedestrians for each time of the day
time_of_day_count = df.groupby('time_of_day')['Pedestrians'].sum()
# Sort it
time_of_day_count = time_of_day_count.reindex(['Morning', 'Afternoon', 'Evening', 'Night'])

# Analyzing pedestrian activity
plt.figure(figsize=(12,6))
time_of_day_count.plot(kind='line', marker='o', color= 'purple')
plt.title('Pedestrians Throughout the Day')
plt.xlabel('Time of Day')
plt.ylabel('Pedestrian Count')
plt.tight_layout()
plt.show()

