
X = [[7,20,12],[10,25,16],[27,9,6]]

Y = [[3,18,11],[61,15,3],[4,50,9]]

sum = [[0,0,0],[0,0,0],[0,0,0]]

for a in range(len(X)):

    for b in range(len(Y)):
        
        sum[a][b] = X[a][b] + Y[a][b]
print(sum)

