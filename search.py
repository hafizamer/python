def ss(number_list, n):
    found=False
    for i in number_list:
        if i==n:
            found=True
            break
    return found

numbers=range(1,101)
result=ss(numbers, 99)
print(result)

result2=ss(numbers,101)
print(result2)
