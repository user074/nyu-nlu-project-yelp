# central functions

import nltk
from nltk.corpus import treebank

# problem inside here
def identifying(tagged, lib):
    foods = []
    length = len(tagged)
    i=0
    while(i<length):
        bloc = i-1
        aloc = i+1
        candidate = tagged[i][0].lower()

        if candidate[-1]=='s':
            test = candidate[:-1]
        else:
            test = candidate
        #if(test in lib)or(candidate in lib): # ('NN' in tagged[i][1])and(test in lib):    # when food is found
        if('NN' in tagged[i][1])and(test in lib):
            #print(candidate)
            candidate = tagged[i][0].lower()
            #while(('NN' in tagged[bloc][1])or(('NN' in tagged[bloc-1][1])and((tagged[bloc][1]=='CC')or('NN' in tagged[bloc][1]))))and(bloc-1>=0):    # when there is names of food before the located
            while(('NN' in tagged[bloc][1])or(('NN' in tagged[bloc-1][1])and(tagged[bloc][1]=='CC')))and(bloc-1>=0):
                #while('NN' in tagged[bloc][1])and(bloc>=0):
                candidate = tagged[bloc][0].lower() + ' ' + candidate
                '''
                if('NN' in tagged[bloc][1])and(tagged[bloc][0] not in lib):    # when name of food is not in library
                    lib.append(tagged[bloc][0].lower())
                '''
                bloc = bloc-1
            #while(aloc<len(tagged))and('NN' in tagged[aloc][1]):
            while((aloc<len(tagged))and('NN' in tagged[aloc][1]))or((aloc+1<len(tagged))and('NN' in tagged[aloc+1][1])and('CC' in tagged[aloc][1])):
                candidate = candidate + ' ' + tagged[aloc][0].lower()
                if('NN' in tagged[aloc][1])and(tagged[aloc][0].lower() not in lib):    # when name of food is not in library
                    lib.append(tagged[aloc][0].lower())
                aloc +=1
            i = aloc -1
            if candidate not in foods:
                foods.append(candidate)
            #foods.append(candidate)
        i +=1
    return foods, lib


def tagging(sentence):
    sentence1 = sentence.replace('\n',' ')
    sentence2 = sentence1.replace('\/',' ')
    tokens = nltk.word_tokenize(sentence2)
    tagged = nltk.pos_tag(tokens)
    return tagged

def seedextract():
    food_seed = []
    f = open('seed.txt', 'rb')
    for item in f:
        item1 = str(item.strip())
        item2 = item1[2:]
        item = item2[:-1]
        food_seed.append(item)
    f.close()
    return food_seed


def seedsave(saving):
    thefile = open('seed.txt', 'w')
    for item in saving:
        thefile.write('%s' % item)
    thefile.close()
    return 1

def tag_n_id(sentence):
    one = tagging(sentence)
    lib = seedextract()
    two = identifying(one, lib)
    foods = two[0]
    #print(foods)
    #newlib = two[1]
    #seedsave(newlib)
    #purify()
    return foods

def check(word):
    c1 = nltk.word_tokenize(word)
    c2 = nltk.pos_tag(c1)
    return c2




