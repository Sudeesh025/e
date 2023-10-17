def tower_of_hanoi(n,source,destination,auxilary):
    if(n==1):
        print("move the disk  from source",source,"to destination",destination)
        return
    tower_of_hanoi(n-1,source,auxilary,destination)
    print("move the disk" , n ,"from source",source,"to destination",destination)
    tower_of_hanoi(n-1,auxilary,destination,source)
n=4
tower_of_hanoi(n,"A","B","c")