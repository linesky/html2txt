a:int=0
styles=True
scripts=True
triggers=False
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
        
    for ta in tags:
        ta=ta.strip()
        if counter==0:
            if len(ta)>0:
               if ta=="style" or ta=="STYLE":
                   styles=False
               if ta=="script" or ta=="SCRIPT":
                   scripts=False
               if styles and scripts:
                   if triggers:
                       print("\t",end="")
                   print(ta)
               if ta=="/style" or ta=="/STYLE":
                   styles=True
               if ta=="/script" or ta=="/SCRIPT":
                   scripts=True
        else:
            varsn=ta.split(" ")
            for varn in varsn:
                varn=varn.strip()
                if len(varn)>0:
                    if ta=="style" or ta=="STYLE":
                        styles=False
                    if ta=="script" or ta=="SCRIPT":
                        scripts=False
                    if styles and scripts: 
                        print(varn)
                    if ta=="/style" or ta=="/STYLE":
                        styles=True
                    if ta=="/script" or ta=="/SCRIPT":
                        scripts=True
                   

        
        counter+=1
        
    