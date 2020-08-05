import pandas as pd 
import os, fnmatch


# print(sessionData)

## Steps: Pull from master data sheet
##        then go into each session and add columns
##        use searching to find proper CSV
##        make empty list, add to it, then add columns

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def participantGenerator(amount):
    for i in range(amount+1):
        if i == 0:
            continue
        if i < 10:
            yield 'P' +str(0) + str(i)
        else:
            yield 'P' + str(i)
    
    
if __name__ == "__main__":
    ## df.insert(2, "Age", [21, 23, 24, 21], True)
    # print(find('P01_S01*.csv', 'wellness_transcription'))
    masterData = pd.read_excel('FR_self_disclosure_analysis.xlsx', sheet_name=None)
    # print(masterData['P01']['FR'])
    sessionPath = 'wellness_transcription/P01/P01_S01_2019-09-26-17-20-15-2015.csv'
    sessionData = pd.read_csv(sessionPath)
    rowCount = len(masterData['P01'])
    # print(rowCount)
    ## dictionary mapping phrases to the rest of the info
    ## then go into the seperate transcripts, mark where each matches, and append the columns
    indexToSession = {1:'S01',2:'S02',3:'S02',4:'S03',5:'S03',6:'S04',7:'S04',8:'S05',9:'S05',10:'S06',11:'S06',12:'S06',13:'S07',14:'S07'}
    stringMapping = {}
    participant = 'P01'
    for row in masterData[participant].iterrows():
        if (row[1]['Self Disclosure (0/1)']) == 1:
            # print(type(row[0]))
            # print(indexToSession[2])
            sheet = pd.read_csv(find(str(participant)+'_'+str(indexToSession[row[0]])+'*.csv','wellness_transcription')[0])
            sheetRows = len(sheet)
            nullList = [0] * sheetRows
            nullList2 = nullList.copy()
            
            for row2 in sheet.iterrows():
                # print(row[1]['FR'],row2[1]['text'],'\n')
                if row2[1]['text'] == row[1]['FR']:
                    index = row2[0]
                    nullList[index] = row[1]['Context']
                    nullList2[index] = 1
                    sheet.insert(4,"Context",nullList, True)
                    sheet.insert(5,"Disclosure",nullList2,True)
                    print('inserted')
                    # sheet['Context'] = nullList
                    break
            sheet.to_csv(str(participant + str(indexToSession[row[0]])))
    # print(sheet)
    ## TODO: push to github and share link
    ## TODO: create a way to save this systematically
    ## TODO: decide if we need to do the close times first, or at the same time
    ## TODO: debug why sometimes a new column isnt being added.
    ## TODO: What to do with transcripts that dont have a self disclosure statement?
    ## TODO: create a generator for Participant codes **DONE**
    ## TODO: try to minimize use of external variables (Can we index by string?)
    ## TODO: NOTE: TRANSCRIPTS AND MASTER SHEET DO **NOT** MATCH ALWAYS
    #       Possibly need to either make a system to disregard words or find a new way to match. 