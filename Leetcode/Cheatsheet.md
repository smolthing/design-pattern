## Python

```python

max(1,2) # 2

list = [1,2,3]
list[0]
list.append(4)
squared = [x**2 for x in list]

for value in list:
    print(value) # 1

for index in range(len(list)):
    print(index) # 0

for index, value in enumerate(list):
    print(index, value) # 0, 1

s = "abc"
for i in list(s):
    print(ord(i)) # 97, 98, 99

dict = {'a': [1]}
dict['a'] # [1]
dict.get('a') # [1]
dict.get('b', [1]) # [1]

if 'a' in dict:
    dict['a'].append(1)
else:
    dict['a'] = [1]

from collecitons import defaultdict
dict2 = defaultdict(int) # { key: 1 }
dict2['unknown'] # 0
dict2['add'] = 1

dict3 = defaultdict(list) # { key: [] }
dict3['key'].append(1) # { key: [1]}

set1 = {1,2,3}
set1.add(3) # {1,2,3}

set2 = {2,3,4}


from collections import OrderedDict
cache = OrderedDict()
if key not in self.cache: # O(1) for the average case and O(n) for the worst case where collisions in the hash table, resulting in linear search time within hash buckets
cache.move_to_end(key)
self.cache.popitem(0)
cache[key] = value

set1.union(set2) # {1,2,3,4}
set1.difference(set2) # 1
set2.difference(set1) # 4

set([1,1,2,3]) #[1,2,3]

tuple = (1,2,3)
tuple[0] # 1
a,b,c = tuple

list = [4,1,5,2,3]
sorted(list) # returns [1,2,3,4,5], list is unsorted [4,1,5,2,3]
list.sort() # list is [1,2,3,4,5]
list.reverse() # list is [5,4,3,2,1]

list[::-1] # list is [1,2,3,4,5]

if 1 in list:
if 1 not in list:

a = 2
if 1 < a < 5:
    print('yes')

string = "this is a sentence"
string.split(" ") # ['this', 'is', 'a', 'sentence'], string is unchanged "this is a sentence"
",".join(string.split(" ")) # 'this,is,a,sentence'

"aa".upper() # AA
"AA".lower() # aa
"aa".islower() # true
"AA".isupper() # true
"abc".isalpha() # true
"a1".isalnum() # true
"1".isnumeric() # true
"Ⅷ".isnumeric()
" ".isspace() # true
"1".isdigit() # true
"".isdecimal() # 

a = [1,2,3,4,5]
a[:2] # [1, 2]
a[2:] # [3, 4, 5]
a[2:3] # [3]


from collections import Counter
counter = Counter('mississippi')
counter # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
counter['m'] # 1

import heapq
heap = [3, 10, 4, 7, 8, 20, 15] # min heap by defalt
heapq.heapify(heap)
heapq.nlargest(3, heap) # [20, 15, 10]
[20, 15, 10]
heap[0] # 3
heapq.heappop(heap)
heapq.heappush(heap, 1)
heapq.nsmallest(3, heap) # [3, 4, 7]

max_heap = [-num for num in [3, 10, 4, 7, 8, 20, 15]] # change to negative
heapq.heapify(max_heap)

counter = Counter('mississippi')
heapq.nlargest(k, counter.keys(), key=counter.get)

min(1,5) # 1
max(1,5) # 5
abs(-1) # 1
abs(1) # 1
pow(2,4) #16

5//2 # 2
5/2 # 2.5

import math
math.floor(1.9) # round down to 1
math.ceil(1.1) # round up to 2

10 % 2 # modulo, even number
11 % 2 # 1 , odd number
9 % 3 #  divisible by 3

list = [1,2,3,4,5]
rotation = 1000
actual_rotation = rotation % len(list) # no rotation, 0

k = 2
rotated_list = list[len(list) - k:] + list[:len(list) - k]  # last k item + items before k, [4, 5, 1, 2, 3]
rotated_list = list[-k:] + list[:-k] # shortcut, [4, 5, 1, 2, 3]

import requests
try:
    response = requests.get(current_page)
    response.raise_for_status()
    result = response.json()
    print(result)
except requests.exceptions.HTTPError as _:
    error_message = response.json().get("message")
    print(f"error message: {error_message}")
except Exception as error:
    print(f"uncaught error: {error}")
```


