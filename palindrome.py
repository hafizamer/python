def palindrome(word):
    word=word.lower()
    return word[::-1]==word

result=palindrome("mom")
print(result)
result=palindrome("algo")
print(result)
result=palindrome("algoogla")
print(result)
                  
