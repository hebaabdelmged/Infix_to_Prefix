#from pythonds.basic.stack import Stack
class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
def infixToPreFix(infixExpr): # convert an infix expression to a prefix expression
                              # e.g: A+B ==> +AB

    opStack = Stack() # Stack for the operators
    varStack = Stack() # Stack for the variables


    prec = {} # dictionary for the the priorities of the operations/precedures
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1


    #if token intered without spaces : tokenList = infixExpr.split()
    # ==>> split the string to a list

    for token in infixExpr:

        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            varStack.push(token) # if token is a variable, push it to the variable stack

        elif token =='(':
            opStack.push(token) # in case of an open round bracket, push it to the operator stack

        elif token == ')': #in case of closed bracket:

            while (opStack.peek() != '('): # pop both variable and operator stack until an open bracket is found

                # the prefix converting process
                operand1 = varStack.pop()
                operand2 = varStack.pop()
                operator = opStack.pop()

                tmpString = operator+operand2+operand1

                varStack.push(tmpString)

            opStack.pop() # to remove the residual '('

        else: # if token is an operator

            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]): # if the operator stack isn't empty,
                                                                                    # then compare the priorities.
                                                                                    # if the current operator/token is lower or equal, then pop the higher operator and 2 variables from the variable stack
                # the prefix converting process
                operand1 = varStack.pop()
                operand2 = varStack.pop()
                operator = opStack.pop()

                tmpString = operator + operand2 + operand1

                varStack.push(tmpString)


            opStack.push(token) #if the operator stack is empty, then push it to the stack

    while not opStack.isEmpty(): # in case the loop is finished, then process any risdual operators and push it to the variable stack till the operator stack is empty

        # the prefix converting process
        operand1 = varStack.pop()
        operand2 = varStack.pop()
        operator = opStack.pop()

        tmpString = operator + operand2 + operand1

        varStack.push(tmpString)

    return varStack.peek() # output prefix expression 


Expression = list(input('Enter the Infix Expression: '))

print ("The Prefix Expression: " + infixToPreFix(Expression))
