"""

Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
"""

def tower_builder(n_floors):
    intialChar = '*'
    step = 1
    stack = []
    totalSteps = (n_floors * 2) - 1
    for i in range(0,n_floors):
        stack.append(f'{(intialChar * step):^{totalSteps}}')
        step += 2
    return stack

print(tower_builder(1))    
print(tower_builder(2))    
print(tower_builder(3))    
print(tower_builder(4))    
print(tower_builder(5))    
