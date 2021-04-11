def romano_int(romano):
    romano_number = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    flag = 0
    for r in range(len(romano)):
        if r != len(romano)-1 and romano_number[romano[1]] < romano_number[romano[r+1]]:
            flag += romano_number[romano[r]] * -1
        else:
            flag += romano_number[romano[r]] 
    return (f"{romano} = {flag}")


algorismo = input(": ").upper()
print(romano_int(algorismo))

# copyright ErykTavares © 2021
            