## Java
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder().uri(URI.create(hasNext)).build();
HttpResponse response = client.send(request, BodyHandlers.ofString());
ObjectMapper mapper = new ObjectMapper();
List<RepoItem> repoItems = mapper.readValue(response.body().toString(),
          new TypeReference<>() {
          });


import java.util.Optional;

Optional<String> value = Optional.of("hello");
Optional<String> valueEmpty = Optional.empty();
String result = valueEmpty.orElse("hello");

if (value.isPresent()) {
    value.get();
}

value.ifPresent(value -> System.out.println(value));

Optional<String> transformedValue = value.map(value -> value.toUpperCase());
transformedValue.ifPresent(value -> System.out.println(value));
```

## JavaScript
```js
try {
    const response = await fetch(url);
    const listOfRepos = await response.json();
    if (response.ok) {
        console.log(listOfRepos);
    }
} catch (error) {
    console.log(error);
}

[1,2,3].reduce((total, current) => total + current, 0);
["one", "two", "three"].filter(item => ["input", "one"].some(word => item.includes(word)));


```

## TypeScript
```
```


## Questions

200. Number of Islands

Given a matrix, find the number of island.
Iterate through all the node and increment if it is 1, use dfs on all directions and set linked island to 0.
time complexity: O(n)
space complexity: 1
```
def numIslands(self, grid: List[List[str]]) -> int:
    count = 0
    gridRow = len(grid)
    gridCol = len(grid[0])

    for row in range(gridRow):
        for col in range(gridCol):
            if grid[row][col] == "1":
                count += 1

                self.setIslandToVisited(grid, row + 1, col)
                self.setIslandToVisited(grid, row - 1, col)
                self.setIslandToVisited(grid, row, col + 1)
                self.setIslandToVisited(grid, row, col - 1)
    
    return count

def setIslandToVisited(self, grid, row, col) -> None:
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
        return
    
    grid[row][col] = "0"
    self.setIslandToVisited(grid, row + 1, col)
    self.setIslandToVisited(grid, row - 1, col)
    self.setIslandToVisited(grid, row, col + 1)
    self.setIslandToVisited(grid, row, col - 1)
```

3. Longest Substring Without Repeating Characters

Store characters last position in a dict and track max count
time complexity: O(n)
space complexity: O(n)
```
def lengthOfLongestSubstring(self, s: str) -> int:
    longestSubstringCount = 0
    charMap = {}
    startIndex = 0

    for index, char in enumerate(s):
        if charMap.get(char, -1) >= startIndex:
            startIndex = charMap[char] + 1
        
        charMap[char] = index
        longestSubstringCount = max(longestSubstringCount, index - startIndex + 1)
    
    return longestSubstringCount
```

701. Insert into a Binary Search Tree

bst means left is always smaller than right, if value is small and no left node, add a note to left. if there is a left,
go into the left and compare left and right again.
time complexity: O(h) height of tree
space complexity: O(h)
```
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)

    currentValue = root.val

    if not root.left and val < currentValue:
        root.left = TreeNode(val)
    elif not root.right and val > currentValue:
        root.right = TreeNode(val)
    elif val < currentValue:
        self.insertIntoBST(root.left, val)
    elif val > currentValue:
        self.insertIntoBST(root.right, val)

    return root
```

206. Reverse Linked List

time complexity: O(n)
space complexity: O(1)

```
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    newHead = None
    
    while head:
        temp = head.next
        head.next = newHead
        newHead = head
        head = temp

    return newHead
```

704. Binary Search

check middle, otherwise go to left or right

time complexity: O(logn)
space complexity: O(1)
```
def search(self, nums: List[int], target: int) -> int:

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2 # (start + end ) // 2 might get overflow 

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            print(start, end)
            start = mid + 1
        else:
            print(start, end)   
            end = mid - 1

    return -1 
```

217. Contains Duplicate

time complexity: O(n)
space complexity: O(n)
```
def containsDuplicate(self, nums: List[int]) -> bool:
    visited = {}

    for i in nums:
        if visited.get(i) != None:
            return True
        visited[i] = True

    return False
```

```
def containsDuplicate(self, nums: List[int]) -> bool:
    return not len(set(nums)) == len(nums)
