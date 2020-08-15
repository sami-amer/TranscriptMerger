## see how to count words
## try and see best way to merge to get lengths as close as possible
## how accurate is Jaccards when things are merged to be close but not exact

import pandas as pd

string1 = 'This is a test string with no punctuation.' ## 8 Words
string2 = 'This is a more. Complex String.  It has errors and [inaudible 00:38:29]' ## 11 words
# print(len(string2.split(' '))) # find a way to strip empty elements
data = pd.read_csv('wellness_aws_transcripts_csv/P01_S02.csv')
for row in data.iterrows():
    print(row[1]['comment'])