# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#analyzing age distribution
census = np.concatenate([data,new_record])
print(census.shape)

age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


#identifying minority race
race_0 = []
race_1 = []
race_2 = []
race_3 = []
race_4 = []
for i in census[:,2]:
    if i == 0:
        race_0.append(i)
    if i ==1 :
        race_1.append(i)
    if i ==2:
        race_2.append(i)
    if i == 3:
        race_3.append(i)
    if i == 4:
        race_4.append(i)
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
len_race = [len_0,len_1,len_2,len_3,len_4]

minority_race = len_race.index(np.min(len_race))
print(minority_race)
#subsetting and analyzing senior citizen's working hours
senior_citizens = census[census[:,0]>60]

working_hours_sum = np.sum(senior_citizens[:,6])

senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

#anlyzing pay according to their education
high = census[census[:,1]>10]
low = census[census[:,1]<=10]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

print(avg_pay_high)
print(avg_pay_low)












