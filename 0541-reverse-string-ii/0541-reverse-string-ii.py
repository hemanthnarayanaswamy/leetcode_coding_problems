class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = [chr for chr in s]         ## Convert string in List as string is immutable
        for i in range(0, len(s), 2*k): ## Iterating with a step count or batch of 2*K
            end_index = min(i+k, len(s))  ## We need to find the end index usually it is i+k if not enough character its len(s)
            s[i:end_index] = s[i:end_index][::-1] ## Reversing the elements 

        return "".join(s) ## List into String
             