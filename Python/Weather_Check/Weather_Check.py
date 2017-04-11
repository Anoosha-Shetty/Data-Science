### Weather Check
'''
Header | Definition
---|---------
`Do you typically check a daily weather report?` | Yes or No
`How do you typically check the weather?` | "The Weather Channel",
"Local TV News", "Radio weather", "Internet search",
"The default weather app on your phone", "Newsletter", "Newspaper",
"A specific website or app (please provide the answer)
`A specific website or app (please provide the answer)` | If they responded this
value for the second question, they were asked to write-in the app or website
they used. 
`If you had a smartwatch (like the soon to be released Apple Watch), how likely
or unlikely would you be to check the weather on that device?` | "Very Likely",
"Somewhat Likely", "Somewhat unlikely", "Very unlikely"
`Age` | 18-29, 30-44, 45-59, 60+
`What is your gender?` | Female, Male
`How much total combined money did all members of your HOUSEHOLD earn last
year?` | $0 to $9,999, $10,000 to $24,999, $25,000 to $49,999,
$50,000 to $74,999, $75,000 to $99,999, $100,000 to $124,000,
$125,000 to $149,999, $150,000 to $174,999, $175,000 to $199,999, $200,000+,
Prefer not to answer. 
`US Region` | New England, Middle Atlantic, East North Central,
West North Central, South Atlantic, East South Central, West South Central,
Mountain, Pacific. 
'''
def uniq(parm1):
    uniq_lst = list(set(parm1))
    return(sorted(uniq_lst))
    
def val_rep(pos):
    for i in mod_lst:
        if i[pos] == '-':
            i[pos] = 'N/A'
    return(mod_lst)
    
def ageprob(parm1, parm2):
    #print(parm1)
    #print(parm2)
    dict1 = {}
    print("**********",parm1,"**********")
    for i in parm2:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    print(dict1)
    return(dict1)


fileop = open(r"D:\GitHub\Datasets\weather-check\weather-check.csv")
wchk = fileop.read().split("\n")
wchk1 = wchk[1:len(wchk)]
#print(wchk1[0:20])

wchk_lst = []
len_lst = []
for i in wchk1:
    tmp_lst = i.split(",")
    len_lst.append(len(tmp_lst))
    wchk_lst.append(tmp_lst)
    
#Call the function to get the unique values for the individual list length
len_lst = uniq(len_lst)
print(len_lst)

#As the list contains
mod_lst = []
for i in wchk_lst:
    if len(i) == 9:
        mod_lst.append(i)
    elif len(i) == 10:
        tmp_lst = [i[0], i[1],i[2], i[3], i[4], i[5],i[6],i[7]+i[8],i[9]]
        mod_lst.append(tmp_lst)
    elif len(i) == 11:
        #print(i)
        tmp_lst = [i[0], i[1],i[2], i[3], i[4], i[5],i[6],i[7]+i[8]+i[9],i[10]]
        mod_lst.append(tmp_lst)
        #print(tmp_lst)
    elif len(i) == 12:
        tmp_lst = [i[0], i[1],i[2], i[3]+","+i[4], i[5],i[6],i[7],i[8]+i[9]+i[10],i[11]]
        mod_lst.append(tmp_lst)
    elif len(i) == 13:
        tmp_lst = [i[0], i[1],i[2], i[3]+","+i[4]+","+i[5]+","+i[6],i[7], i[8], i[9], i[10]+i[11],i[12]]
        mod_lst.append(tmp_lst)
        

#print(mod_lst[0:100])


# Create a dictionary with Region as the key and number of entries for each
Region = {}
for i in mod_lst:
    if i[8] in Region:
        Region[i[8]] = Region[i[8]] + 1
    else:
        Region[i[8]] = 1

#print(Region)

# Replace the fields having values '-' with 'N/A'
tmp_lst = val_rep(2)
tmp_lst = val_rep(3)
tmp_lst = val_rep(4)
tmp_lst = val_rep(5)
tmp_lst = val_rep(6)
tmp_lst = val_rep(7)
tmp_lst = val_rep(8)

# Remove double quotes " in the annual income column (8th column)
# Move the details of the probability factor to a separate list
# Move the details of age-group to a separate list
fin_lst = []
prob_lst = []
agegrp_lst = []
for i in mod_lst:
    i[7] = i[7].replace('"','')
    fin_lst.append(i)
    prob_lst.append(i[4])
    agegrp_lst.append(i[5])





#Get unique values for the probability of buying a smartwatch
prob = uniq(prob_lst)
print(prob)

# Get details about the age group of people who are more likely to buy a smartwatch

tmp_dct = {}
fil_lst = []

for i in prob:
    tmp_lst = []
    for j in fin_lst:
        if j[4] == i:
            #print("a")
            tmp_lst.append(j[5])
    #print(tmp_lst)
    tmp_dct = ageprob(i,tmp_lst)
    #print(tmp_dct)
