# def counter(FIRST=0):
#     cnt = [FIRST]
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#     return add_one
#
# num5 = counter(5)
#
# print(num5())
# print(num5())
# print(num5())

# print(counter()())

def countA(a,b):
    def countY(x):
        return a*b+x
    return countY

line1 = countA(3,5)
line2 =  countA(4,6)
print(line1(4))
print(line2(7))