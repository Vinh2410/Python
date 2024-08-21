# use loops to check even or odd numbers
while True:
    x = input()

    # add pause function to stop loop
    if x != "p":
        if int(x) == 0: 
            print("not even or odd number")
            continue
        elif int(x)%2 == 0 :
            print("Even number")
            continue
        else:
            print("Odd number")
            continue
    else:
        break

#End process loop 
print("Ket thuc chuong trinh")