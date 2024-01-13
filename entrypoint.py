import sys
import os

HELP = 'See https://github.com/dolsem/secure-cql-shell/blob/main/README.md'

if not 'cert' in os.environ:
  print('Error: missing "cert" environment variable. ' + HELP, file=sys.stderr)
  exit(1)
if not 'key' in os.environ:
  print('Error: missing "key" environment variable. ' + HELP, file=sys.stderr)
  exit(1)

with open('/cert.pem', 'w') as f:
  f.write(os.environ['cert'])
with open('/key.pem', 'w') as f:
  f.write(os.environ['key'])

os.execvp('cqlsh', ['cqlsh'] + sys.argv[1:])
