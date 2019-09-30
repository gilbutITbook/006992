import time
import random

count = 0
start = time.clock()

for i in range(10000000):
    count += 1
    random.random()

end = time.clock()
print(end-start)
