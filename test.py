from difflib import SequenceMatcher

with open('file1.txt') as file01 , open('file2.txt') as file02:
    data_file1 = file01.read()
    data_file2 = file02.read()

    matches = SequenceMatcher(None,data_file1,data_file2).ratio()

    print(f" The plagarised content is {matches*100}%")


## Th percentage of the plagarised content shall be displayed here.