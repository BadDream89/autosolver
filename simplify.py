

# removes all whitespaces
def remove_whitespaces(expression: str) -> str:

    return "".join(expression.split(" "))


# finds all addendums and also add minus, to negative numbers
# returns list of the members splitted by "+"
def find_members(expression: str) -> list:

    expression = expression.split("-")
    workspace = expression.copy()

    
    #print(workspace)

    is_empty_first = 0
    for key, part in enumerate(expression):

        if key == 0 and part == "":
            is_empty_first = 1
            workspace[1] = "-" + workspace[1]
        
        elif key > is_empty_first:
            workspace[key] = "-" + workspace[key]

    if workspace[-1] == "-":
        workspace.pop(-1)

    result = "+".join(workspace)
    return result.split("+")


# gets all coefficients
def divide_members(members: str):

    coefficients: list = []
    free_addendums: list = []

    for member in members:

        if "x" in member:
            coefficients.append(member.replace("x", ""))
        else:
            free_addendums.append(member)
            

    return coefficients, free_addendums

def sum_eval(obj: list) -> int:
    return sum(map(eval, obj))

def check_syntax(expression: str) -> None:

    if "=" not in expression or expression.count("=") > 1:
        error = "should be 1 '=' symbol"
        raise error

def delete_empties(obj: list):

    result = obj.copy()
    for i in range(0, obj.count("")):
        result.remove("")
    for i in range(0, obj.count(" ")):
        result.remove(" ")

    return result
    

def find_brackets(expression: str):

    pass



def simplify(equation: str):

    # removes all whitespaces
    equation = remove_whitespaces(equation)
    check_syntax(equation)

    parts: list = equation.split("=")

    left_members: list = find_members(parts[0])
    right_members: list = find_members(parts[1])

    # left part coefficients, left part free_addendums
    # right part coefficients, right part free_addendums
    lcoefs, lf_adds = divide_members(left_members)
    rcoefs, rf_adds = divide_members(right_members)

    lcoefs, lf_adds, rcoefs, rf_adds = map(delete_empties, [lcoefs, lf_adds, rcoefs, rf_adds])

    # coefficient on every side
    lcoef_sum, rcoef_sum = map(sum_eval, [lcoefs, rcoefs])

    # addendum on every side
    lf_adds_sum, rf_adds_sum = map(sum_eval, [lf_adds, rf_adds])

    # final coefficient and final addendum
    coef = lcoef_sum - rcoef_sum
    add = lf_adds_sum - rf_adds_sum

    return coef, add

