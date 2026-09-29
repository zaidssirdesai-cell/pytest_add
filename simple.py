def simpleint(p,t,r):
    return p*t*r/100

if __name__ == "__main__":
    p=float(input("Enter the principle:"))
    t=float(input("Enter the time:"))
    r=float(input("Enter the rate:"))

    print("Simple interest is :", simpleint(p,t,r))
    