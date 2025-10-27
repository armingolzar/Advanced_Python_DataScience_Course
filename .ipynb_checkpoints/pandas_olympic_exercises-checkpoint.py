import pandas as pd
import matplotlib.pyplot as plt


# Practis 1: Load the two files, `olympics_events.csv` and `olympics_games.csv`, and display the first 10 lines of each data frame.


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')

# print(olympic_dataset.head(10))

# print('\n')

# print('############################################################################################################')

# print('\n')

# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# print(olympic_games_dataset.head(10))

# End of the practice 1



# Practice 2: Merge the two data frames on the `GamesID` and `ID` columns. Join = **outer**. Drop the now-unnecessary id-columns afterwards.


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# print(complete_olympic_dataset)

# End of the practice 2



# Practice 3: History lesson! Malaysia's olympic nationality code is `MAS`. Prior to this, the Federation of Malaya competed under the code `MAL`. Likewise, Sarawak and Sabah competed as North Borneo (`NBO`). 
# 1. In which years did the Federation of Malaya compete in the Olympics?


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)


# unique_years_of_participating_of_malaya_dataset = len(complete_olympic_dataset.loc[complete_olympic_dataset['Nationality'] == 'MAL', 'Year'].unique())
# print(unique_years_of_participating_of_malaya_dataset)

# ####### Attention: also remmember nunique() method for getting the unique number of a thing in dataframe not series
# see below for that 

# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)


# unique_years_of_participating_of_malaya_dataset = complete_olympic_dataset.loc[complete_olympic_dataset['Nationality'] == 'MAL', ['Nationality','Year']].nunique()
# print(unique_years_of_participating_of_malaya_dataset)

# ####### Attention: the code for doing nunique method and after that seeing the uniqe values of the resulat is Below:

# df = pd.DataFrame({
#     'color': ['red', 'blue', 'red', 'green'],
#     'size': ['S', 'M', 'L', 'S'],
#     'price': [10, 20, 10, 30]
# })

# # Step 1: See number of unique values
# nunique_series = df.nunique()
# print("Number of unique values per column:")
# print(nunique_series)
# print(type(nunique_series))

# # Step 2: See actual unique values per column
# print("\nUnique values per column:")
# for col in df.columns:
#     # print(col)
#     print(f"{col}: {df[col].unique()}")

# End of the practice 3


# Practice 4: How many athletes did they send?


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# athletes =  complete_olympic_dataset.loc[complete_olympic_dataset['Nationality'] == 'MAL', 'Name'].unique()
# print(len(athletes))


# End of the practice 4


# Practice 5: Who were the first countries to participate in the Olympic games (as per this data set)?


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# FIRST_YEAR_OF_OLYMPIC = complete_olympic_dataset['Year'].min()
# print(FIRST_YEAR_OF_OLYMPIC)

# countiries_of_first_year = complete_olympic_dataset.loc[complete_olympic_dataset['Year'] == FIRST_YEAR_OF_OLYMPIC, 'Nationality'].unique()
# print(countiries_of_first_year)


# End of the practice 5



# Practice 6: How many men and women has Malaysia (`MAS`) sent to the Olympics in total? Keep in mind that athletes can participate in multiple events and multiple years. Each person should only ever be counted once.


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# malaysia_olympic_dataset = complete_olympic_dataset.loc[complete_olympic_dataset['Nationality'] == 'MAS', ['Name', 'Sex']]
# malaysia_olympic_dataset_unique = malaysia_olympic_dataset[~ malaysia_olympic_dataset.duplicated()]
# # print(malaysia_olympic_dataset_unique)
# print(malaysia_olympic_dataset_unique.groupby('Sex').size())


# End of the practice 6


# Practice 7: How many men and women has Malaysia (`MAS`) sent to the Olympics each year?


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)
# # print(complete_olympic_dataset)
# selected_olympic_dataset = complete_olympic_dataset.loc[complete_olympic_dataset['Nationality'] == 'MAS', ['Name', 'Sex', 'Event', 'Year']]

# selected_filter = selected_olympic_dataset.loc[:, ['Name', 'Year']]
# filtered_bool_lst = ~ selected_filter.duplicated()
# print(len(filtered_bool_lst))
# print(selected_olympic_dataset.shape)

# selected_olympic_dataset_filterd = selected_olympic_dataset[filtered_bool_lst]

# print(selected_olympic_dataset_filterd.groupby(['Year', 'Sex']).size())


# End of the practice 7


# practice 8: How many gold medals has each country won? How about Malaysia (`MAS`)?


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# gold_medal_olympic_dataset = complete_olympic_dataset.loc[complete_olympic_dataset['Medal'] == 'Gold', ['Nationality']]

# print(gold_medal_olympic_dataset.groupby('Nationality').size())

