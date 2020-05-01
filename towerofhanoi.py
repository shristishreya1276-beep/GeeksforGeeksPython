'''Tower of Hanoi is very common problem. In the question there are n disks and three towers and we are supposed to move the disks to one tower from other by keeping in the same order while keeping larger one at bottom and smaller ones at top. Code in python using python.'''
n = int(input("Enter number of disks: "))
def TowerOfHanoi(n, source, destination, using):
    if n == 1:
        return print("Move disk 1 from " + source + " to destination " + destination)
    TowerOfHanoi(n-1, source, using, destination)
    print("Move disk " + str(n) + " from " + source + " to destination " + destination)
    TowerOfHanoi(n-1, using, destination, source)
TowerOfHanoi(n, 'A', 'C', 'B')
