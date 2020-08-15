sentences = {'"Awesome. All right, before we get started, can you choose the figures that best describe how you feel right now?"'}


if __name__ == "__main__":
    import nltk
    sen1 = 'I am an amazing boy who is out of this world'
    sen2 = 'I am an amazing boy who is out of this world'
    print(nltk.jaccard_distance(set(sen1),set(sen2)))
