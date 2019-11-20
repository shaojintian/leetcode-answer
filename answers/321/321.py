'''
记住！！！！！
python里 list ，dictionary都是传址的！！！！！！！！！！！任何CRUD操作都需要.copy()防止被修改
'''

def maxNumber(nums1,nums2,k):
    def pickMaxSubList(nums, i):
        if not i:
            return []
        res, _pop = [], len(nums) - i
        while nums:
            num = nums.pop(0)
            # _pop is pop number
            while res and _pop and res[-1] < num:
                res.pop(-1)
                _pop -= 1
            res.append(num)
        return res[:i]

    res = [0 for _ in range(k)]

    for i in range(k + 1):
        if i <= len(nums1) and k - i <= len(nums2):
            l1 = pickMaxSubList(nums1.copy(), i)
            l2 = pickMaxSubList(nums2.copy(), k-i)
            # print('l2',l2)
            temp = [max(l1, l2).pop(0) for _ in range(k)]
            if res < temp:
                res = temp
    return res

if __name__ == '__main__':
    print(maxNumber([3,4,6,5],[9,1,2,5,8,3],5))
