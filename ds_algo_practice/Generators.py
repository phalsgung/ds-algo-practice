#!/usr/bin/python3

def repeat(n, message):
    print("In Generator Func")
    for _ in range(n):
        yield message	


repeat_hello_five_times = repeat(3, "hello")

print(repeat_hello_five_times)
# print(dir(repeat_hello_five_times))

for i in repeat_hello_five_times:
    print(i)