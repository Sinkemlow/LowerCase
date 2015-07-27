import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.lower()
    print test.replace('\n','')

test_cases.close()
