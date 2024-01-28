s = 'cba cba cba'
print(' '.join(''.join(sorted(x)) for x in s.split()))