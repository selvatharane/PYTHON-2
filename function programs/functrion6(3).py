'''15 + 30 + 45 + 60 + …… + N
Sample Input
N = 5 (Number of terms)
Then the series will be 15 + 30 + 45 + 60 +75
Sample Output:
_______'''
def series_sum():
    sum=0
    common_diff=15
    num_terms=5
    for i in range(num_terms):
        term=common_diff*(i+1)
        sum+=term
    return sum
res=series_sum()
print(res)
