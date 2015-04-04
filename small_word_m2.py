import re

def pattern(word,tw):
        for w in word:
                if w.islower():
                        word=word.replace(w,'.')
        print word
        for i in range(len(tw)):
                if re.match(word,tw[i]):
                        print tw[i]
                        return

#if a word contains double letters
def double_letter(word):
        global sent
        global assumption
        i=0
        for i in range(1,len(word)-2):
            if word[i] == word[i+1]:
                double_w.append(word)
                print double_w
                double_word = open("double_letter_vowel.txt", "r+")
                l = word[i]
        if word[-1] == word[-2]:
                double_w.append(word)
                double_word = open("double_letter_cons.txt", "r+")
                l = word[-1]
        if double_w:
                j = 0
                doublew  = double_word.read().split()
                for w,c in zip(double_w,doublew[j]):
                        sent = sent.replace(l, doublew[j])
                        print sent
                        assumption[l]=doublew[j]
                        print assumption
                j+=1
s = raw_input("Enter the ciphertext: ")
sent = s.lower()
words = sent.split()
s_w = str(min(words, key=len))
c=0
cnt1=cnt2 =cnt3= 0
assumption = {}
assertion = {}
one_w = []
two_w = []
three_w = []
four_w = []
double_w = []

for word in words:
        if ((len(word) == 1) and (word not in one_w)):
                one_w.append(word)
        if ((len(word) == 2) and (word not in two_w)):
                two_w.append(word)
        if ((len(word) == 3) and (word not in three_w)):
                three_w.append(word)
        if (len(word) > 3):
                double_letter(word)
                        
# for words having single letter

if one_w:
        one_word = open("single_word.txt", "r+")
        ow  = one_word.read().split()
        
        for i in range(0,len(one_w)):
                sent = sent.replace(one_w[i], ow[i])
                cnt1=1
                print sent
                assumption[one_w[i]]=ow[i]

# for words having two letters
#for word in sent.split():
 #      if ((len(word) == 2) and (word not in two_w)):
  #            two_w.append(word)
   #    print two_w
        

if two_w:
        j=u=0
        
        two_word = open("double_word.txt", "r+")
        tw  = two_word.read().split()
        print tw
        tr=tw[cnt2]
        print tr
        for word in two_w:
                
                for t in word:
                        if t.isupper():
                                print "Hello"
                                pattern(word,tw)
                                u+=1
        
        if u==0:
                for w,c in zip(word,tw[j]):
                        
                        print c
                        sent = sent.replace(w,c)

                        print sent
                        assumption[w]=c
                        print assumption
                
                
                j+=1
        cnt2=1
        
# for words having three letters

if three_w:
        j=u=0
        
        three_word = open("three_word.txt", "r+")
        trw  = three_word.read().split()

        for word in three_w:
                
                for t in word:
                        if t.isupper():
                                pattern(word,trw)
                                u+=1
        
        if u==0:
                for w,c in zip(word,trw[j]):
                        
                        
                        sent = sent.replace(w,c)

                        print sent
                        assumption[w]=c
                        print assumption
                
                
                j+=1
        cnt3=1

#ERROR WITH CASE:
       # SK G EEK
                
        


  






        

