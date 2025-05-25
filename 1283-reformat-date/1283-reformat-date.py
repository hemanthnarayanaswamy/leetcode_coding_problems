class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        dd, mm, yyyy = date.split() 
        dd = "0" + dd[0] if len(dd) == 3 else dd[:2]
        return f'{yyyy}-{months[mm]}-{dd}'