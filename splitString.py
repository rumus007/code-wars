"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""
import re


def solution(s):
    if(len(s) % 2 != 0):
        s += "_"
    return re.findall('..', s)


print(solution('abcd'))
