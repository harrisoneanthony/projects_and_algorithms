'''Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]'''

def tower_builder(n_floors):
    tower = []
    for n in range(1,n_floors+1):
        tower.append(f"{(n_floors - n)*' '}{(n-1)*'*'}*{(n-1)*'*'}{(n_floors - n)*' '}")
    return tower
    

print(tower_builder(3))