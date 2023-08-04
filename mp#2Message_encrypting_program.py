message = (input("ENTER A MESSAGE:\n"))

class Solution:
   def solve(self, s, k):
      def shift(c):
         i = ord(c) - ord('a')
         i += k
         i %= 26
         return chr(ord('a') + i)

      return "".join(map(shift, s))

ob = Solution()
print("=========================================")
print(message,"ENCRYPTED TO:\n", (ob.solve(message, 3)))
print("==============@NIETO=====================")
