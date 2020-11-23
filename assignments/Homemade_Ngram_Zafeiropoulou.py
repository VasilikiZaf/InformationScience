import os 
import string
type(string.punctuation)


os.getcwd()

os.chdir(r"C:\Users\vasil\Desktop\InformationScience\course\data")

def readsplitclean(file):
    with open(file, 'r') as text:
        corpus = text.readlines()
        newlist = []
        punct = string.punctuation + '-'
        for l in corpus:
            words = l.split()
            for w in words:
                w = w.lower()
                w = w.strip(punct)
                newlist.append(w)
        return newlist

def freqgenerator(x):
    mylist = readsplitclean(x)
    freqdic = {}
    sortdic = []
    for word in mylist:
        if word not in freqdic:
            freqdic[word] = 0
        freqdic[word] += 1
    sortdic = sorted(freqdic.items(), key = lambda x : x[1], reverse = True)
    return sortdic[:101]

freqgenerator('corpus.txt')
