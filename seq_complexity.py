#!/usr/bin/env python3

import glob
import pandas as pd
import matplotlib.pyplot as plt
import sys


#count the kmers
def countKmers(seq):
    kmerList = []
    for i in range(len(seq)):
        if len(seq[i:i+k]) == k:
            kmer = seq[i:i+k]
            kmerList.append(kmer)
        else:
            pass
    return(kmerList)

#plot and data frame
def plotKmerFreq(counter):
    w = range(len(counter))
    values = counter.values()
    labels = counter.keys()

    kmerFreq_df = pandas.DataFrame(counter, index=['kmer'])
    print(kmer_freq_df)
    kmerFreq_df.plot(kind='bar');

    plt.figure(figsize = (10,4))
    plt.bar(w, values, tick_label = labels);
    plt.savefig('kmerFreq_df.png')


#main 
counter = {}
k = int(input("kmer size? "))

for filename in glob.glob('*.fasta'):
        f = open(filename,'r')
        fasta = f.readlines()
        for row in f:
            if ">" in row:
                name = row.split(">")[1].split("\n")[0]
                continue
            if len(row) <= 1:
                continue
            seq = row.rstrip("\n")
            kmerList = countKmers(seq)
    

plotKmerFreq(kmerList)

print('Linguistic Complexity: ',len(kmerList), "/", (k**k))