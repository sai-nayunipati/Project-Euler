"""
This algorithm first adds all the multiples of three
to the running total, and then adds all the multiples
of five PROVIDED they are not also a multiple of three.
"""

def algorithm():
    runningTotal = 0
    # Add all multiples of three
    for i in range (1, 334): # range is [a,b)
        runningTotal += i * 3
    # Add all multiples of five, PROVIDED they are not a multiple of three
    for i in range (1, 200): # I  want all the valid numbers BELOW 1000
        if i % 3 != 0:
            runningTotal += i * 5
    
    print(runningTotal)

algorithm()
