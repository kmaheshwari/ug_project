#
import re
import grammar_test
#from grammar_test import main 
#from tkinter import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import string
import sys
import Dashboard

cnt1=cnt2=cnt3=cnt4=cnti3=cnti4=cntn3=cntn4=s2cnt=e2cnt= 0
s3cnt=e3cnt=s4cnt=e4cnt=0
assumption = {}
assertion = {}
one_w = []
two_w = []
three_w = []
four_w = []
double_w = []
trans_cnt=0

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

#open ending four letter list 
e_4wrd = open("e_4wrd.txt", "r+")
efw  = e_4wrd.read().split()

#open ending three letter list 
e_3wrd = open("e_3wrd.txt", "r+")
etrw  = e_3wrd.read().split()

#open ending two letter list 
e_2wrd = open("e_2wrd.txt", "r+")
etw  = e_2wrd.read().split()


#open starting four letter list 
st_4wrd = open("st_4wrd.txt", "r+")
sfw  = st_4wrd.read().split()

#open starting three letter list 
st_3wrd = open("st_3wrd.txt", "r+")
strw  = st_3wrd.read().split()

#open starting two letter list 
st_2wrd = open("st_2wrd.txt", "r+")
stw  = st_2wrd.read().split()

class MainDialog(QDialog, Dashboard.Ui_Form):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.translate.clicked.connect(self.button_click)
        #self.connect(self.translate, SIGNAL("clicked()"),self.main)
        #self.main()

    def button_click(self):
        global sent,words,a_sent, three_w, four_w, double_w, trans_cnt
        global cnt1, cnt2, cnt3, cnt4, cnti3, cnti4, cntn3, cntn4, s2cnt, e2cnt
        global s3cnt,e3cnt, s4cnt, e4cnt, assumption, one_w,two_w
        s = self.cipher.text()
        sent = s.lower()
        match = re.match(r'^[A-Za-z ]*$', s)
        
        if not match:
            self.result.append("Invalid CipherText")
            #self.result.append("Invalid CipherText")
           
        else:
            sent = s.lower()
            words = sent.split()
            a_sent=sent
            self.main()
            cnt1=cnt2=cnt3=cnt4=cnti3=cnti4=cntn3=cntn4=s2cnt=e2cnt= 0
            s3cnt=e3cnt=s4cnt=e4cnt=0
            assumption = {}
            assertion = {}
            one_w = []
            two_w = []
            three_w = []
            four_w = []
            double_w = []
            trans_cnt=0
    
    def main(self):

        global sent,trans_cnt,words,trans_cnt,a_sent,assumption
        global one_w, two_w, three_w, four_w, double_w 
        t_d = 0
        
        final_cnt = 0
        #To check whether sentence is correct after backtrack or not
        for word in sent.split():
            if word.isupper() and self.spell_check(word)==True:
                final_cnt+=1
        
        if final_cnt != len(sent.split()):
            #Find one-letter word in cipher sentence
            for word in words:
                    if ((len(word) == 1) and (word not in one_w)):
                            one_w.append(word)
            
            #if found one-letter word then make a list 'one_w and append all the words'
            if one_w:
                self.one_letter()
                a_sent = sent #store sent before transposition
                
                #do transposition
                if(trans_cnt<1):
                    t1_done=self.transposition()
                    trans_cnt+=1
                    if t1_done:
                        status=self.trans_status()
                        if not status:
                            t_d=1
                        else:
                            self.result.append(sent)
                    else:
                        t_d=1

            #if cipher sentence is not transposition ciper or 
            #there is no one-letter word in cipher seentence
            if (t_d==1 or len(one_w)==0) :
                

                # for finding pairs possible with I
                flag = 0
                s=sent.split()
                
                if len(words[0])==1:
                    if s[0]=='I':
                        
                        if (len(s[1])==2):
                            for w in s[1]:
                                if w in s[0]:
                                    flag+=1
                            if flag==0:
                                self.replacefunc(s[1],'AM')
                        if (len(s[1])==3):
                            for w in s[1]:
                                if w in s[0]:
                                    flag+=1
                            if flag==1:
                                if s[1].index(s[0])==1:
                                    self.replacefunc(s[1],'DID')
                                else:
                                    key=self.find_key('I')
                                    sent=sent.replace('I',key)
                                    del assumption[key]
                                    self.replacefunc(key,'A')

                            if flag==0:
                                self.replacefunc(s[1],itrw[cnti3])
                        if (len(s[1])==4):
                            for w in s[1]:
                                if w in s[0]:
                                    flag+=1
                            if flag==1:
                                if s[1].index(s[0])==1:
                                    if s[1][-1]==s[1][-2]: 
                                        self.replacefunc(s[1],'WILL')
                                    else:
                                       self.replacefunc(s[1],'LIKE') 
                                else:
                                    key=self.find_key('I')
                                    sent=sent.replace('I',key)
                                    del assumption[key]
                                    self.replacefunc(key,'A')

                            if flag==0:
                                replacefunc(s[1],ifw[cnti4])

                # for words having two letters
                for word in sent.split():
                       if ((len(word) == 2) and (word not in two_w) ):
                            if not word.isupper():
                                two_w.append(word)
                                
                       
                #creation of list two_w containing two-letter words
                if two_w:
                    self.pat_rep(two_w,tw,cnt2) 
                    a_sent = sent 
                    if not one_w and trans_cnt<1:
                        t_done=self.transposition()
                        trans_cnt+=1
                        if t_done:
                            status=self.trans_status()
                            if not status:
                                t_d=1
                            else:
                                self.result.append(sent)
                        else:
                            t_d=1


                #checking A-noun pair
                s1 = sent.split()
                nf=nt=[]
                for i in range(len(s1)-1):
                    if len(s1[i])==1:
                        if s1[i]=='A':
                            
                            if len(s1[i+1])==3:
                                nt.append(s1[i+1])
                                self.pat_rep(nt,ntrw,cntn3)
                            if len(s1[i+1])==4:
                                nf.append(s1[i+1])
                                self.pat_rep(nf,nfw,cntn4)
                if t_d==1 :
                    
                    
                    self.result.append(sent)
                    # for words having three letters
                    for word in sent.split():
                        if ((len(word) == 3) and (word not in three_w)):
                            if not word.isupper():
                                three_w.append(word)
                    if three_w:
                        self.pat_rep(three_w,trw,cnt3)
                        
                    # for words havin double letter
                    for word in sent.split():
                        if (len(word) > 2):
                            self.double_letter(word)

                    # for words having four letters
                    for word in sent.split():
                        if ((len(word) == 4) and (word not in four_w) ):
                            if not word.isupper():
                                four_w.append(word)
                    if four_w:
                        self.pat_rep(four_w,fw,cnt4)
                        
        else:
            grammar_test.main(sent)
            self.result.append("Final answer")
            self.result.append(sent)


    def find_key(self,value):
        global assumption
        for k,v in list(assumption.items()):
            if v== value:
                return k

    def spell_check(self,word):
        #checks the spelling of the word and returns true if the spelling is correct
        if ((len(word) == 2)):
            #if two-letter word
            if word in tw:
                return True
        if ((len(word) == 3)):
            #if three-letter word
            if word in trw:
                return True
        if ((len(word) == 4)):
            #if four-letter word
            if word in fw:
                return True
        if ((len(word) > 4) ):
            return True
        return False

    def replacefunc(self,word,file_word):
        #replaces the word passed with a word from file
            global sent,assumption
            for w,c in zip(word,file_word):
                if w.islower():
                    if c not in list(assumption.values()):
                        sent = sent.replace(w, c)
                        self.result.append(sent)
                        assumption[w]=c
                        self.result.append(str(assumption))
                    
    def transposition(self):
        #checks if 
        global sent,assumption
        self.result.append("transposition")
        upper = []
        p = c =0
        for words in sent.split():
            for w in words:
                if w.isupper():
                    key = self.find_key(w)
                    
                    p = ord(w.lower())
                    c = ord(key)
                    if p<c:
                        p=p+26

                    upper.append(c-p)
                    

                    
                    
        upper = list(set(upper))
        
        if len(upper)==1:
            for words in sent.split():
                for w in words: 
                    if w.islower():
                        pr = (ord(w) - upper[0])
                        if pr < 97:
                            pr = ord(w) + 26 - upper[0]
                        if pr > 122:
                            pr = ord(w) - 26 - upper[0]
                        pr = (chr(pr)).upper()
                        sent = sent.replace(w,pr)
                        assumption[w] = pr
                        self.result.append(str(assumption))
                        self.result.append(sent)
            #to check whether transposition is done or not
            return True
        return False


    #for backtrack
    def backtrack(self,wrd):
        #wrd: word for which no pattern was found
        global sent, assumption, one_w, two_w, three_w, four_w, double_w 
        k=key=""
        kl=[]
        
        self.result.append("backtrack started")
        for w in wrd:
            if w.isupper():
                 
                 k1=self.find_key(w)
                 self.result.append(str(k1))
                 kl.append(k1)
                 sent=sent.replace(w,k1)
                 del assumption[k1]
        
        self.result.append(str(assumption))
        self.result.append(sent)
        for i in range(len(kl)): 
            for char in sent.split():
                if kl[i] in char:
                    for wr in char:
                        if wr.isupper():
                            key=self.find_key(wr)
                            
                            kl.append(key)
                            if key != None:
                                sent=sent.replace(wr,key)
                                
                                del assumption[key]
        self.result.append(sent)
        
        
        one_w = []
        two_w = []
        three_w = []
        four_w = []
        double_w = []
        self.result.append("after backtrack")
        
        self.result.append(sent)
        self.main()
            
              

    def trans_status(self):
        global sent
        for w in sent.split():
            if len(w) >1:
                
                if not self.spell_check(w):
                    self.revert_trans()
                    return False
        return True            


    def pat_rep(self,lst,prfil,cnt):
    	#lst:list of specific words(i.e 2-letter, 3-letter etc) in the sentence containing cipher letters.
    	#fil:text file of containing 2-letter,3-letter etc plain-letter words corresponding to list.
    	#cnt:counter to mention the position in the file
    	#pat_rep function replaces the words from list with suitable word from file according to condition.
        global cnt1, cnt2, cnt3, cnt4, cnti3, cnti4, cntn3, cntn4, s2cnt, e2cnt, s3cnt, e3cnt, s4cnt, e4cnt 
        global assumption,sent
        lfil=prfil
        self.result.append(str(prfil))
        self.result.append(str(lst))
        lcnt=cnt
        j=0
        
        for word in lst:
            self.result.append("inside pat_rep")
            
            prfil = lfil
            self.result.append("this is")
            self.result.append(str(prfil))
            i = lst.index(word)		#index of word in list
            cnt_cap=0    			#counter for capital letter in a word
            for t in word:
            	#if a letter in word of list is already in assumption replace the cipher-letter with 
            	#corresponding plainletter entry in assumption
                if t in assumption:		
                    word=word.replace(t,assumption[t])
                    
                    
                    t=t.replace(t,assumption[t])
                #if a letter in word is capital increase counter
                if t.isupper():
                    cnt_cap+=1
                    
           
            
            j = (sent.split()).index(word)		#index of word in original sentence which is modified
            

            if len(word)==2:
                if j==0:
                    prfil = stw
                    cnt=s2cnt
                elif j==len(sent.split())-1:
                    prfil = etw
                    cnt=e2cnt
                # else:
                #     fil = lfil
                #     cnt=lcnt
                #     self.result.append lfil

            if len(word) == 3 and prfil!=ntrw:
                
                #if a 3-letter word is in starting/ending position then replace the file with another file containing 
                #all possible 3-letter words which can come at starting or ending
                if j==0:
                    prfil = strw
                    cnt=s3cnt
                elif j==len(sent.split())-1:
                    prfil = etrw
                    cnt=e3cnt
                # else:
                #     fil = lfil
                #     cnt=lcnt
            if len(word) == 4 and prfil!=nfw:
            	#if a 4-letter word is in starting/ending position then replace the file with another file containing 
                #all possible 4-letter words which can come at starting or ending
                
                if j==0:
                    prfil = sfw
                    cnt=s4cnt
                elif j==len(sent.split())-1:
                    prfil = efw
                    cnt=e4cnt
                # else:
                #     fil = lfil
                #     cnt=lcnt
            lst[i] = word
            
            #if the word contains any capital letter then call pattern matching
            if cnt_cap>=1 and cnt_cap<len(word):
                
                self.pattern(word,prfil,cnt)
            #if the word does not contain any capital letter then replace the word with word in file 
            if cnt_cap==0:
                
                #start from the position of counter in the file
                while (cnt<len(prfil)):
                    c=0
                    #if the letter of word from file is already in assumption increase the counter to 
                    #replace with the next word else replace with the same word
                    for f in prfil[cnt]:
                        if f in list(assumption.values()):
                            c=1
                    if c>0:
                        cnt+=1
                    if c==0:
                        self.replacefunc(word,prfil[cnt])
                        cnt+=1
                        break
            if len(word) == 2:
                cnt2 = cnt
            if len(word) == 3:
                cnt3 = cnt
            if len(word) == 4:
                cnt4 = cnt
    def revert_trans(self):
        global sent,a_sent,assumption
        k=[] 
        v=[]

        sent = a_sent
        self.result.append("revert")
        self.result.append(sent)
        for w in sent:
            if w.isupper():
                k.append((self.find_key(w)))
                v.append(w)
        
        assumption.clear()
        for i in range(len(k)):
            assumption[k[i]]=v[i]
        #assumption = a_assump
        
         
                
                    
                    
    def pattern(self,word,fil,cnt):
            #word: word from sentence containing a capital letter
            #fil: corresponding file(e.g 4_word file for 4-letter word)
            #cnt: counter that mentions position in the file
            #pattern function replaces the words from list with suitable word from file according to conditions if a pattern is matched
            global cnt2,cnt4
            self.result.append("pattern")
            pat=""
            c=0
            n=cnt
            wd=word
            i=0
            mtch = []
            j=[]
            #check if a letter occurs more than once in the word(for e.g in THAT, T occurs twice)
            for w in word:
                    wc = 0
                    if w.islower():
                        wc = word.count(w)
                        
                        if wc>1:
                            
                            j.append((word.index(w)))   #append both the index of occurrence
                            fil = mtch          #replace the file with another list
            
            #append all the words from file in which a letter occur more than once
            if fil == mtch:
                for wrd in fil:
                    if wrd[j[0]] == wrd[j[1]]:
                        fil.append(wrd)
                
            #replace all the small letters in the word with "." for pattern matching
            for w in word:
                    wc = 0
                    if w.islower():
                        word=word.replace(w,'.')
            self.result.append(word)
                        
                    
            
            # while( c==0):
            #     for i in range(cnt, (len(fil)-1)):

            #         self.result.append "inside"
                    
            #         if re.match(word,fil[cnt]):
            #             self.result.append "match"
            #             pat = fil[cnt]
            #             self.result.append pat
            #             replacefunc(wd,pat)
            #             c=1
            #             break
            #         cnt+=1
                          
            # if (cnt == len(fil)):
            #     if not c==1:
            #         self.result.append "hi1"
            #         backtrack(wd)
            #match the word with every word from file and replace with the first pattern match found. 
            for ch in fil:
                n+=1    
                self.result.append(str(n))
                if re.match(word,ch):
                    pat= ch
                    self.result.append(pat)
                    self.replacefunc(wd,pat)
                    c=1     #implies pattern is found  
                    break
                cnt+=1
                self.result.append(str(cnt))
            
            #if no pattern is matched call backtrack
            if (n == len(fil)):
                if not c:
                    
                    self.backtrack(wd)
            if sent.isupper():
                self.main()



    #if a word contains double letters
    def double_letter(self,word):
            global sent
            global assumption
            global double_word
            global l,doublew,key
            i=0
            for i in range(1,len(word)-2):
                if word[i] == word[i+1]:
                     
                    double_w.append(word)
                    
                    double_word = open("double_letter_vowel.txt", "r+")
                    doublew  = double_word.read().split()
                    if (word[i].isupper()):
                        if word[i] not in doublew:
                            key=self.find_key(word[i])
                            
                            sent=sent.replace(word[i],key)
                            self.result.append(sent)
                            del assumption[key]
                            self.result.append(assumption)
                            if doublew[0] in list(assumption.values()):
                                for word in sent.split():
                                    if doublew[0] in word:
                                        if spell_check(word):
                                            
                                            self.replacefunc(key,doublew[1])
                                            
                                        else:
                                            key1=self.find_key(doublew[0])
                                            sent=sent.replace(doublew[0],key1)
                                            del assumption[key1]
                                            self.replacefunc(key1,doublew[0])
                            else:
                                self.replacefunc(key,doublew[0])

                    l = word[i]
                if word[-1] == word[-2]:
                    double_w.append(word)
                    double_word = open("double_letter_cons.txt", "r+")
                    doublew  = double_word.read().split()
                    l = word[-1]
            if double_w:
                    j = 0
                    self.replacefunc(l,doublew[j])
                    j+=1

    def one_letter(self):
        global sent
        self.result.append(str(len(one_w)))
        for i in range(0,len(one_w)):
                sent = sent.replace(one_w[i], ow[i])
                cnt1=1
                self.result.append(sent)
                assumption[one_w[i]]=ow[i]

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


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
                    

        






            


                
        


  






        

