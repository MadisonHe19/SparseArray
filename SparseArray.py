

'''There is a collection of input strings and a collection of query strings. For each query string,
determine how many times it occurs in the list of input strings. Complete the function
matchingStrings in the editor below. The function must return an array of integers representing the
frequency of occurrence of each query string in strings.matchingStrings has the following parameters:

strings - an array of strings to search
queries - an array of query strings

example string = ['ab', 'ab', 'abc'] queries = ['ab', 'abc', 'bc'] so 2 instances of ab , 1 of abc
and 0 of bc. For each query, we add an element to our return array results = [2,1,0]
'''
def matchingStrings(strings, queries):
    occurrences = []
    for querieString in queries:
        count = 0
        for inputString in strings:
            if querieString == inputString:
                count+= 1
        occurrences.append(count)
    return occurrences
