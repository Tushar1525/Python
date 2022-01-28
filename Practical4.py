# -*- coding: utf-8 -*-
'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
Input Format: The first line contains. The second line contains an array A[]  of n integers each separated by a space.
Constraints:
Output Format: Print the runner-up score.

Sample Input

5
2 3 6 6 5

Sample Output

5
Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''

a=int(input())  # For Input
run_up=map(int,input().split())  # inputing for 1 runner-ups
print(sorted(list(set(run_up)))[-2])  # sorting the list