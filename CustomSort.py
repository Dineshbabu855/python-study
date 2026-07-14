arr =["a","aa","aaaaaaa","aaa","aa","a","a","a"]
arr.sort(key=lambda x: len(x))
print(arr)