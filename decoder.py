import base64
from itertools import cycle

FINAL_MESSAGE = '''LU4QAQwRIhIRVUlfTFEAFAg3HURYT1UkDg4eDAQLAwJBTWxJRBEcBiIEDxcNQkBWQAMLMAYRABxV 
Z1tCVQALDwQCAgQ0BQZTQ1JgAAEaAAAaEwoDAyJOQ05PVTIPDh0KDgkSQEpNcRsCFg0bMxJFUlNF 
SwUGAAhxRUNTCR0oRkJISUIbHwlHSis='''

KEY = "VictorGabrielvgfm"

result = []
for i, c in enumerate(base64.b64decode(FINAL_MESSAGE)):
  result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print(''.join(result))