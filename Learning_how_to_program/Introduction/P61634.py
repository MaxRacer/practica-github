anio=int(input())
if anio % 100==0:      
    if (anio // 100) % 4 == 0:
        print("YES")
    else:
        print("NO")
else:  
    if anio % 4==0:
        print("YES")
    else:
        print("NO")