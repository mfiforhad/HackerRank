def avg(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)


print(avg(2, 5))


def reverse_words_order(sentence):
    s = sentence.split()
    s.reverse()
    output = " ".join(s)
    return output.swapcase()


print(reverse_words_order("aWESOME is cODING"))
