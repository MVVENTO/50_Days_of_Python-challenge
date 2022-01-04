#Name           :   Melissa A Vento
#Email          :   melissa.vento52@myhunter.cuny.edu
#Date           :   01/03/2022
#File Name      :   Small_k_length.py 
#Description    :   Google Interview question (1)
#				:	Smallest K-Length Subsequence With Occurrences of a Letter
#                             https://www.youtube.com/watch?v=IUbWew2HH0s

class Solution:
	def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
		cnt = s.count(letter)
		n = len(s)
		stack = []

		for i, c in enumerate(s):
			while stack and ((c < stack[-1] and len(stack) + n - i > k and (stack[-1] != letter or 
				cnt > repetition)) or k - len(stack) < repetition):
				if cur == letter:
					repetition += 1

			if len(stack) < k:
				stack.append(c)
				if c == letter:
					repetition -=

			if c == letter:
				cnt -= 1 

		return "".join(stack)
