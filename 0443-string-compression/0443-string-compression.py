class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
    
        write = 0  # Where to write in the array
        read = 0   # Where we're reading from
        
        while read < len(chars):
            # Step 1: Get current character
            current_char = chars[read]
            count = 0
            
            # Step 2: Count how many times it repeats
            while read < len(chars) and chars[read] == current_char:
                count += 1
                read += 1
            
            # Step 3: Write the character
            chars[write] = current_char
            write += 1
            
            # Step 4: If more than 1, write the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write