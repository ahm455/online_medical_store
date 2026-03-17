A = [
    [2, 5, 1,5],
    [0, -3, 4,6],pip install googlemaps pandas
    [7, 2, 6,9]
]

B = [
    [1, 0, 3],
    [-2, 4, 5],
    [3, -1, 2],
    [2,4,5]
]
def add_matrices(a, b):
    result=[]
    for x in range(len(a)):
        row=[]
        for y in range(len(a[0])):
            row2=a[x][y]+b[x][y]
            row.append(row2)
        result.append(row)    

    print(result)
def sub_matrices(a, b):
    result=[]
    for x in range(len(a)):
        row=[]
        for y in range(len(a[0])):
            row2=a[x][y]-b[x][y]
            row.append(row2)
        result.append(row)    

    print(result)

def multi_matrices(a,b):
    result=[]
    for x in range(len(a)):
        row=[]
        for y in range(len(b[0])):
            total=0
            for k in range(len(a[0])):
                l= a[x][k]*b[k][y]
                total+=l
            row.append(total)
        result.append(row)  
    print(result)    


multi_matrices(A,B)    