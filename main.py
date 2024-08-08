from simplify import simplify


def main():

    eq = input("equation: ")
    simplified = simplify(eq)
    
    print(simplified)



if __name__ == "__main__":

    while True:
        main()