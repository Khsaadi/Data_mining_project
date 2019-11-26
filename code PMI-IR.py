# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:21:07 2019

@author: LENOVO
"""

from __future__ import division
import nltk, re, pprint
from nltk import bigrams
import urllib,urllib.request
import copy
from nltk.collocations import *
from nltk.tokenize import word_tokenize
import nltk.data
import urllib
import json
from math import log
import itertools


list=[]
newlist=[]
newlist1=[]
ct=0

def hits(word1,word2=""): #
    #query = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=%s"
    #query="http://example.com/over/there?name=ferret"
    query='www.google.com'
    #query="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"
    if word2 == "":
        results = urllib.request.urlopen(query % word1)
    else:
         print(query )
         results =urllib.request.urlopen(query )
         
         #% word1+" "+"AROUND(10)"+" "+word2)
         #results = urllib.request.urlopen(query % word1+" "+print("AROUND(10)")+" "+word2)
         #results = urllib.request.urlopen(query)
        
    json_res = json.loads(results.read())
    google_hits=int(json_res['responseData']['cursor']['estimatedResultCount'])
    return google_hits


def so(phrase):
    num = hits(phrase,"excellent")
    #print num
    den = hits(phrase,"poor")
    #print den
    ratio = num / den
    #print ratio
    sop = log(ratio)
    return sop

list1= ["RB","RBR","RBS"]
list2= ["VB","VBD","VBN","VBG"]
list_combn = itertools.product(list1,list2)



        

def check(newl,spl1):
    print (newl)
    print (spl1)
    for k in range(0,len(newl)):
        if(k!=len(newl)-1):
            list_new=[]
            list_new.append(newl[k])
            list_new.append(newl[k+1])
            list_new = tuple(list_new)
        
            if( newl[k]=="JJ" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS"):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])
                
            if( newl[k]=="JJ" and newl[k+1]=="NN" ) or ( newl[k]=="JJ" and newl[k+1]=="NNS" ):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])
                
            if( newl[k]=="NN" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS") or ( newl[k]=="NNS" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS"):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])
                
            if( newl[k]=="RB" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS") or ( newl[k]=="RBR" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS") or ( newl[k]=="RBS" and newl[k+1]=="JJ" and newl[k+2]!="NN" and newl[k+2]!="NNS"):
                return "".join(spl1[k])+" "+"".join(spl1[k+1])
                
            for iter in list_combn:
                if(list_new == iter):
                    return "".join(spl1[k])+" "+"".join(spl1[k+1])
            
            

def text_pos(raw):
    global list,newlist,newlist1,ct
    print ("raw input:",raw)
    spl=raw.split()
    print ("\n")
    print ("split version of input:",spl)
    pos=nltk.pos_tag(spl)
    print ("\n")
    print ("POS tagged text:","")
    for iter in pos:
        print (iter,"")
    for i in range(0,len(pos)):
        if(i!=len(pos)-1):
            list.append(pos[i])
            list.append(pos[i+1])
            t1 = list[0]
            t2 = list[1]
            newlist.append(t1[1])
            newlist.append(t2[1])
            list=[]
    print ("\n")
    print ("Extracting the tags alone:","")
    print (newlist)
    for j in range(0,len(newlist)):
        if((j%2!=0) and (j!=len(newlist)-1)):
            newlist[j]=0
            
    newlist = [x for x in newlist if x != 0]
    print ("Checking whether the tags conform to the required pattern...")
    print ("\n")
    print (spl)
    print (newlist)
    print ("The extracted two-word phrases which satisfy the required pattern are:")
    strr1=check(newlist,spl)
    return strr1

print ("PMI - Pointwise Mutual Information")
print ("\n")
strr = text_pos("Nokia is a amazing phone")
print (strr)
x = so(strr)
print( x)