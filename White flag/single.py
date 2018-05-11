import nltk
from nltk.corpus import treebank
from central import *
import sys

newfile = open("final.txt", "w")

first = []
for line in sys.stdin:          # extracting from file, line by line
    line1 = line.strip()
    line2 = line.split('text\": \"')[1]
    line3 = line2.split('\"')[0]
    first.append(line3)

second = []
for line in first:              # tagging sentence by sentence
    line = line.strip()
    res = tag_n_id(line)
    for item in res:
         second.append(item)

lib = seedextract()

fin = []
for item in second:       # extracint food name and food name only
    if item in fin:
        continue
    if('\\' in item)or('/' in item)or('=' in item)or('*' in item)or('[' in item):
        continue
    fin.append(item)

fin2 = []
for item2 in fin:
    signal = True
    hold = item2
    letters = hold.split(' ')

    for stuff in letters:
        if stuff=='and':
            continue
        if not (stuff in lib):
            signal = False
            break
    if(signal):
        fin2.append(item2)

final = fin2
for i in final:
    newfile.write("%s \n"%(i))


newfile.close()












