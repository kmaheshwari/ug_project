#
import re
#import grammar_test
#from grammar_test import main 
from Tkinter import *
import string

# def result(strng):

#     tex.insert(END,strng)
#     tex.grid()
      


# def show_entry_fields():
#     print("CipherText: %s\nPlainText: %s" % (e1.get(), e2.get()))
#     e1.delete(0,END)
#     e2.delete(0,END)


def main():
    global sent,trans_cnt,a_sent,main_cnt,one_w,two_w,three_w,four_w
    t_d = 0
    t_nd=0
    main_cnt=main_cnt+1
    if main_cnt>1:
        one_w=[]
        two_w=[]
        three_w=[]
        four_w=[]
    print one_w
    print two_w
    print sent
    print "inside main"
    final_cnt = 0

    for word in sent.split():
        if word.isupper() and spell_check(word)==True:
            final_cnt+=1
    if final_cnt != len(sent.split()):
        for word in words:
                if (len(word) == 1) :
                    if word.islower():
                        one_w.append(word)
        print "1 wrd"
        print one_w
        if one_w:
            one_letter()
            a_sent = sent #store sent before transposition
            
            if(trans_cnt<1):
                t1_done=transposition()
                trans_cnt+=1
                if t1_done:
                    status=trans_status()
                    if not status:
                        t_d=1
                    else:
                        print sent
                else:
                    t_d=1


        
        if (t_d==1 or len(one_w)==0 or trans_cnt>0) :
            

            # for finding pairs with I
            flag = 0
            s=sent.split()
            #for i in range(len(words)-1):
            if len(words[0])==1:
                if s[0]=='I':
                    
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
                            replacefunc(s[1],itrw[cnti3])
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
                            replacefunc(s[1],ifw[cnti4])

            # for words having two letters
            for word in sent.split():
                   if (len(word) == 2) :
                        if not word.isupper():
                            two_w.append(word)
                            
                   
            print "yes"
            print two_w
            if two_w:
                pat_rep(two_w,tw,cnt2) 
                a_sent = sent 
                if not one_w and trans_cnt<1:
                    t_done=transposition()
                    trans_cnt+=1
                    if t_done:
                        status=trans_status()
                        if not status:
                            t_d=1
                        else:
                            print sent
                    else:
                        t_d=1
                


                

            #transposition
            # if not sent.isupper():
            #     print "yup"
            #     print sent
            #     transposition()
            
            #checking A-noun pair
            s1 = sent.split()
            nf=nt=[]
            for i in range(len(s1)-1):
                if len(s1[i])==1:
                    if s1[i]=='A':
                        
                        if len(s1[i+1])==3:
                            nt.append(s1[i+1])
                            pat_rep(nt,ntrw,cntn3)
                        if len(s1[i+1])==4:
                            nf.append(s1[i+1])
                            pat_rep(nf,nfw,cntn4)
            if (t_d==1 or trans_cnt>0 ) :
                
                
                print sent
                # for words having three letters
                for word in sent.split():
                    if ((len(word) == 3) and (word not in three_w)):
                        if not word.isupper():
                            three_w.append(word)
                if three_w:
                    pat_rep(three_w,trw,cnt3)
                    
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
                    pat_rep(four_w,fw,cnt4)
                    
    else:
    #     grammar_test.main(sent)
        print "Final answer"
        print sent


def find_key(value):
    for k,v in assumption.items():
        if v== value:
            return k

def spell_check(word):
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

def replacefunc(word,file_word):
    #replaces the word passed with a word from file
        global sent
        for w,c in zip(word,file_word):
            if w.islower():
                if c not in assumption.values():
                    sent = sent.replace(w, c)
                    print sent
                    assumption[w]=c
                    print assumption
                
def transposition():
    #checks if 
    global sent
    print "transposition"
    upper = []
    p = c =0
    for words in sent.split():
        for w in words:
            if w.isupper():
                key = find_key(w)
                
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
                    print assumption
                    print sent
        #to check whether transposition is done or not
        return True
    return False


#for backtrack
def backtrack(wrd):
    #wrd: word for which no pattern was found
    global sent,two_w,b_done
    k=key=""
    kl=[]
    
    print "backtrack started"
    for w in wrd:
        if w.isupper():
            for char in sent.split():
                if w in char:
                    if char.isupper():
                        for wr in char:
                            
                            key=find_key(wr)
                            
                            kl.append(key)
                            if key != None:
                                sent=sent.replace(wr,key)
                                
                                del assumption[key]
             # k1=find_key(w)
             # kl.append(k1)
             # sent=sent.replace(w,k1)
             # del assumption[k1]
    
    print assumption
    print sent
    # for i in range(len(kl)): 
    #     for char in sent.split():
    #         if kl[i] in char:
    #             for wr in char:
    #                 if wr.isupper():
    #                     key=find_key(wr)
                        
    #                     kl.append(key)
    #                     if key != None:
    #                         sent=sent.replace(wr,key)
                            
    #                         del assumption[key]
    print sent
    
    
    one_w = []
    two_w = []
    three_w = []
    four_w = []
    double_w = []
    print "after backtrack"
    
    print sent
    b_done=1
    #main()

    # j = True

    # while(j):
    #  c=0
    #  for i in range(len(s)):
    #     #if any word which is already replaced in sentence does not have correct spelling 
    #     #then backtrack is called again on that word else counter is increased for every corerct word.
    #      if s[i].isupper():
    #          if not spell_check(s[i]):
    #              si = s[i]
    #              #i=0
    #              c=0
    #              backtrack(si)
    #          else:
    #              c+=1
    #     #if every letter of the word in sentence is not replaced then call pat_rep function for it.
    #      else:
    #          if(len(s[i])==2):
    #              pat_rep(s[i].split(),tw,cnt2)
    #          if(len(s[i])==3):
    #              pat_rep(s[i].split(),trw,cnt3)
    #          if(len(s[i])==4):
                
    #              pat_rep(s[i].split(),fw,cnt4)
    #  #if all the words of the sentence are correct then terminate the while loop to end backtrack.
    #  if c == len(s):
    #      j = False

    
            

