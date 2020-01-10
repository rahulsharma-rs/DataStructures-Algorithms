"""
Paranthesis or Bracket validator
input
{[()]}
output
True

input
{}[}
output false
"""
#function to closing paranthesis and popped paranthesis from the skack
def isPair(p1,p2):
    if p1=='{' and p2=='}':
        return True
    elif p1=="[" and p2==']':
        return True
    elif p1=='(' and p2==')':
        return True
    else:
        return False
#function to check whether the paranthesis in a sequence are balances or not
def isBalanced(str=None):
    if str==None:
        return -1
    size=len(str)#size of the string
    i=0#iterator variable of the string
    stack=[]#initialize the empty list as stack datastructure
    balanced=True#intialize balanced as true
    while i<size and balanced:
        if str[i] in "{[(":
            stack.append(str[i])#push the bracket in the stack
            i+=1
            continue
        elif str[i] in "}])":
            if not stack:#chech is stack is empty and the bracket in the string are closing paranthesis eg. }}
                print('Stack empty')
                balanced =False
                return balanced
            else:
                temp=stack.pop()#pop the top element from the list
                if isPair(temp,str[i]):#check whether the popped bracket and the encountered bracket are same
                    i+=1
                else:
                    balanced=False
        else:
            i+=1
    if len(stack)>0:# check if stack is empty
        balanced=False
    return balanced
code="#include <stdio.h>int main() {printf() displays the string inside quotation printf(\"Hello, World!\"); return 0;}"
#print(isBalanced(''))
print(isBalanced(code))