"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace
at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def strip_comments(string, markers):
    output = []
    for line in string.split('\n'):
        formatted = line.strip()
        for marker in markers:
            if marker in formatted:
                formatted = formatted.split(marker)[0].strip()
        output.append(formatted)
    return '\n'.join(output)
