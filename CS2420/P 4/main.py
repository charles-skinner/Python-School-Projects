from stack import Stack

def main():
    f = open("data.txt", "r")
    content = f.readlines()
    for line in content:
        print(f"infix: {line}",end="")
        print("postfix: ",end="")
        postfix = in2post(line)  
        answer = eval_postfix(postfix)
        print(f"answer: {answer}")
        print()

def cleaner(expr):
    if type(expr) != str:
        raise ValueError
    return expr.replace(" ","").strip("\n")

def in2post(expr):
    expr = cleaner(expr) #remove spaces and \n's
    st = Stack() #ready the stack
    operators = {"+":1,"-":1,"*":2,"/":2} #this is used to determine which operator has precedence
    postfix = "" #we will be adding characters to this as we go
    i = 0 
    while True:
        try:
            expr[i] #try to get the character
        except:
            break  #if it doesn't work you're out of index and we're done iterating
        if expr[i] == "(": #is the character a "("?
            st.push(expr[i]) #put it on the stack
            i += 1 #move on to next character
        elif expr[i].isdigit(): #is the character a number? 
            print(expr[i],end=" ") #print it
            postfix += expr[i] #add it to our string
            i += 1 #move on
        elif expr[i] in operators: #is character an operation symbol?
            #check the stack for an operation of higher precedence 
            while (st.head)and(st.top()!="(")and(operators[st.top()]>=operators[expr[i]]):
                postfix += st.top() #if there was one we will add it and look for another
                print(st.pop(),end=" ") #print any we find
            st.push(expr[i]) #there weren't any higher operators so we add the current one to the stack
            i += 1 #move on
        else: #it isn't a left parens, number, or operator. should be right parens
            #move items from the stack to string until you reach "(" if it's not there raise syntax error
            while True:
                try:
                    st.top() #try to look at top of stack
                except:
                    raise SyntaxError #if there's nothing on the stack that's a problem, raise error
                if st.top()!="(": #if the top isn't a "(" it should be an operator
                    postfix += st.top() #add to postfix
                    print(st.pop(),end=" ") #remove it from stack and print
                else: #we've found the corresponding parens
                    st.pop() #remove from stack
                    i += 1
                    break #stop iterating
    while True:
        try:
            st.top()
        except:
            break
        postfix += st.top()
        print(st.pop(),end=" ")
    print()
    return postfix
      
def eval_postfix(expr):
    st = Stack()
    i = 0
    if type(expr) != str:
        raise ValueError
    while True:
        try: 
            expr[i]
        except:
            break
        if expr[i] == " ":
            i += 1
        elif expr[i].isdigit():
            st.push(expr[i])
            i += 1
        else:
            try:
                b = int(st.pop())
                a = int(st.pop())
            except:
                raise SyntaxError
            if expr[i] == "+":
                st.push(a + b)
            elif expr[i] == "-":
                st.push(a - b)
            elif expr[i] == "*":
                st.push(a * b)
            else:
                st.push(a / b)

            i += 1
    return int(st.pop())

            
if __name__ == "__main__":
    main()