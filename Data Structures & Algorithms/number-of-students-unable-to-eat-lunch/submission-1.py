class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        counter = Counter(students)
        
        for s in sandwiches:
            if counter[s]:
                counter[s] -= 1
            else:
                break
        
        return counter[1] + counter[0]