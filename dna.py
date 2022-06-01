import sys
import re
import csv
import copy

# check number of argv
if (len(sys.argv) != 3):
    print('Usage: python dna.py data.csv sequence.txt')
    sys.exit(1)

# open the database
with open(sys.argv[1], 'r') as database:
    database_reader = csv.DictReader(database)
    # create list of dictionaries for the read data
    person_data = list(database_reader)
# extract the fields name
fields = list(person_data[0].keys())

# open the sequence file
with open(sys.argv[2], 'r') as dna:
    read_sequence = dna.read()
# create dictionary for the repeatition of each STR in the dna sequence
repeatition = {}
STRs = fields[1:]
for STR in STRs:
    match = re.findall(rf"(?:{STR})+", read_sequence)
    if (not match):
        repeatition[STR] = '0'
    else:
        longest = max(match, key=len)
        count = str(int(len(longest)/len(STR)))
        repeatition[STR] = count

# create a copy of person_data to remove the name field from
person_data_copy = copy.deepcopy(person_data)
# remove name field data to easily check each person
for dictionary in person_data_copy:
    del(dictionary['name'])

# check each person
i = 0
for person in person_data_copy:
    if (person == repeatition):
        print(f"{person_data[i]['name']}")
        exit()
    i += 1

print('No match')