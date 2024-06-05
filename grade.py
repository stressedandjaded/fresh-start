score = input("Enter score: ")
fs = float(score)

try:
    if fs > 1:
        print("Value is out of range.")
    quit()
except:
    if fs >= 0.9 :
        print("A")
    elif fs >= 0.8 :
        print("B")
    elif fs >= 0.7 :
        print("c")
    elif fs >= 0.6 :
        print("D")
    elif fs < 0.6 :
        print("F")

