"""
You are given a list of commands to perform on an initially empty list.
Perform the commands and print the list whenever the command is "print".

Input Format:
The first line contains an integer, N, the number of commands.
Each of the next N lines contains one of the commands described above.

Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
print
sort
print
pop
reverse
print

Sample Output:
[6, 5, 10]
[5, 10, 9, 1]
[1, 9, 10, 5]
"""

if __name__ == "__main__":
    N = int(input())
    lst = []
    for _ in range(N):
        inputs = list(input().split())
        cmd = inputs[0]
        args = map(int, inputs[1:])

        match cmd:
            case "insert":
                lst.insert(*args)
            case "print":
                print(lst)
            case "remove":
                lst.remove(*args)
            case "append":
                lst.append(*args)
            case "sort":
                lst.sort()
            case "pop":
                lst.pop()
            case "reverse":
                lst.reverse()
