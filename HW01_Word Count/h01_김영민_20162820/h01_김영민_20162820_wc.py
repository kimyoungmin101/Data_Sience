import sys
import re
from collections import Counter
    
words = int(sys.argv[1])

n = 0

counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in re.sub('[^a-zA-Z0-9]',' ', line).strip().split()
                  )

for word, wordcount in counter.most_common(words):
    sys.stdout.write(word)
    sys.stdout.write("\t")
    sys.stdout.write(str(wordcount))
    sys.stdout.write("\n")