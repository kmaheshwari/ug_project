s = raw_input("Enter the ciphertext: ")
sent= s.lower()
words = sent.split()
s_w = str(min(words, key=len))
c=0
cnt1=cnt2 = 0
assumption = {}
assertion = {}
one_w = []
two_w = []
three_w = []
four_w = []
for word in words:
	if ((len(word) == 1) and (word not in one_w)):
		one_w.append(word)
	if ((len(word) == 2) and (word not in two_w)):
		two_w.append(word)
	if ((len(word) == 3) and (word not in three_w)):
		three_w.append(word)

# for words having single letter
if one_w:
	one_word = open("single_word.txt", "r+")
	ow  = one_word.read().split()
	
	for i in range(0,len(one_w)):
		sent = sent.replace(one_w[i], ow[i])
		cnt1=1
		print sent
		assumption[one_w[i]]=ow[i]
		
if two_w:

	j=u=0
	
	two_word = open("double_word.txt", "r+")
	tw  = two_word.read().split()
	print tw
	for word in two_w:
		
		for t in word:
			if t.isupper():
				pattern(word)
				u+=1
        
        if u==0:
	        for w,c in zip(word,tw[j]):
	        	
	        	print c
	        	sent = sent.replace(w,c)

	        	print sent
	        	assumption[w]=c
			print assumption
		
		
		j+=1
	cnt=1
	

if three_w:
	j=u=0
	
	three_word = open("three_word.txt", "r+")
	trw  = three_word.read().split()
	
	for word in three_w:
		
		for t in word:
			if t.isupper():
				pattern(word)
				u+=1
        
        if u==0:
	        for w,c in zip(word,trw[j]):
	        	
	        	
	        	sent = sent.replace(w,c)

	        	print sent
	        	assumption[w]=c
			print assumption
		
		
		j+=1
	cnt2=1
	

def pattern(word):
	print word
	
# if len(s_w) == 3:
# 	one_word = open("single_word.txt", "r+")
# 	ow  = one_word.read().split()
# 	print ow
# 	sent = sent.replace(s_w, ow[0])
# 	cnt=1
# 	print sent
# 	assumption[s_w]=ow[0]




	






	

