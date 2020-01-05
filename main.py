import sys
from query import query
from formatter import formatter

# do cli parsing tings
word = sys.argv[1]

# pass arg parsed from cli into query function
# results will be a dictionary w/ google, wikipedia and reddit as keys and links as values
results = query(word)

# formatter takes in results and returns appropriately formatted text to print
message = formatter(**results)

# print message to cmd
print(message)
