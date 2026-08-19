class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        bookings = defaultdict(set)
        reservedRows = set()

        for r, s in reservedSeats:
            bookings[r].add(s)
            reservedRows.add(r)
        # print(bookings)

        ans = (n - len(reservedRows)) * 2
        for r in reservedRows:
            if r in bookings:
                row = [1] * 11
                v = 0
                for s in bookings[r]:
                    row[s] = 0
                #print(r, row)
                if sum(row[2:6]) == 4:
                    v += 4
                if sum(row[6:10]) == 4:
                    v += 1
                if sum(row[4:8]) == 4:
                    v += 2
                
                if v == 7 or v == 5:
                    ans += 2
                elif v != 0:
                    ans += 1

        return ans
