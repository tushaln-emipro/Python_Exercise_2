"""
    Program - 10
    [[2,4,5],[4,6,8],[3,6,9]]
    Considering the above list, we need to have a sum of all the values of all the inner lists.
    - Find the sum of only even numbers
    - Find the sum of all the numbers from all the inner lists
    Don’t use a loop.
"""
temp_list = [[2,4,5],[4,6,8],[3,6,9]]
flatList = [ item for elem in temp_list for item in elem]
print(sum(filter(lambda x: not x%2, flatList)))
