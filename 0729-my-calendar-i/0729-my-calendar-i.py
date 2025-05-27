class MyCalendar:

    def __init__(self):
        self.booked_events = [] # [(startTime, endTime), ...]

    def book(self, startTime: int, endTime: int) -> bool:
        # TC: O(N)
        # SC: O(N)

        idx = bisect.bisect_left(self.booked_events, (startTime, endTime))

        if idx > 0:
            prev_end_time = self.booked_events[idx - 1][1]
            if prev_end_time > startTime:
                return False

        if idx < len(self.booked_events):
            current_event_idx_at_start_time = self.booked_events[idx][0]
            if current_event_idx_at_start_time < endTime:
                return False
        
        self.booked_events.insert(idx, (startTime, endTime))

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)