```

207. Course Schedule

check for cycle in graph
time complexity: O(n)
space complexity: O(n)
```
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        checked = [False] * numCourses
        visited = [False] * numCourses

        for i in range(numCourses):
            if self.hasCycle(graph, i, visited, checked):
                return False
            
            checked[i] = True
        
        return True

    def hasCycle(self, graph, course, visited, checked):
        if checked[course]:
            return False

        for prereq in graph[course]:
            if visited[prereq]:
                return True

            visited[prereq] = True
            if self.hasCycle(graph, prereq, visited, checked):
                return True

            visited[prereq] = False
        
        return False
```

210. Course Schedule II

check for cycle in graph, add to an ordered list
time complexity: O(n)
space complexity: O(n)
```
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # create a graph course -> prerequiste
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        
        # create orderList, checkedCourse, visitedCourse
        orderList = []
        checkedCourse = [False] * numCourses
        visitedCourse = [False] * numCourses
    
        for i in range(numCourses):
            if self.hasCycle(graph, i, checkedCourse, visitedCourse, orderList):
                return []

            checkedCourse[i] = True

        return orderList

        
        return orderList
        # for every course starting from 0, check for cycle, add to checkCourse and reset visistedCourse

    def hasCycle(self, graph, numCourse, checkedCourse, visitedCourse, orderList):
        if checkedCourse[numCourse]:
            return False

        for prereq in graph[numCourse]:
            if visitedCourse[prereq]:
                return True

            visitedCourse[prereq] = True

            if self.hasCycle(graph, prereq, checkedCourse, visitedCourse, orderList):
                return True

            visitedCourse[prereq] = False

        if numCourse not in orderList:
            orderList.append(numCourse)

        return False
```

176. Second Highest Salary
```
select max(salary) as SecondHighestSalary from employee where salary < (select max(salary) from employee)
```

175. Combine Two Tables
```
select p.firstName, p.lastName, a.city, a.state
from person as p
left join address as a
on p.personId = a.personId
```

56. Merge Intervals

time complexity: O(nlogn)
space complexity: O(n)
```
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged_intervals = []

    for start, end in intervals:
        if not merged_intervals:
            merged_intervals.append([start,end])
        else:
            last_interval = merged_intervals[-1]
            if start <= last_interval[1]:
                last_interval[1] = max(last_interval[1], end)
            else:
                merged_intervals.append([start,end])
    return merged_intervals
```

20. Valid Parentheses

time complexity: O(n)
space complexity: O(n)
```
def isValid(self, s: str) -> bool:
    mapping = {"{":"}", "[":"]", "(":")"}
    stack = []
    for i in list(s):
        if i in mapping:
            stack.append(i)
        elif not stack or i != mapping[stack.pop()]:
            return False

    return len(stack) == 0
```

797. All Paths From Source to Target

time complexity: O(nodes + edges)
space complexity: O(nodes + edges)
```
def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    allPaths = []
    
    stack = [(0,[0])]
    reachLastNodeOfAPath = len(graph) - 1

    while stack:
        currentNode, path = stack.pop()
        
        if currentNode == reachLastNodeOfAPath:
            allPaths.append(path)
        
        for neighbour in graph[currentNode]:
            stack.append((neighbour,path+[neighbour]))

    return allPaths
```

1. Two Sum

time complexity: O(n)
space complexity: O(n)
```
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for index, value in enumerate(nums):
            if visited.get(target - value, -1) >= 0:
                return [visited[target - value], index]
            visited[value] = index

        return []
```


35. Search Insert Position

time complexity: O(n)
space complexity: O(1)
```
def searchInsert(self, nums: List[int], target: int) -> int:
    
    start = 0 
    end = len(nums) - 1

    while start <= end:
        mid = start + (end-start) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return start
```

1011. Capacity To Ship Packages Within D Days
Guess the capacity to be between max value and sum of all values, then check if capacity will result in the n days. Do a binary search to find the next capacity guess.

time complexity: O(nlogn)
space complexity: O(1)
```
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)

        while start < end:
            mid = (start + end) // 2
            currentDays = self.getDays(mid, weights)
            
            if currentDays <= days:
                end = mid
            else:
                start = mid + 1

        return start

    def getDays(self, capacity: int, weights: List[int]) -> int:       
        days = 1
        currentCapacity = 0
 
        for w in weights:
            currentCapacity += w

            if currentCapacity > capacity:
                days += 1
                currentCapacity = w
        print(days, capacity)
        return days

```