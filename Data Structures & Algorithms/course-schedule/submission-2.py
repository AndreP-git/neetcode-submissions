class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses # counts how many courses have a certain pre
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[pre] += 1
            graph[course].append(pre)

        queue = deque()
        for n in range(numCourses): # all course with no prereq can be added to queue
            if indegree[n] == 0:
                queue.append(n)
        
        finish = 0
        while queue:
            node = queue.popleft()
            finish += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return finish == numCourses 
