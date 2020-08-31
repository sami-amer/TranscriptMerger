import pandas as pd 
import nltk

def create(csv):
    df = pd.read_csv(csv)
    phrases =[]
    for item in df.iterrows():
        if item[1]['speaker'] == 'Jibo':
            phrases.append(item[1]['text'])
    return phrases

def match(csv, phrases):
    df = pd.read_csv(csv)
    indexes = []
    for item in df.iterrows():
        text = item[1]['comment']
        jaccards = float('inf')
        matched = ''
        index = 0
        for i, phrase in enumerate(phrases):
            if nltk.jaccard_distance(set(phrase),set(text)) < jaccards:
                tolerance = (abs(len(phrase) - len(text))/(max([len(phrase),len(text)]))) * 0.8 ## this number can be tinkered
                matched = phrase
                jaccards = nltk.jaccard_distance(set(phrase),set(text))
        if jaccards < tolerance:
            indexes.append(item[0])
    return indexes
        # print(text,'||', matched,'||', jaccards, tolerance)
if __name__ == "__main__":

    # sen1 = 'I am an amazing boy who is out of this world'
    # sen2 = 'I am an amazing boy who is out of this world'
    # print(nltk.jaccard_distance(set(sen1),set(sen2)))
    # text = "Before we get started, can you juice the figures that best describe how you feel right now?"
    phrases = create('wellness_transcription/P01/P01_S02_2019-09-27-18-20-33-2033.csv')
    # # print(a)
    # jaccards = float('inf')
    # matched = ''
    # index = 0
    # for i, phrase in enumerate(phrases):
    #     if nltk.jaccard_distance(set(phrase),set(text)) < jaccards:
    #         matched = text
    #         jaccards = nltk.jaccard_distance(set(phrase),set(text))
    #         index = i
    #     # phrases.remove(index)
    # print(jaccards,matched)
    indexes = match('wellness_aws_transcripts_csv/P01_S02.csv',phrases)
    print(indexes)