# 1. 绳子覆盖最多的点数 
# planA,O(N*logN)
def max_points(arr, L):   
  ans = 1   
  for i in range(len(arr)):     
    nearst = nearest_index(arr, i, arr[i]-L)     
    ans = max(ans, i-nearest+1) 
  return ans
    
def nearest_index(arr, R, value):  
  L = 0   
  index = R   
  while L < R:     
    mid = L + ((R-L)>>1)     
    if arr[mid] >= value:       
      index = mid       
      R = mid - 1    
    else:       
      L = mid + 1  
  return index 

# planB 滑动窗口
def max_point_2(arr, L):
  left, right = 0, 0
  n = len(arr)
  max_ = 0
  while L < n:
    while right < n and arr[right]-arr[left] <= L:
      right += 1
    max_ = max(max_, right-left)
    left += 1
  return max_
