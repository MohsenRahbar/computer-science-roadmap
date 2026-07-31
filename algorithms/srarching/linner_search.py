pos = -1
def linner (mylist:list[int],n:int):
    i = 0 
    while i < len(mylist):
        if mylist[i] == n:
            globals() ['pos'] = i 
            return True
        i = i + 1
    return False

def main():
    mylist = [1,2,3,4,5,6]
    n = 5
    if linner(mylist,n):
        print(f"found at {pos}")
    else:
        print("NOT FOUND")
        
if __name__ == "__main__":
    main()