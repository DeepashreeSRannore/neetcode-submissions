"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #Since its an object
        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            prevend=intervals[i-1].end
            currstart=intervals[i].start
            if prevend>currstart:
                return False
        return True

        #TC : O(nlongn)
        #SC : O(n)


