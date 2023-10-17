def Generate_list(n):
    table_list=[]
    for i in range(0,n):
        row=[]
        for a in range(0,n):
            row.append(a)
        table_list.append(row)
    return table_list

print(Generate_list(10))