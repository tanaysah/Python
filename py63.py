try:
    with open("numbers.txt", "r") as f:
        nums = [int(x.strip()) for x in f.readlines()]

    # a. Max number
    max_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
    print("Max:", max_num)

    # b. Average
    avg = sum(nums) / len(nums)
    print("Average:", avg)

    # c. Count >100
    count = sum(1 for n in nums if n > 100)
    print("Count >100:", count)

except Exception as e:
    print("Error:", e)