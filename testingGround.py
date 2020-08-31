## see how to count words
## try and see best way to merge to get lengths as close as possible
## how accurate is Jaccards when things are merged to be close but not exact

import pandas as pd

string1 = 'This is a test string with no punctuation.' ## 8 Words
string2 = 'This is a more. Complex String.  It has errors and [inaudible 00:38:29]' ## 11 words
# print(len(string2.split(' '))) # find a way to strip empty elements

def get_word_count(string):
    return len(string.split(' '))


# aws = pd.read_csv('wellness_aws_transcripts_csv/P01_S02.csv')
# manual = pd.read_csv('wellness_transcription/P01/P01_S02_2019-09-27-18-20-33-2033.csv')
# awsNums = []
# manNums = []
# for row in aws.iterrows():
#     awsNums.append(get_word_count(row[1]['comment']))
# for row in manual.iterrows():
#     manNums.append(get_word_count(row[1]['text']))

# print(awsNums,'\n\n',manNums)

def sentence_combiner(awsList, manList):
    ## case for recursion end is either list having only 1 element.
    if awsList is None or manList is None:
        return None
    newList1,newList2 = get_merges(awsList,manList,5)
    # print(newList1,'\n\n',newList2,'\n\n\n')
    sentence_combiner(newList1, newList2)

def get_merges(awsList, manList,tolerance):
    ## NOTE: there is an issue with the tolerance
    # when the targeted number is small, there is an issue with being first under the tolerance, then way over i.e. 1 + 49, 1 is less than 7 by x but 50 is more than 7 by x    
    
    if awsList[0] <= manList[0]:
        for i in range(len(awsList)):
            #  print(sum(aws[:i]), manList[0])
            if sum(awsList[:i]) == 0:
                continue
            if manList[0] - tolerance <= (sum(awsList[:i])) <= manList[0] + tolerance:
                print('matched', awsList[:i],manList[0])
                return awsList[i:], manList[1:]
    elif awsList[0] > manList[0]:
        for i in range(len(manList)):
            #  print(sum(aws[:i]), manList[0])
            if sum(manList[:i]) == 0:
                continue
            if awsList[0] - tolerance <= (sum(manList[:i])) <= awsList[0] + tolerance:
                print('matched', manList[:i],awsList[0])
                return awsList[1:], manList[i:]
    else:
        print('WOW')
    
if __name__ == "__main__":
    aws1 = [1, 2, 17, 25, 7, 8, 1, 1, 4, 20, 7, 8, 10, 1, 1, 6, 7, 15, 1, 8, 12, 13, 18, 3, 11, 16, 2, 19, 3, 10, 19, 1, 7, 10, 20, 7, 7, 1, 7, 6, 4, 26]
    man1 = [15, 4, 20, 41, 1, 49, 1, 29, 21, 31, 30, 2, 19, 33, 38, 14, 1, 44]
    sentence_combiner(aws1,man1)