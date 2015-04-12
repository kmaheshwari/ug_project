#
import re
import grammar_test
from grammar_test import main 
from Tkinter import *
import string

def result(strng):

    tex.insert(END,strng)
    tex.grid()
      


# def show_entry_fields():
#     print("CipherText: %s\nPlainText: %s" % (e1.get(), e2.get()))
#     e1.delete(0,END)
#     e2.delete(0,END)


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

def replacefunc(word,list):
        global sent
        for w,c in zip(word,list):
            if w.islower():
                if c not in assumption.values():
                    sent = sent.replace(w, c)
                    print sent
                    assumption[w]=c
                    print assumption
                
def transposition():
    global sent
    upper = []
    p = c =0
    for words in sent:
        for w in words:
            if w.isupper():
                key = find_key(w)
                print key
                p = ord(w.lower())
                c = ord(key)
                upper.append(c-p)
                
    upper = list(set(upper))
    print upper
    if len(upper)==1:
        for words in sent:
            for w in words: 
                if w.islower():
                    pr = (ord(w) - upper[0])
                    if pr < 97:
                        pr = ord(w) + 26 - upper[0]
                    pr = (chr(pr)).upper()
                    sent = sent.replace(w,pr)
                    assumption[w] = pr
                    print assumption
                    print sent
#for backtrack
def backtrack(wrd,file):
    global sent
    if len(wrd)==2:
        for w in wrd:
            if w.isupper():
                if w in sent:
                    print "hi"
    
def pat_rep(lst,fil,cnt):

    
    j=0
    for word in lst:
        i = lst.index(word)
        print "right"
        u=0    
        ch = 0
        for t in word:
            if t in assumption:
                word=word.replace(t,assumption[t])
                
                t=t.replace(t,assumption[t])

            if t.isupper():
                u+=1
                print u
        lst[i] = word
        print lst
        if u>=1 and u<len(word):
            print word
            pattern(word,fil,cnt)
        if u==0:
                
            c=0
            for f in fil[cnt]:
                if f in assumption.values():
                    c=1
            if c>0:
                cnt+=1
                    
            if c==0:
                     
                replacefunc(word,fil[cnt])
                cnt+=1


            
            
                
                
        

def pattern(word,fil,cnt):
        pat=""
        ol=[]
        c=0
        n=cnt
        wd=word
        i=0
        
        for w in word:
                if w.islower():
                        
                    word=word.replace(w,'.')
                    print word
        


        
        while(cnt<len(fil) and c==0):
            n+=1
            if re.match(word,fil[cnt]):
                pat= fil[cnt]
                print pat
                replacefunc(wd,pat)
                c=1
            cnt+=1
                

                
        if (n == len(fil)):
            if not c==1 :
                print "hi1"
                backtrack(wd,fil)

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
                                        
                                        replacefunc(key,doublew[1])
                                        print sent
                                    else:
                                        key1=find_key(doublew[0])
                                        sent=sent.replace(doublew[0],key1)
                                        del assumption[key1]
                                        replacefunc(key1,doublew[0])
                        else:
                            replacefunc(key,doublew[0])

                l = word[i]
            if word[-1] == word[-2]:
                double_w.append(word)
                double_word = open("double_letter_cons.txt", "r+")
                doublew  = double_word.read().split()
                l = word[-1]
        if double_w:
                j = 0
                replacefunc(l,doublew[j])
                j+=1

def one_letter():
    global sent
    
    for i in range(0,len(one_w)):
            sent = sent.replace(one_w[i], ow[i])
            cnt1=1
            print sent
            assumption[one_w[i]]=ow[i]



s = raw_input("Enter the ciphertext: ")

# app = Tk()
# #Code to add widgets will go here...
# app.title('Dashboard')
# app.grid()

# #top = Tkinter.Tk()
# tex = Text(master=app)
# tex.grid(row=2)

# Label(app, text="CipherText").grid(row=0)
# #Label(app, text="PlainText").grid(row=1)

# e1 = Entry(app)

# e1.grid(row=0, column=1)

# Button(app, text='Quit', command=app.quit).grid(row=3, column=0, sticky=W, pady=4)
# Button(app, text='Translate', command=result(lambda e=sent: result(e)).grid(row=3, column=1, sticky=W, pady=4)

# #mainloop()

# s=e1.get()
match = re.match(r'^[A-Za-z ]*$', s)
# err="Invalid ciphertext"
if not match:
    print("Invalid CipherText")
    #result(err)
    #mainloop()

else:
    sent = s.lower()
    words = sent.split()
    cnt1=cnt2=cnt3=cnt4=cnt3=cnt4= 0
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
    
    #open three letter noun list
    nthree_word = open("3_letter_noun.txt", "r+")
    ntrw  = nthree_word.read().split()

    #open three letter list paired with I
    ithree_word = open("I_3wrd.txt", "r+")
    itrw  = ithree_word.read().split()

    #open four letter noun list
    ifour_word = open("I_4wrd.txt", "r+")
    ifw  = ifour_word.read().split()


                    

    # for words having single letter
    # for i in range(len(words)-1):
    #     print "inloop"
    #     if len(words[i])==1:
    #         if len(words[i+1])==2:
    #             ow.reverse()

    for word in words:
            if ((len(word) == 1) and (word not in one_w)):
                    one_w.append(word)
    
    if one_w:
        one_letter()   

                                      
    # for finding pairs with I
    flag = 0
    s=sent.split()
    #for i in range(len(words)-1):
    if len(words[0])==1:
        if s[0]=='I':
            print "Yuippee"
            if (len(s[1])==2):
                for w in s[1]:
                    if w in s[0]:
                        flag+=1
                if flag==0:
                    replacefunc(s[1],'AM')
            if (len(s[1])==3):
                for w in s[1]:
                    if w in s[0]:
                        flag+=1
                if flag==1:
                    if s[1].index(s[0])==1:
                        replacefunc(s[1],'DID')
                    else:
                        key=find_key('I')
                        sent=sent.replace('I',key)
                        del assumption[key]
                        replacefunc(key,'A')

                if flag==0:
                    replacefunc(s[1],itrw[cnt3])
            if (len(s[1])==4):
                for w in s[1]:
                    if w in s[0]:
                        flag+=1
                if flag==1:
                    if s[1].index(s[0])==1:
                        if s[1][-1]==s[1][-2]: 
                            replacefunc(s[1],'WILL')
                        else:
                           replacefunc(s[1],'LIKE') 
                    else:
                        key=find_key('I')
                        sent=sent.replace('I',key)
                        del assumption[key]
                        replacefunc(key,'A')

                if flag==0:
                    replacefunc(s[1],ifw[cnt4])

    # for words having two letters
    for word in sent.split():
           if ((len(word) == 2) and (word not in two_w) and word.islower()):
                  two_w.append(word)
                  print two_w
           
    
    if two_w:
        pat_rep(two_w,tw,cnt2)           
        

    #transposition
    if not sent.isupper():
        print "yup"
        print sent
        transposition()
    
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
        if ((len(word) == 3) and (word not in three_w) and word.islower()):
            three_w.append(word)
    if three_w:
        pat_rep(three_w,trw,cnt3)
        
    # for words havin double letter
    for word in sent.split():
        if (len(word) > 2):
            double_letter(word)

    # for words having four letters
    for word in sent.split():
        if ((len(word) == 4) and (word not in four_w) and word.islower() ):
            if not word.isupper():
                four_w.append(word)
    if four_w:
        pat_rep(four_w,fw,cnt4)
        
    #main(sent)






            


                
        


  






        

