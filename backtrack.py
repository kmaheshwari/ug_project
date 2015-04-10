global sent
    cnt=0
    if len(wrd)==2:
        cnt=cnt2  
    if len(wrd)==3:
        cnt=cnt3
    if len(wrd)==4:
        cnt=cnt4     
    n=0
    for w in wrd:
        if (w.isupper() and n==0):
            
            
                k=find_key(w)
                print k
                wrd=wrd.replace(w,k)
                sent=sent.replace(w,k)
                print sent
                del assumption[k]
                #for wrd in sent.split():
                replacefunc(wrd,file[cnt])
                cnt=cnt+1
                n+=1
