from simplify import simplify

# solver for simplified equation
def solve(coef: int, add: int) -> int:

    return -(add / coef)

def main():

    eq = "20x + 10 = 0"
    coef, add = simplify(eq)

    print(f"{coef}x + {add} = 0")
    answer = solve(coef, add)
    print(answer)


if __name__ == "__main__":

    while True:
        main()
        break