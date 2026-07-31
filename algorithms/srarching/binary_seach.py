a = [-2,-1,0,2,3,45,50,51]

def search(arr:list[int],target:int) -> bool:
    
    N = len(arr)
    L = 0
    R = N -1
    while L <= R:
        M = (L + R) // 2
        if arr[M] == target:
            print(f"found at index  {M}")
            return True
        elif target < arr[M]:
            R = M -1
        else:
            L = M +1
            
    return False


print(search(a,45))
            
    
    