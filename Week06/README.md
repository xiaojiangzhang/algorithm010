# 递归代码模板
```
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

# 分治代码模板
```
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 
  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 
  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …
  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

# 动态规划

关键点：
1. 动态规划和递归或者分治没有本质上的区别，（关键看有无最优子结构）
2. 共性：找到重复子问题
3. 差异性：最优子结构、中途可以淘汰次优解。


**DP三步走**
1. 最优子结构
2. 存储中间状态
3. 递推公式（状态转移方程或者DP方程）