# gold_medal_olympic_dataset_groupbied = gold_medal_olympic_dataset.groupby('Nationality').size()
# # print(type(gold_medal_olympic_dataset_groupbied))
# print(gold_medal_olympic_dataset_groupbied['MAS'])

# End of the practice 8


# Practice 9: What is the median age of gold medalists?


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# ages_of_gold_medalists = complete_olympic_dataset.loc[complete_olympic_dataset['Medal'] == 'Gold', 'Age']
# print(ages_of_gold_medalists)
# print(ages_of_gold_medalists.median())

# End of the practice 9


# Practice 10: Look at only swimmers. How has the mean weight of all competitors changed throughout the years? Use `*.plot()` to get a visual sense of the trend.

olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

complete_olympic_dataset.drop(columns='ID', inplace=True)

swimmers = complete_olympic_dataset.loc[complete_olympic_dataset['Sport'] == 'Swimming', ['Weight', 'Year']]

swimmers_weight_groupbied = swimmers.groupby('Year').mean()
print(type(swimmers_weight_groupbied))

weight_means_groupbied = []
for x in swimmers_weight_groupbied['Weight']:
    if pd.isna(x) == True:
        weight_means_groupbied.append(0)
    else:
        weight_means_groupbied.append(x)

print(weight_means_groupbied)
print(len(weight_means_groupbied))
years_indexes = swimmers_weight_groupbied.index.to_list()
print(years_indexes)

plt.plot(years_indexes, weight_means_groupbied, color = 'green', label = 'KG', linewidth=2)
plt.xlabel('Years')
plt.ylabel('Weights')
plt.title('Change in weights of swimmers during years')
plt.legend()
plt.grid(True)
plt.show()

# End of the practice 10


# Practice 11: What is the mean and standard deviation of the BMI of athletes in each sports discipline? The BMI can be computed as

# BMI = weight/((height/100)**2)

# with the values in this dataset. To solve this question, break it down into individual steps:
# - Calculate the BMI for all athletes
# - Group by 'Sport'
# - Calculate the mean and standard deviation of the BMI of the grouped data frame
    
# *Hint*: Use `*.agg([..., ...])` to apply "mean" and "std" (standard deviation) simultaneously.


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# height_filtered_athletes_dataset = complete_olympic_dataset.loc[pd.isna(complete_olympic_dataset['Height']) == False, :]
# weight_height_filtered_athletes_dataset = height_filtered_athletes_dataset.loc[pd.isna(height_filtered_athletes_dataset['Weight']) == False, :]

# # print(weight_height_filtered_athletes_dataset)

# lst_heights = weight_height_filtered_athletes_dataset['Height']
# lst_weights = weight_height_filtered_athletes_dataset['Weight']

# lst_bmi = lst_weights/ ((lst_heights/100)**2)

# weight_height_filtered_athletes_dataset['BMI'] = lst_bmi

# print(weight_height_filtered_athletes_dataset.groupby('Sport')['BMI'].agg(['mean', 'std']))


# End of the practice 11



# Practice 12: What country has the most gold medals in wrestling?


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# # print(complete_olympic_dataset['Sport'].unique())

# wrestling_gold_medal_dataset = complete_olympic_dataset.loc[(complete_olympic_dataset['Sport'] == 'Wrestling') & (complete_olympic_dataset['Medal'] == 'Gold'), :]
# print(wrestling_gold_medal_dataset.groupby('Nationality').size().sort_values(ascending=False))


# End of the practice 12


# Practice 13: How many different types of events have ever been held for fencing?


# olympic_dataset = pd.read_csv(r'../practice_files/olympics_events.csv')
# olympic_games_dataset = pd.read_csv(r'../practice_files/olympics_games.csv')

# complete_olympic_dataset = pd.merge(olympic_dataset, olympic_games_dataset, left_on='GamesID', right_on='ID', how='outer')

# complete_olympic_dataset.drop(columns='ID', inplace=True)

# print(complete_olympic_dataset)

# # print(complete_olympic_dataset['Sport'].unique())

# fencing_events = complete_olympic_dataset.loc[complete_olympic_dataset['Sport'] == 'Fencing', 'Event'].unique()
# print(fencing_events)
# print(len(fencing_events))

# End of the practice 13


# Attention: we can find all of the champions of the Table Tennis Men's Singles in olympic by code below:

# print(complete_olympic_dataset)

# print(complete_olympic_dataset.loc[complete_olympic_dataset['Sport'] == 'Table Tennis', 'Event'].unique())

# winner_2012 = complete_olympic_dataset.loc[(complete_olympic_dataset['Sport'] == 'Table Tennis') & (complete_olympic_dataset['Event'] == "Table Tennis Men's Singles") & (complete_olympic_dataset["Medal"] == "Gold"), ['Name', 'Nationality', 'Year']]

# print(winner_2012)


# Great job you've done data exploratory course compeletely.
