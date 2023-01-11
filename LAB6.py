#KNOWLEDGE BASE USING PREPOSITIONAL LOGIC
TFcombo=[(False, False, False), (False, False, True), (False,True, False), (True, False, False), (False, True, True), (True, True, False), (True,False, True), (True, True, True)]
variable={'a':0,'b':1, 'c':2}
kb=''
q=''
priority={'~':3,'^':2,'v':1,}

def input_logic():
    global kb, q
    kb = input("Input logic: ")
    q = input("Input query: ")
    
def entailment():
    global kb, q
    print('kb :','alpha')
    for comb in TFcombo:
        s = evaluatePostfix(toPostfix(kb), comb)
        f = evaluatePostfix(toPostfix(q), comb)
        print(s ,':', f)
        if s and not f:
            return False
    return True

def isOperand(c):
    return c.isalpha() and c!='v'

def isLeftParanthesis(c):
    return c == '('

def isRightParanthesis(c):
    return c == ')'

def isEmpty(stack):
    return len(stack) == 0

def peek(stack):
    return stack[-1]

def priorityPrecedence(c1, c2):
    try:
        return priority[c1]<=priority[c2]
    except KeyError:
        return False
    
def toPostfix(infix):
    stack = []
    postfix = ''
    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if isLeftParanthesis(c):
                stack.append(c)
            elif isRightParanthesis(c):
                operator = stack.pop()
                while not isLeftParanthesis(operator):
                    postfix += operator
                    operator = stack.pop()
            else:
                while (not isEmpty(stack)) and priorityPrecedence(c, peek(stack)):
                    postfix += stack.pop()
                stack.append(c)
    while (not isEmpty(stack)):
        postfix += stack.pop()
    
    return postfix

def evaluatePostfix(exp, comb):
    stack = []
    for i in exp:
        if isOperand(i):
            stack.append(comb[variable[i]])
        elif i == '~':
            val1 = stack.pop()
            stack.append(not val1)
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(_eval(i,val2,val1))
        return stack.pop()

def _eval(i, val1, val2):
    if i == '^': 
        return val2 and val1
    return val2 or val1

input_logic()
final = entailment()
if final:
    print("Knowledge base entails query")
else:
    print("Knowledge base doesn't entail query")
    
    
#knowledge base: (~av~bvc)^(~a^b)^c 
#alpha: ~c

#knowledge base: (~avb)^(bvc)^c
#alpha: a^c


#ouput:

#Input logic: (avb)^(~cva)
#Input query: a^c
#kb : alpha
#False : False
#False : False
#False : False
#True : True
#False : False
#True : True
#True : True
#True : True
#Knowledge base entails query