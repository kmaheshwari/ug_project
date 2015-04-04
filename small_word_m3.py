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
                if c not in assumption.values():
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


def pat_rep(list,file):
    
    j=0
    for word in list:
        u=0    
        for t in word:
                if t.isupper():
                        u+=1
                        break

        if u>=1:
            pattern(word,file)
        if u==0:
                for fl in file:
                    c=0
                    for f in fl:
                        if f in assumption.values():
                            c=1
                    if c==1:
                        j+=1     
                        replace(word,file[j])
                        break
                
                
        

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
            if not c==1 :
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
    
    for i in range(0,len(one_w)):
            sent = sent.replace(one_w[i], ow[i])
            cnt1=1
            print sent
            assumption[one_w[i]]=ow[i]


s = raw_input("Enter the ciphertext: ")
match = re.match(r'^[A-Za-z ]*$', s)
if not match:
    print("Invalid CipherText")
else:
    sent = s.lower()
    words = sent.split()
    s_w = str(min(words, key=len))
    cnt1=cnt2=cnt3=cnt4= 0
    assumption = {}
    assertion = {}
    one_w = []
    two_w = []
    three_w = []
    four_w = []
    double_w = []

    #to open all the required files
    one_word = open("single_word.txt", "r+")
    ow  = one_word.read().split()

    two_word = open("double_word.txt", "r+")
    tw  = two_word.read().split()

    three_word = open("three_word.txt", "r+")
    trw  = three_word.read().split()

    four_word = open("four_word.txt", "r+")
    fw  = four_word.read().split()

    #open four letter noun list
    nfour_word = open("4_letter_nouns.txt", "r+")
    nfw  = nfour_word.read().split()
    
    nthree_word = open("3_letter_noun.txt", "r+")
    ntrw  = nthree_word.read().split()
                    

    # for words having single letter
    for i in range(len(words)-1):
        print "inloop"
        if len(words[i])==1:
            if len(words[i+1])==2:
                ow.reverse()

    for word in words:
            if ((len(word) == 1) and (word not in one_w)):
                    one_w.append(word)
    
    if one_w:
        one_letter()   
                                      
    # for words having two letters
    for i in range(len(words)-1):
        if len(words[i])==1:
            if len(words[i+1])==2:
                replace(words[i+1],'AM')

    for word in sent.split():
           if ((len(word) == 2) and (word not in two_w)):
                  two_w.append(word)
           print two_w
    
    if two_w:
        pat_rep(two_w,tw)           
        cnt2+=1

    #checking A-noun pair
    s1 = sent.split()
    nf=nt=[]
    for i in range(len(s1)-1):
        if len(s1[i])==1:
            if s1[i]=='A':
                print s1[i+1]
                if len(s1[i+1])==3:
                    nt.append(s1[i+1])
                    pat_rep(nt,ntrw)
                if len(s1[i+1])==4:
                    nf.append(s1[i+1])
                    pat_rep(nf,nfw)
    
    # for words having three letters
    for word in sent.split():
        if ((len(word) == 3) and (word not in three_w)):
            three_w.append(word)
    if three_w:
        pat_rep(three_w,trw)
        cnt3+=1
    # for words havin double letter
    for word in sent.split():
        if (len(word) > 2):
            double_letter(word)

    # for words having four letters
    for word in sent.split():
        if ((len(word) == 4) and (word not in four_w) ):
            if not word.isupper():
                four_w.append(word)
    if four_w:
        pat_rep(four_w,fw)
        cnt4+=1
    main(sent)








            


                
        


  






        

