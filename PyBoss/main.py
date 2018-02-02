import os
import csv
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
filename1='employee_data1.csv'
filename2='employee_data2.csv'
filepath1=os.path.join(filename1)
filepath2=os.path.join(filename2)
employeeid=[]
employeefullname=[]
dob=[]
ssn=[]
state=[]
#Open files Gather Data in Lists
with open (filepath1,'r',newline='') as csvfile:
    file1data=csv.reader(csvfile,delimiter=",")
    for row in file1data:
        employeeid.append(row[0])
        employeefullname.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
file1length=len(employeeid)
with open (filepath2,'r',newline='') as csvfile:
    file2data=csv.reader(csvfile,delimiter=",")
    for row in file2data:
        employeeid.append(row[0])
        employeefullname.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
#Delete Tite Row from File 2
del employeeid[file1length+1]
del employeefullname[file1length+1]
del dob[file1length+1]
del ssn[file1length+1]
del state[file1length+1]
numrows=len(employeeid)
numemployees=len(employeeid)-1 #Account for First Header Row

#Split Name into First and Last, Store in New Lists
names=[]
firstname=[]
lastname=[]
for i in range(1,numrows):
    names.append(employeefullname[i].split(" "))

#Split Date into DD, MM, YYYY and Rearrange into DD/MM/YYYY
day=[]
month=[]
year=[]
date=[]
newdob=[]
for i in range(1,numrows):
    date.append(dob[i].split("/"))
# for row in date:
    #month=row[0]
    #day=row[1]
    # year=row[2]
    
month=(row[0] for row in date)
day=(row[1] for row in date)
year=(row[2] for row in date)


# SSN re-written so only last 4 numbers show
ssnlast4=[]

for i in range(1,numrows):
    ssn.append(ssn[i].split("-"))
ssnlast4=(row[3] for row in ssn)

# Abbreviate State
st=[]
print(str(len(state)))
print(state[0])
print(state[1])
# for i in range(1,numrows):
#     currentstate=state[i]
#     st.append(us_state_abbrev[currentstate])
for i in range(1,numrows):
    st.append(us_state_abbrev[state[i]])
    
# Output to File
fileoutputname='PyBossOutput.csv'
fileoutputpath=os.path.join(fileoutputname)
with open (fileoutputpath,'w', newline='') as csvfile:
    outputdata=csv.writer(csvfile,delimiter=",")
    outputdata.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    outputdata.writerows(date)
