# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record = np.array(new_record)

#Code starts here
data = np.genfromtxt(path, delimiter = ",", skip_header = 1)
census = np.concatenate((data,new_record), axis = 0)


# --------------
#Code starts here
import numpy as np
age = census[:,0]
max_age = max(age)
min_age = min(age)
age_mean = sum(age)/len(age)
age_std = np.std(np.array(age))
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


# --------------
#Code starts here
race_0 = census[census[:,2]==0,:]
race_1 = census[census[:,2]==1,:]
race_2 = census[census[:,2]==2,:]
race_3 = census[census[:,2]==3,:]
race_4 = census[census[:,2]==4,:]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

x= min(len_0,len_1,len_2,len_3,len_4)

if(len_0==x):
    y=0
elif(len_1==x):
    y=1
elif(len_2==x):
    y=2
elif(len_3==x):
    y=3
elif(len_4==x):
    y=4

minority_race = y
print(minority_race)




# --------------
#Code starts here
import numpy as np
senior_citizens = census[census[:,0]>60,:]
working_hours_sum = sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)



# --------------
#Code starts here
high = census[census[:,1]>10,:]
low = census[census[:,1]<=10,:]
avg_pay_high = sum(high[:,7])/len(high)
avg_pay_low = sum(low[:,7])/len(low)

print(avg_pay_high)
print(avg_pay_low)


