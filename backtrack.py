

def backtrack(wrd):
    global sent
    kl=[]

    if len(wrd)==4:
        for w in wrd:
            if w.isupper():
                    
                    k=find_key(w)
                    kl.append(k)
                    sent=sent.replace(w,k)
                    del assumption[k]
        print sent
        print kl

def sent_check():
    for word in sent.split():
        n=0
        if word.isupper():
            if spell_check(word):
                break
            else:
                backtrack(word)
        
        print word
        for i in range(len(word)):
            if word[i] in kl:
                
                n=2
                print n
        if n==2 :
            print "back"
            print len(word)
            if(len(word)==2):

                pat_rep(word,tw,cnt2)
            if(len(word)==3):
                pat_rep(word,trw,cnt3)
            if(len(word)==4):
                
                pat_rep(word.split(),fw,cnt4)