def trans_status():
    global sent
    for w in sent.split():
        if len(w) >1:
            
            if not spell_check(w):
                revert_trans()
                return False
    return True            


def pat_rep(lst,prfil,cnt):
	#lst:list of specific words(i.e 2-letter, 3-letter etc) in the sentence containing cipher letters.
	#fil:text file of containing 2-letter,3-letter etc plain-letter words corresponding to list.
	#cnt:counter to mention the position in the file
	#pat_rep function replaces the words from list with suitable word from file according to condition.
    global cnt2,cnt4 ,b_done
    lfil=prfil
    print prfil
    print lst
    lcnt=cnt
    
    j=0
    


    
    
    for word in lst:

        ind=lst.index(word)
        print "inside pat_rep"
        lst_len=len(lst[0])
        lst=[]
        
        for strng in sent.split():
            if len(strng)==lst_len :
                if not strng.isupper():
                    lst.append(strng)
                elif sent.isupper():
                    exit()
                else:
                    ind-=1
        word=lst[ind]

        prfil = lfil
        print "this is"
        print lst
        print prfil
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
            #     print lfil

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
            
            pattern(word,prfil,cnt)
        #if the word does not contain any capital letter then replace the word with word in file 
        if cnt_cap==0:
            
            #start from the position of counter in the file
            while (cnt<len(prfil)):
                c=0
                #if the letter of word from file is already in assumption increase the counter to 
                #replace with the next word else replace with the same word
                for f in prfil[cnt]:
                    if f in assumption.values():
                        c=1
                if c>0:
                    cnt+=1
                if c==0:
                    replacefunc(word,prfil[cnt])
                    cnt+=1
                    break
        if len(word) == 2:
            cnt2 = cnt
        if len(word) == 3:
            cnt3 = cnt
        if len(word) == 4:
            cnt4 = cnt
        

def revert_trans():
    global sent,a_sent
    k=[] 
    v=[]

    sent = a_sent
    print "revert"
    print sent
    for w in sent:
        if w.isupper():
            k.append((find_key(w)))
            v.append(w)
    
    assumption.clear()
    for i in range(len(k)):
        assumption[k[i]]=v[i]
    #assumption = a_assump
    
     
            
                
                
def pattern(word,fil,cnt):
        #word: word from sentence containing a capital letter
        #fil: corresponding file(e.g 4_word file for 4-letter word)
        #cnt: counter that mentions position in the file
        #pattern function replaces the words from list with suitable word from file according to conditions if a pattern is matched
        global cnt2,cnt4
        print "pattern"
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
        print word
                    
                
        
        # while( c==0):
        #     for i in range(cnt, (len(fil)-1)):

        #         print "inside"
                
        #         if re.match(word,fil[cnt]):
        #             print "match"
        #             pat = fil[cnt]
        #             print pat
        #             replacefunc(wd,pat)
        #             c=1
        #             break
        #         cnt+=1
                      
        # if (cnt == len(fil)):
        #     if not c==1:
        #         print "hi1"
        #         backtrack(wd)
        #match the word with every word from file and replace with the first pattern match found. 
        for ch in fil:
            n+=1    
            print n
            if re.match(word,ch):
                pat= ch
                print pat
                replacefunc(wd,pat)
                c=1     #implies pattern is found  
                break
            cnt+=1
            print cnt
        
        #if no pattern is matched call backtrack
        if (n == len(fil)):
            if not c:
                
                backtrack(wd)
                
        if sent.isupper():
            main()



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
                
                double_word = open("double_letter_vowel.txt", "r+")
                doublew  = double_word.read().split()
                if (word[i].isupper()):
                    if word[i] not in doublew:
                        key=find_key(word[i])
                        
                        sent=sent.replace(word[i],key)
                        print sent
                        del assumption[key]
                        print assumption
                        if doublew[0] in assumption.values():
                            for word in sent.split():
                                if doublew[0] in word:
                                    if spell_check(word):
                                        
                                        replacefunc(key,doublew[1])
                                        
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
    trans_cnt=0
    sent = s.lower()
    words = sent.split()
    main_cnt=0
    b_done=0
    cnt1=cnt2=cnt3=cnt4=cnti3=cnti4=cntn3=cntn4=s2cnt=e2cnt= 0
    s3cnt=e3cnt=s4cnt=e4cnt=0
    assumption = {}
    assertion = {}
    one_w = []
    two_w = []
    three_w = []
    four_w = []
    double_w = []
    a_sent=sent

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

    
    while(not sent.isupper()):
        main()
    else:
        print "Final sententence"
        print sent
        exit()

                    

        






            


                
        


  






        

