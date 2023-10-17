def subset_sum(arr, n, target, current_subset=[]):
    if target == 0:
        print("Subset with the given sum:", current_subset)
        return
    if n == 0 and target != 0:
        return
    if arr[n - 1] > target:
        subset_sum(arr, n - 1, target, current_subset)
        return
    include_current = current_subset + [arr[n - 1]]
    subset_sum(arr, n - 1, target - arr[n - 1], include_current)
    subset_sum(arr, n - 1, target,current_subset)

arr = [6,8,9,5,4,3,26,2]
target = int(input("Enter the target sum: "))
n = len(arr)
subset_sum(arr, n, target)