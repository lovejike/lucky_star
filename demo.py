# 1. 绳子覆盖最多的点数 
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
