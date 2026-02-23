import random as r 

ans=r.randint(1,9)
while True:
    ip=int(input("guess number from 1-9 (choose '0' to exit): "))
    if ip==0:
        print("EXITED !")
        break
    elif ip==ans:
        print("you won !!")
        print(f"random number was {ans}")
    else:
        print("saala haar gaya !")
        print(f"random number was {ans}")