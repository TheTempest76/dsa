def compareVersion( version1, version2):
        v1 = version1.split(".") # split the versions into two  lists of strings
        v2 = version2.split(".")
        for i in range(max(len(v1) , len(v2))):# extract each component out of each list
            num1 =  int(v1[i])  if i<len(v1) else 0 # this one is to prevent an index out of range error when we len of v1 is more than v2 or vice versa
            num2 = int(v2[i])  if i<len(v2) else 0 # because if one doesn't have a third part of a version then we want to have that as a zero
            if num1<num2:
                return -1
            elif num1>num2:
                return 1
        return 0

compareVersion("1.01", "1.01.00009")



# 165. Compare Version Numbers
# Solved
# Medium
# Topics
# Companies

# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

#     If version1 < version2, return -1.
#     If version1 > version2, return 1.
#     Otherwise, return 0.
