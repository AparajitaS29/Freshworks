import json
import re as regex
import os
import glob


def filebrowser():
    return [f for f in glob.glob("*.json")]
    
    
def isDictEmpty(structure):
    if structure:
        #print('Structure is not empty.')
        return False
        
    else:
        #print('Structure is empty.')
        return True
               

listOfFiles = filebrowser()


jsonFilePrefix = input("Enter JSON file name prefix: ")
jsonMergeFileName = input("Enter the file to merge into: ")

jsonMergeFileName = jsonMergeFileName + ".json"

mergedArray = {}

for files in listOfFiles:
    if regex.findall(jsonFilePrefix, files):
        with open(files) as f:
            data = json.load(f)
            dictionaryKeyName = list(data)
            
            if isDictEmpty(mergedArray):
                mergedArray[dictionaryKeyName[0]] = []
            
            for p in data[dictionaryKeyName[0]]:
                mergedArray[dictionaryKeyName[0]].append(p)
                #print(mergedArray)

        
print(mergedArray)


with open(jsonMergeFileName, 'w') as outfile:
    json.dump(mergedArray, outfile, indent=4)
