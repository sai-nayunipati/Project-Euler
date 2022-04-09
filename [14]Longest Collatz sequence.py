def recursiveAlgorithm(input, count):
    if input/2 == 1:
        return count + 1
    
    if input % 2 == 0:
        count = recursiveAlgorithm(input/2, count+1)
    else:
        count = recursiveAlgorithm(3*input+1, count+1)
    
    return count

# Program
max = 0
number = 0
for i in range(1,999999):
    answer = recursiveAlgorithm(i, 0)
    if answer > max:
        max = answer
        number = i
        
print(number)
