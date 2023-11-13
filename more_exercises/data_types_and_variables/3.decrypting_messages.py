key = int(input())
print(*[chr(ord(input()) + key) for i in range(int(input()))], sep="")