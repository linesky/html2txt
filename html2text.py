a:int=0
styles=True
scripts=True
triggers=False
triggers2=False
filename="my.html"
print("\x1bc\x1b[41;30m")
f1=open(filename,"r")
files=f1.read()
f1.close()
splits=files.split(">")
counter=0
for n in splits:
    n=n.replace("\n","")
    n=n.replace("\r","")
    tags=n.split("<")
    triggers=False
    counter=0
    if len(tags)==2 and len(tags[0])>0:
        triggers=True
        triggers2=True
    xx=True    
    for ta in tags:
        ta=ta.strip()
        if counter>0:
            varsn=ta.split(" ")
            for varn in varsn:
                varn=varn.strip()
                if len(varn)>0:
                    if varn=="style" or varn=="STYLE":
                        styles=False
                    if varn=="script" or varn=="SCRIPT":
                        scripts=False
                    if styles and scripts: 
                        xx=False
                    if varn=="/style" or varn=="/STYLE":
                        styles=True
                    if varn=="/script" or varn=="/SCRIPT":
                        scripts=True
                    if varn=="br" or varn=="BR" or varn=="p" or varn=="P" or varn=="/p" or varn=="/P":
                        print("")
                    if varn=="a" or varn=="A":
                        
                        triggers2=False
                    if triggers2==False and (varn.find("href")>-1 or varn.find("HREF")>-1):
                        hrefs=varn.split("=")
                        if len(hrefs)>1:
                            print(hrefs[1],end="")
                    
        else:
                   
            if len(ta)>0:
               if ta=="style" or ta=="STYLE":
                   styles=False
               if ta=="script" or ta=="SCRIPT":
                   scripts=False
               if styles and scripts:
                   if ta=="br" or ta=="BR" or ta=="p" or ta=="P" or ta=="/p" or ta=="/P":
                       print("")
                   if varn=="a" or varn=="A":
                        
                       triggers2=False



                   if triggers:
                       print(" ",end="")
                   
                   print(ta,end="")
               if ta=="/style" or ta=="/STYLE":
                   styles=True
               if ta=="/script" or ta=="/SCRIPT":
                   scripts=True

        
        counter+=1
        
    