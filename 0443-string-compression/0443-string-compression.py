class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed = []
        curr_char = ""
        curr_char_count = 0
        for c in chars:
            if curr_char_count == 0:
                curr_char = c
                curr_char_count = 1
            elif c == curr_char:
                curr_char_count += 1
            else: 
                compressed.append(curr_char)
                if curr_char_count != 1:
                    compressed.extend(list(str(curr_char_count)))
                curr_char = c
                curr_char_count = 1
        
        compressed.append(curr_char)
        if curr_char_count != 1:
            compressed.extend(list(str(curr_char_count)))
        print(compressed)
        chars[:len(chars)] = compressed
        print(chars)
        print(len(chars))
        return len(chars)