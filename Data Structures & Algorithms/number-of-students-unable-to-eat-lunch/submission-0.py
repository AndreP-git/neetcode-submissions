class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        counter = 0 
        students = deque(students)
        sandwiches = sandwiches[::-1]

        while students and counter <= len(students):
            if students[0] == sandwiches[-1]:
                students.popleft()
                sandwiches.pop()
                counter = 0
            else:
                students.append(students.popleft())
                counter += 1
            print(students)
            print(sandwiches)
        
        return len(students)