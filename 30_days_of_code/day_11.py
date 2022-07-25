def hourglass(arr):
    max =-float('inf') # for negative values
    for i in range(1,5):
        for j in range(1,5):
            sum = 0
            sum += arr[i][j]
            sum += arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            sum += arr[i+1][j-1] + arr[i-1][j] + arr[i+1][j+1]

            if sum > max:
                max = sum
    return max

if __name__ == '__main__':
        arr = []

        for I in range(6):
            arr.append(list(map(int, input().rstrip().split())))

print(hourglass(arr))