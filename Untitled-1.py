S = 0 
for i in range (1,9) :
    print(f"ona i est {i}") 
    N = int(input()) 
    if N < 0 :
        break
    S = S + i 
print(S)