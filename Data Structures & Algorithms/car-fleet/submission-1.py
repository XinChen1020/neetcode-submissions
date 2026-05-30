class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time
         
        result = 0
        sorted_pos_speed = sorted(zip(position, speed), reverse = True)
        time = [(target - pos) / speed for pos, speed in sorted_pos_speed]
        stack = deque()

        for i in range(len(time)):

            # if current time to complete is higher than the previous
            # fleet time, a new fleet would be formed.
            # otherwise, it will get merged
            if not stack or time[i] > stack[-1]:
                result += 1
                stack.append(time[i])
            
        return result