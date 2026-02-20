hora=input()            
partes=hora.split()    
h=int(partes[0])        
m=int(partes[1])        
s=int(partes[2])        
s=s+1
if s == 60:
    s=0
    m=m+1
if m == 60:
    m=0
    h=h+1
if h==24:
    h=0
print(f"{h:02d}:{m:02d}:{s:02d}")