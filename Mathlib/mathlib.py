from treeClass import EqNode

priority = {
    '!' : 0,
    '^' : 1,
    '*' : 2,
    '/' : 2,
    '%' : 2,
    '+' : 3,
    '-' : 3,
}

associativity = {
    '!' : "unar",
    '^' : "RL",
    '*' : "LR",
    '/' : "LR",
    '%' : "LR",
    '+' : "LR",
    '-' : "LR",
}


def is_operator(element):
    return element in priority.keys()

def check_priority(oper1, oper2):
    if priority[oper1] > priority[oper2]:
        return 1
    elif priority[oper1] < priority[oper2]:
        return -1
    else:
        return 0


def to_postfix(infix_expr):
    oper_stack = []
    postfix_expr = []
    
    for elem in infix_expr:
        if not is_operator(elem):
            postfix_expr.append(elem)




def evaluate(input_expr):
    to_postfix(input_expr)

