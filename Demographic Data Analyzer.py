#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    
  df = pd.read_csv('adult.data.csv')
  total_people = len(df)

  def percentage(n):
    return len(n)*100/total_people
    
  gps = df.groupby('race')
  races = ['Amer-Indian-Eskimo','Asian-Pac-Islander','Black', 'Other','White']
  res = pd.Series([gps.get_group(races[x])['age'].count() for x in range(len(races))], index=races)
  race_count = res.sort_values(ascending=False)

    # What is the average age of men?

  male = df['sex'] == 'Male'
  age_male = df['age'][male].aggregate(np.mean)
  average_age_men = round(age_male,1)


    # What is the percentage of people who have a Bachelor's degree?
  
  bchlr = df[df['education'] == 'Bachelors']
  percentage_bachelors = round(percentage(bchlr),1)



    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
  res = df[((df['education'] == 'Bachelors') | (df['education'] == 'Masters')       | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')]

  higher_education = len(df[((df['education'] == 'Bachelors') | 
                        (df['education'] == 'Masters') |
                        (df['education'] == 'Doctorate'))])
  lower_education = len(df[(df['education'] != 'Bachelors') & 
                       (df['education'] != 'Masters') &
                       (df['education'] != 'Doctorate')])

    # percentage with salary >50K
  higher_education_rich = round(len(res)*100/higher_education,1)


  res = df[((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')]
  lower_education_rich = round(len(res)*100/lower_education,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df['hours-per-week'].aggregate(np.min)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = len(df[df['hours-per-week'] == min_work_hours])

  res = df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')]
  rich_percentage = round(len(res)*100/num_min_workers,1)

    # What country has the highest percentage of people that earn >50K?


  gp_country = df.groupby('native-country')  
  a = 0
  b = ''
  for i, j in gp_country:
    grp = gp_country.get_group(i)
    res = grp[grp['salary'] == '>50K']
    if len(res)*100/len(grp) > a:
        a = len(res)*100/len(grp)
        b = i
    
  highest_earning_country = b
  highest_earning_country_percentage = round(a,1)


    # Identify the most popular occupation for those who earn >50K in India.

  res = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
  res_group = res.groupby('occupation')
  a = 0
  b = ''
  for key, values in res_group:
    if len(res_group.get_group(key)) > a:
        a = len(res_group.get_group(key))
        b = key
  top_IN_occupation = b

    # DO NOT MODIFY BELOW THIS LINE

  if print_data:
      print("Number of each race:\n", race_count) 
      print("Average age of men:", average_age_men)
      print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
      print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
      print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
      print(f"Min work time: {min_work_hours} hours/week")
      print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
      print("Country with highest percentage of rich:", highest_earning_country)
      print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
      print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage':
      highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }

