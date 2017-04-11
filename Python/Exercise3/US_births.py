'''
1. Define function read_csv() to read a .csv file, 
year: Year (1994 to 2003).
month: Month (1 to 12).
date_of_month: Day number of the month (1 to 31).
day_of_week: Day of week (1 to 7).
births: Number of births that day.
2. Split the string on newline character \n and remove the header.
3. Iterate over the string and split each row on ','
4. Convert each field to int
5. Assign this to the final list and return this list
'''
def read_csv(file):
    strlst = open(file).read().split("\n")
    string_list = strlst[1:len(strlst)]
    
    final_list = []
    for i in string_list:
        string_fields = i.split(",")
        int_fields = []
        for j in string_fields:
            int_fields.append(int(j))
        final_list.append(int_fields)
    return(final_list)    

'''
Calculate number of births by month
'''
def month_births(birth_list):
    births_per_month = {}
    for mnth in birth_list:
        if mnth[1] in births_per_month:
            births_per_month[mnth[1]] = births_per_month[mnth[1]] \
               + mnth[4]
        else:
            births_per_month[mnth[1]] = mnth[4]
    return(births_per_month)  

'''
Calculate number of births each day of week
'''
def dow_births(birth_list):
    births_per_day = {}
    for day in birth_list:
        if day[3] in births_per_day:
            births_per_day[day[3]] = births_per_day[day[3]] + day[4]
        else:
            births_per_day[day[3]] = day[4]
    return(births_per_day)

'''
Calculate number of births by Year/month/date_of_month/day_of_week by
specifying the list and column position (year = 1, month = 2, 
date_of_month = 3, day_of_week = 4)
'''
def calc_counts(birth_list, col_pos):
    totals = {}
    for i in birth_list:
        if i[col_pos-1] in totals:
            totals[i[col_pos-1]] = totals[i[col_pos-1]] + i[4]
        else:
            totals[i[col_pos-1]] = i[4]
    return(totals)

''' 
Calculate min and max key/values in a dictionary 
'''
def calc_minmax(datset):
    minval = min(datset.values())
    maxval = max(datset.values())
    minkey = min(datset.keys())
    maxkey = max(datset.keys())
    return(minkey, maxkey, minval, maxval)    
              
''' 
Sort the dictionary by key/val (parm = 1 for sort by key, 
parm = 2 for sort by value) 
'''
from collections import OrderedDict
def sort_dict(datset, parm):
    if(parm == 1):
        ordered = OrderedDict(sorted(datset.items(), key = lambda a: a[0]))
    elif(parm == 2):
        ordered = OrderedDict(sorted(datset.items(), key = lambda a: a[1]))
    return(ordered)


# Main logic
cdc_list = read_csv(r'D:\GitHub\Data-Science\Python\Exercise3\US_births_2000-2014_SSA.csv')
print("\n-----------------")
print("First 10 elements")
print("-----------------")
print(cdc_list[0:10])

#Number of births each month (Function used: month_births)
cdc_month_births = month_births(cdc_list)
print("\n---------------------------")
print("Number of births each month")
print("---------------------------")
print(cdc_month_births)

#Number of births each day of week (Function used: dow_births)
cdc_day_births = dow_births(cdc_list)
print("\n---------------------------------")
print("Number of births each day of week")
print("---------------------------------")
print(cdc_day_births)

#Number of births every year (Function used: calc_counts)
cdc_year_births = calc_counts(cdc_list,1)
print("\n-------------")
print("Yearly totals")
print("-------------")
print(cdc_year_births)

#Number of births every month (Function used: calc_counts)
cdc_month_births = calc_counts(cdc_list,2)
print("\n---------------")
print("Monthly totals:")
print("---------------")
print(cdc_month_births)

#Number of births in a month (daywise) (Function used: calc_counts)
cdc_dom_births = calc_counts(cdc_list,3)
print("\n--------------------")
print("Day-of-month-totals:")
print("--------------------")
print(cdc_dom_births)

#Number of births in a week (daywise) (Function used: calc_counts)
cdc_dow_births = calc_counts(cdc_list,4)
print("\n-------------------")
print("Day-of-week-totals:")
print("-------------------")
print(cdc_dow_births)

#Extract the keys from cdc_dow_births
print("\n------------------------")
print("Dict Keys (Day-of-week):")
print("------------------------")
print(cdc_dow_births.keys())

#Extract the values from cdc_dow_births
print("\n-------------------------")
print("Dict Values (Day-of-week:")
print("-------------------------")
print(cdc_dow_births.values())

#Calculate the min key, max key, min val, max, val from cdc_year_births
minmax = calc_minmax(cdc_year_births)
print("\n-------------------")
print("Min/Max key/values:")
print("-------------------")
print("Min_key: ", minmax[0], "\nMax_key: ", minmax[1], "\nMin_val: " \
      , minmax[2], "\nMax_val: " , minmax[3])

#Sort the dictionary cdc_year_births by key using the in-built function sorted
print("\n----------------------------------------")
print("Sort by key (in-built function 'sorted')")
print("----------------------------------------")
print(sorted(cdc_year_births))

#Sort the dictionary cdc_year_births by key using the user-defined function
#sort_dict (parm value 1 (key)
print("\n----------------------")
print("Sort by key (parm = 1)")
print("----------------------")
sortbykey = sort_dict(cdc_year_births, 1)
print(sortbykey)

#Sort the dictionary cdc_year_births by value using the user-defined function
#sort_dict (parm value 2 (value)
print("\n----------------------")
print("Sort by val (parm = 2)")
print("----------------------")
sortbyval = sort_dict(cdc_year_births, 2)
print(sortbyval)

'''
tmp = cdc_list[0:10]
print(tmp)
for i in tmp:
    print(i[0])
    years = set(i[0])
'''
