def participantGenerator(amount):
    for i in range(amount+1):
        if i == 0:
            continue
        if i < 10:
            yield 'P'+str(0) + str(i)
        else:
            yield 'P' + str(i)
    
if __name__ == "__main__":
    for x in participantGenerator(40):
        print(x)