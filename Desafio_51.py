def romano_int(romano):
    romano_number = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    flag = 0
    for r in range(len(romano)):
        atual = romano[r]

        if len(romano) == 1:
            flag += romano_number[atual]
        elif len(romano) > 1 and r+1 != len(romano) :
            prox = romano[r+1]
            if romano_number[prox] > romano_number[atual]:
                flag -= romano_number[atual]
            elif romano_number[atual] == romano_number[prox]:
                flag += romano_number[atual]
            else:
                flag += romano_number[atual]
        else:
            prox = atual
            if romano_number[prox] > romano_number[atual]:
                flag -= romano_number[atual]
            elif romano_number[atual] == romano_number[prox]:
                flag += romano_number[atual]
            else: 
                flag += romano_number[atual]
    
    return (str(romano) + " = " + str(flag))


algorismo = input(": ").upper()
print(romano_int(algorismo))

# copyright ErykTavares © 2021
            

