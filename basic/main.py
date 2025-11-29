if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nums = set(arr)
    if len(nums) < 0:
        print(0)
    
    largest = max(nums)
    nums.remove(largest)
    print(max(nums))