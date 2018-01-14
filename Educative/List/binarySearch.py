class Solution(object):
    def binarySearch(self,arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low +high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

def assertEqual(a, b):
    if a != b:
        print(False)
    else:
        print(True)

if __name__ == '__main__':
    print("###### test 1 ########")
    S = Solution()
    arr = [1,2,3,4,5,6,7,8,9,10]
    assertEqual(S.binarySearch(arr,5), 4)

    print("###### test 2 ########")
    arr = []
    assertEqual(S.binarySearch(arr, 4), -1)

    print("###### test 3 ########")
    arr = []
    for i in range(100000000):
        arr.append(i)

    assertEqual(S.binarySearch(arr, 100000), 100000)

