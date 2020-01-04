import argparse
from .query import query
from .formatter import formatter

# do cli parsing tings

# pass arg parsed from cli into query function
# results will be a dictionary w/ google, wikipedia and reddit as keys and links as values
results = query(args)

# formatter takes in results and returns approprietly formatted text to print
message = formatter(results)

# print message to cmd
print(message)
