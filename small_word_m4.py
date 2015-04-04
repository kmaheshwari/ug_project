#
import re
import grammar_test
from grammar_test import main 
def find_key(value):
    for k,v in assumption.items():
        if v== value:
            return k

def spell_check(word):
    if ((len(word) == 2)):
        two_word = open("double_word.txt", "r+")
        tw  = two_word.read().split()
        if word in tw:
            return True
    if ((len(word) == 3)):
        three_word = open("three_word.txt", "r+")
        trw  = three_word.read().split()
        if word in trw:
            return True
    if ((len(word) == 4)):
        four_word = open("four_word.txt", "r+")
        fw  = four_word.read().split()
        if word in fw:
            return True
    return False

def replace(word,list):
        global sent
        for w,c in zip(word,list):
            if w.islower():
                print "in"
                sent = sent.replace(w, c)
                print sent
                assumption[w]=c
                print assumption
                
#for backtrack
def backtrack(wrd):
    global cnt2,sent
    
    
    if ((len(wrd) == 2)):
        n=0
        two_word = open("double_word.txt", "r+")
        tw  = two_word.read().split()
    
        for w in wrd:
            if (w.isupper() and n==0):
                
                
                    k=find_key(w)
                    print k
                    wrd=wrd.replace(w,k)
                    sent=sent.replace(w,k)
                    print sent
                    del assumption[k]
                    #for wrd in sent.split():
                    
    

                    replace(wrd,tw[cnt2])
                    cnt2=cnt2+1
                    n+=1


def pattern(word,fil):
        pat=""
        ol=[]
        n=c=0
        wd=word
        i=0
        for w in word:
                if w.islower():
                        
                    word=word.replace(w,'.')
        print word
        for i in range(len(fil)):
            n+=1
            if re.match(word,fil[i]):
                pat= fil[i]
                print pat
                replace(wd,pat)
                
                c=1
        if (n == len(fil)):
            if not c:
                print "hi"
                backtrack(wd)

#if a word contains double letters
def double_letter(word):
        global sent
        global assumption
        global double_word
        global l,doublew,key
        i=0
        for i in range(1,len(word)-2):
            if word[i] == word[i+1]:
                
                print "in"    
                double_w.append(word)
                print double_w
                double_word = open("double_letter_vowel.txt", "r+")
                doublew  = double_word.read().split()
                if (word[i].isupper()):
                    if word[i] not in doublew:
                        key=find_key(word[i])
                        print key
                        sent=sent.replace(word[i],key)
                        print sent
                        del assumption[key]
                        print assumption
                        if doublew[0] in assumption.values():
                            print "in 1"
                            for word in sent.split():
                                if doublew[0] in word:
                                    if spell_check(word):
                                        print key
                                        replace(key,doublew[1])
                                        print sent
                                    else:
                                        key1=find_key(doublew[0])
                                        sent=sent.replace(doublew[0],key1)
                                        del assumption[key1]
                                        replace(key1,doublew[0])
                        else:
                            replace(key,doublew[0])

                l = word[i]
            if word[-1] == word[-2]:
                double_w.append(word)
                double_word = open("double_letter_cons.txt", "r+")
                doublew  = double_word.read().split()
                l = word[-1]
        if double_w:
                j = 0
                replace(l,doublew[j])
                j+=1

def one_letter():
    global sent
    one_word = open("single_word.txt", "r+")
    ow  = one_word.read().split()
    for i in range(0,len(one_w)):
            sent = sent.replace(one_w[i], ow[i])
            cnt1=1
            print sent
            assumption[one_w[i]]=ow[i]


def two_letter():
    
    j=0
    global sent,cnt2
    global assumption
    two_word = open("double_word.txt", "r+")
    tw  = two_word.read().split()
    print tw
    tr=tw[cnt2]
    print tr
    for word in two_w:
        u=0    
        for t in word:
                if t.isupper():
                        u+=1

        if u==1:
            pattern(word,tw)
        if u==0:
                replace(word,tw[j])
                
                j+=1
        cnt2=1

def three_letter():
    global sent
    j=0
    print three_w
    three_word = open("three_word.txt", "r+")
    trw  = three_word.read().split()

    for word in three_w:
            u=0
            for t in word:
                    if t.isupper():
                            u+=1
            if u>=1:
                pattern(word,trw)
                                            
            if u==0:
                replace(word,trw[j])              
                    
            j+=1
    cnt3=1

def four_letter():
    global sent
    j=0
            
    four_word = open("four_word.txt", "r+")
    fw  = four_word.read().split()

    for word in four_w:
            u=0
            for t in word:
                    if t.isupper():
                            u+=1
            if u>=1:
                pattern(word,fw)
                                            
            if u==0:
                replace(word,fw[j])              
                    
            j+=1
    cnt3=1
    

s = raw_input("Enter the ciphertext: ")
match = re.match(r'^[A-Za-z ]*$', s)
if not match:
    print("Invalid CipherText")
else:
    sent = s.lower()
    words = sent.split()
    s_w = str(min(words, key=len))
    c=0
    cnt1=cnt2= 0
    assumption = {}
    assertion = {}
    one_w = []
    two_w = []
    three_w = []
    four_w = []
    double_w = []

    # for words having single letter

    for word in words:
            if ((len(word) == 1) and (word not in one_w)):
                    one_w.append(word)
    for i in range(len(words)-1):
        if len(word[i+1])==2:
            one_w.reverse()


    if one_w:
        one_letter()   
                                      
    # for words having two letters

    for word in sent.split():
           if ((len(word) == 2) and (word not in two_w)):
                  two_w.append(word)
           print two_w

    if two_w:
        two_letter()            

    
    # for words having three letters
    for word in sent.split():
        if ((len(word) == 3) and (word not in three_w)):
            three_w.append(word)
    if three_w:
        three_letter()
    
    # for words havin double letter
    for word in sent.split():
        if (len(word) > 2):
            double_letter(word)

    # for words having four letters
    for word in sent.split():
        if ((len(word) == 4) and (word not in four_w)):
            four_w.append(word)
    if four_w:
        four_letter()

   # main(sent)








            


                
        


  






        

