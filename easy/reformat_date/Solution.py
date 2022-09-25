class Solution:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    def reformatDate(self, date: str) -> str:
        date = date.split(" ") 
        num,month,year = date[0].strip("strdhn"), self.months.index(date[1]) + 1, date[2]
        if(month <10):
            month = "0"+str(month)
        else: month = str(month)
        if(int(num) <10):
            num = "0"+str(num)
        else: month = str(month)
        return year + "-" + str(month) + "-" + num
        
s = Solution()