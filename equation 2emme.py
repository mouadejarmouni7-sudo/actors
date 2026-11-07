a = int(input("entrer le 1er note "))
b = int(input("entrer la 2eme note"))
c = int(input("enter la 3eme note"))
D=b**2-4*a*c
if a == 0 and b == 0 and c == 0 :
    print("unique solution ")
elif a == 0 and b == 0 :
    print("erreur")
elif a == 0 :
    print("ona equation 1er degree")
else :
 if D > 0 :
    x1 , x2 = ((-b+D**0.5)/(2*a) ), ((-b-D**0.5)/(2*a) )
    print("ona deux solution x1 =",x1,"et x2 =",x2 )
 elif D == 0 :
    x1 = (-b/(2*a))
    print(f"ona une seul solution x1 = {x1}")
 else :
    print("pas du solution")
    
