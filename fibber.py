'''
calculates the summation of all numbers below it in a step wise fashion
how this works in math is, the fibonacci number recursively calls itself as
a summation of two of its functions(itself minus 1 plus itself minus two)
the (itself minus one) is the umber in the sequence before it. The (itself minus 2)
is the number below that, at some point the sum will reachzero and the function stops
RecursionError: maximum recursion depth exceeded
NEEED TO FIND A WAY TO PRINT
NEED TO SIMPLIFY RECURSIVE THINKING ENOUGH TO TEACH TO A CHILD
'''
def Fibber(n):
    #accounts for if n is zero then theres nothing tp add preceding it
    #print(Fibber(n-1) + Fibber(n-2))
    if n == 0: return 0
    #becuase of how the math works 1 will always return 1 becuse the only thing before it is 0
    elif n == 1: return 1
    #from 2 on (which returns 1) it will do the correct math test 20 ===6765
    else:
      #
      return Fibber(n-1)+Fibber(n-2)


print(Fibber(20))
