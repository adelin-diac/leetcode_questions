class MinStack:
    def __init__(self):
        # items entering the stack get appended to end
        # each item will be:
        # {value: XX, min: XX}
        # find min at time of insertion
        self.stack = []

    def push(self, val: int) -> None:
        # if no items in stack, min is the item being added
        if len(self.stack) == 0:
            tmp_min = val
        else:
            # otherwise, min is most recent minimum
            tmp_min = self.stack[-1]['min']
        
        # if new value less than most recent minimum, update the min
        if val < tmp_min:
            tmp_min = val

        item = {}
        item['value'] = val
        item['min'] = tmp_min

        self.stack.append(item)

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]['value']

    def getMin(self) -> int:
        return self.stack[-1]['min']


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()