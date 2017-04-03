#common unisex (gender-neutral) names in the United States
'''
Header	Definition
name	First names from the Social Security Administration
total	Total number of living Americans with the name
male_share	Percentage of people with the name who are male
female_share	Percentage of people with the name who are female
gap	Gap between male_share and female_share

Sample data
1	Casey	176544.3281	0.584286566	0.415713434	0.168573132

'''
 
#Open the file and read the data. Split the data based on '\n'
#Split the data based on "," and append it to a list
filopn = open(r"D:\GitHub\Datasets\unisex-names\unisex_names_table.csv")
names = filopn.read()
names_list = names.split("\n")
split_list = []
for i in names_list:
    comma_list = i.split(",")
    split_list.append(comma_list)

#The length of the list is 921 including the header. Skip the header and read
#only the detail records. It is seen that one of the records has got invalid data. That record is in
#920th position. Slice that records also.
print(len(split_list))
split_list = split_list[1:len(split_list)-1]

#Convert the numeric values in the record to either int or float
conv_list = []
for j in split_list:
    temp_list = [int(j[0]), j[1], float(j[2]), float(j[3]), float(j[4]), \
                 float(j[5])]
    conv_list.append(temp_list)
    
#Get the list of records with total count < 100, 1000, 10000
fil_lt100 = []
fil_lt1k = []   #Less than 1000 but greater than or equal to 100
fil_lt10k = []  #Less than 10000 but greater than or equal to 1000
for k in conv_list:
    if k[2] < 100:
        fil_lt100.append(k)
    elif k[2] >= 100 and k[2] < 1000:
        fil_lt1k.append(k)
    elif k[2] >= 1000 and k[2] < 10000:
        fil_lt10k.append(k)

print(fil_lt100[0:5])
print(fil_lt1k[0:5])
print(fil_lt10k[0:5])

#Get the list of names with higher male_share compared to the female_share
fil_mal = []
fil_fem = []
for l in conv_list:
    if l[3] > l[4]:
        fil_mal.append(l)
    else:
        fil_fem.append(l)


#Sort based on the total..


 

'''
names_list = []
'''
