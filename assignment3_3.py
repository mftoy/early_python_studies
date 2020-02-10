score = input("Enter Score: ")
try:
    sc=float(score)
except:
    print("Please Enter a Numeric Input")
    quit()

if sc > 1.0:
    print("Out of Range Score")
    quit()

elif sc < 0:
    print("Out of Range Score")
    quit()

elif sc >= 0.9 :
    print ("A")
    quit()

elif sc >= 0.8 :
    print ("B")
    quit()

elif sc >= 0.7 :
    print ("C")
    quit()

elif sc >= 0.6 :
    print ("D")
    quit()

elif sc < 0.6 :
    print ("F")
    quit()
