#https://www.reddit.com/r/dailyprogrammer/comments/bazy5j/20190408_challenge_377_easy_axisaligned_crate/

def main():
    print(fit1(5, 100, 6, 1))
    print(fit2(5, 5, 6, 1))
    print(fit3(12, 34, 56, 7, 8, 9))
    
def fit1(X, Y, x, y):
    return (X // x) * (Y // y)

def fit2(X, Y, x, y):
    if (X // y) * (Y // x) > (X // x) * (Y // y):
        return (X // y) * (Y // x)
    return (X // x) * (Y // y)

def fit3(X, Y, Z, x, y, z):
    positioner = []
    positioner = positioner + [(X // x) * (Y // y) * (Z // z)]
    positioner = positioner + [(X // x) * (Y // z) * (Z // y)]
    positioner = positioner + [(X // y) * (Y // x) * (Z // z)]
    positioner = positioner + [(X // y) * (Y // z) * (Z // x)]
    positioner = positioner + [(X // z) * (Y // x) * (Z // y)]
    positioner = positioner + [(X // z) * (Y // y) * (Z // x)]
    return max(positioner)
    
main()
