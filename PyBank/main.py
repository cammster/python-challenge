#Analyze Revenue Data (Date/Revenue)
#Assumptions: Column 1 is string sorted old/new with entry in every month
#             Column 2: Revenue
import os
import csv
#Set Path
filename='budget_data_1.csv'
filepath=os.path.join(filename)
fileoutputname='PyBankOutput.txt'
fileoutputpath=os.path.join('PyBankOutput.txt')
#Set Lists
datelist=[]
revenuelist=[]
datenum=[]

#Open CSV File, Write Dates and Revenues into 2 Lists
with open (filepath,'r',newline="") as csvfile:
    revenuedata=csv.reader(csvfile,delimiter=",") 
    for row in revenuedata:
        datelist.append(row[0])
        revenuelist.append(row[1])

#Total Number of Months Included in Dataset
nummonths2=len(datelist)-1  #Account for Title Row, Each Row Should contain a month

#Total Amount of Revenue Gained Over Entire Period
revenueitems=len(revenuelist)
revnum=[]
#  Convert list of str to numbers and sum
for i in range(1,revenueitems):
    revnum.append(int(revenuelist[i]))
totalrev=sum(revnum)

#Average Change in Revenue Between Months Over Entire Period - Calculates the difference in Revenue 
revchange=[]
revnumlength=len(revnum)
for i in range(1,revnumlength):
    revchange.append(revnum[i]-revnum[i-1])
avgrevchange=sum(revchange)/len(revchange)

#Greatest Increase in Revenue (date/amount) over entire period
revmax=max(revnum)
revmaxindex=revnum.index(revmax)
dateslice=datelist[1:] #Take out header to ensure index maxes Revenue list referenced
datemax=dateslice[revmaxindex]

#Greatest Decrease in Revenue (date/amount) over entire period
revmin=min(revnum)
revminindex=revnum.index(revmin)
datemin=dateslice[revminindex]

#Print Analysis to Terminal and Text File
print("Financial Analysis")
print("-----------------------------------")
print("Total Months: ",nummonths2)
print("Total Revenue: $",totalrev)
print("Average Revenue Change: $",avgrevchange)
print("Greatest Revenue Increase: ",datemax,revmax)
print("Greatest Revenue Decrease: ",datemin,revmin)

with open(fileoutputpath,'w') as text:
    fileoutputname=text.write("Financial Analysis")




