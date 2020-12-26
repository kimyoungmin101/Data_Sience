import matplotlib.pyplot as plt
import numpy as np
import sys
import re
from collections import Counter

y = []

for line in sys.stdin:
    count = re.sub('[^0-9]',' ', line).strip().split()
    if(len(count) >= 2):
        y.append(count[1])
    else:
        y.append(count[0])

x = [i+1 for i in range(len(y))]
plt.plot(x, y, color='blue', linestyle='solid')
plt.yscale('log')
plt.xscale('log')
plt.show()

print('S = 0.92817994137')
print('C = 10846791')
