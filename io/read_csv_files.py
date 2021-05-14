import csv
from csv import writer
import pandas as pd

file = open("output.csv", "r")
df = pd.read_csv("output.csv")


# Reading CSV as vanilla lines

csv_reader = csv.reader(file, delimiter=',')
line_count = 0

'''
for row in csv_reader:
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    else:
        print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
        line_count += 1
'''


# Reading CSV as dictionary


csv_reader = csv.DictReader(file)
line_count = 0
'''
for row in csv_reader:
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    print(f'\t Title:{row["title"]}. Year: {row["year"]}. Network: {row["network"]}.')
    line_count += 1
print(f'Processed {line_count} lines.')
'''

'''
test_links = ['https://mydramalist.com/38301-romantic-doctor-teacher-kim-2', 'https://mydramalist.com/47779-vacation-in-my-own-way']
data_to_write = []
for link in test_links:
    for row in csv_reader:

        if link in row['url']:
            #print (link + " is written")

            print (row['url'])
        else: 
            data_to_write.append(['flower of evil', '2020', 'tvN', '70', 'Kim Chul Gyu','Yoon Jong Ho', 'Yoo Jung Hee', '16', '9.1 17496', '38524', '200', 'Thriller,Mystery,Psychological,Romance,Crime,Melodrama',  'Married Couple,Deception,Suspense,Family Secret,Hidden Personality,Smart Female Lead,Antisocial Personality Disorder,Detective,Serial Killer,Investigation', link])
            #print ("Weeeee")

'''

# Test Append

test_links = ['https://mydramalist.com/38301-romantic-doctor-teacher-kim-2', 'https://mydramalist.com/47779-vacation-in-my-own-way']

for link in test_links:
    if link in df.values: 
        pass

    else: 
        print ("writing")
        file = open("output.csv", "a")
        writer_object = writer(file)
        data_to_write = [['flower of evil', '2020', 'tvN', '70', 'Kim Chul Gyu','Yoon Jong Ho', 'Yoo Jung Hee', '16', '9.1 17496', '38524', '200', 'Thriller,Mystery,Psychological,Romance,Crime,Melodrama',  'Married Couple,Deception,Suspense,Family Secret,Hidden Personality,Smart Female Lead,Antisocial Personality Disorder,Detective,Serial Killer,Investigation', link]]
        writer_object.writerow(data_to_write[0])
        file.close()
#print (df['u'])
# file.close()

# print (data_to_write)

# if data_to_write: 
# file = open("output.csv", "a")
# writer_object = writer(file)
# writer_object.writerow(data_to_write[0])
# file.close()