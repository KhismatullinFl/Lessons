class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda i: i[0])
        first = intervals[0][0]
        last = intervals[0][1]
        l = len(intervals)
        for i in range(1,l):
            if (last>=intervals[i][0]):
                if (last<intervals[i][1]):
                    last = intervals[i][1]
                if(first>intervals[i][0]):
                    first = intervals[i][0]
            else:
                intervals.append([first, last])
                first = intervals[i][0]
                last = intervals[i][1]
        intervals.append([first, last])

        del(intervals[0:l])
        return intervals