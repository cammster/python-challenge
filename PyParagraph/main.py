#Script to Automate the Analysis of a Passage
#Import a Text File
#   Import Operating System Module
import os
#   Set Path
filename='Passage1.txt'
filepath=os.path.join(filename)
#   Open File
with open(filepath,'r') as text:
    #store text as string and print
    lines=text.read()
    print("Paragraph Analysis")
    print("-------------------") 
    strlength=len(lines)   #Total Number of characters in passage (letters,space,punctuation)
  #Approximate Word Count (split by space)
    words=lines.split(" ")  #store words in array
    numwords=len(words)     #obtain number of words
    print("Approximate Word Count: "+str(numwords))
#Approximate Sentence Count (split by period)
    numperiods=lines.count(".")
    print("Average Sentence Count: "+str(numperiods))
#Average Letter Count  - Take number of characters without spaces, commas, period and divide by numwords
    numcommas=lines.count(",")
    numspaces=numwords
    avglettercount=(strlength-numspaces-numcommas-numperiods)/numwords
    print("Average Letter Count per Word: "+str(int(avglettercount)))    
#Average Sentence Length (in words) - Take Word Count and Divide by Sentence Count
    sentencelength=int(numwords/numperiods)
    print("Average Sentence Length (in words): "+str(sentencelength))
