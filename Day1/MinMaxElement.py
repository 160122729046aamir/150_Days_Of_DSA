def minmaxelement(arr,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                continue
    return arr[0],arr[n-1]
print(minmaxelement([1,5,8,2,4,9,0],7))
