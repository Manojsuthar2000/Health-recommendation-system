import pandas as pd
from collections import defaultdict
from simpleai.search import CspProblem, backtrack

print("This program going to tell you about the disease that you may have depending on your input symptoms : ")
print("------------------------------------------------------------------------------------------------------")

Dataset = pd.read_csv('Dataset.csv')
Dataset = Dataset.fillna(method='ffill')
Disease_list = Dataset['Disease'].unique()
print("This program is only going to tell u about this diseases : ")
for i in range(len(Disease_list)):
    print(str(i+1)+Disease_list[i].rjust(15),end='    ')
    if (i+1)%5==0:
        print()

print("------------------------------------------------------------------------------------------------------")
print("The symptoms of this diseases are : ")
Symptom_list=Dataset['Symptom'].unique()
for i in range(len(Symptom_list)):
    print(str(i+1).rjust(3)+Symptom_list[i].rjust(27),end='    ')
    if (i+1)%3==0:
        print()

print("\n------------------------------------------------------------------------------------------------------")
print("To select the symptoms you have write the corresponding integers one by one :\nSymptoms numbers are : (please write aleast two Symptoms) \n")
flag='y'
input_Symptom_list=[]
while flag=='y' or flag=='Y':
    input_Symptom_list.append(Symptom_list[int(input())-1])
    flag=input("Do you like to add more Symptoms : Press y or Y : ")

print("------------------------------------------------------------------------------------------------------")
print("Your Symptoms are : ")
input_Symptom_list=tuple(input_Symptom_list)
for i in input_Symptom_list:
    print(i)

symptom_disease_dict = defaultdict(list)
for symptom in input_Symptom_list:
    for idx, row in Dataset.iterrows():
        if row[2]==symptom:
            symptom_disease_dict[symptom].append(row[0])

Symptom_Disease = dict((symptom_disease_dict.items()))

def constraint(variables,values):
    for i in range(len(values)-1):
        if values[i]!=values[i+1]:
            return False
    return True

constraints=[(input_Symptom_list,constraint)]
problem=CspProblem(input_Symptom_list,Symptom_Disease,constraints)
output = backtrack(problem)
if output!=None:
    print("\nThe disease that you may have is "+ output[input_Symptom_list[0]]+'.')
else: 
    print("\nYour don't have any disease from above list")
