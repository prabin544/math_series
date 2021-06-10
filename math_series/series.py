def fibonacci(n):
    """
    Return nth value in the fibonacci series 

    """
    n1, n2 = 0, 1
    count = 0
    flst = []
    while count < n:
        flst.append(n1)
        nth = n1 + n2     
        n1 = n2           
        n2 = nth          
        count += 1
    return flst[n-1]

def lucas(n):
    """
    Return nth value in the lucas numbers 
    
    """
    n1, n2 = 2, 1
    count = 0
    llst = []
    while count < n:
        llst.append(n1)
        nth = n1 + n2     
        n1 = n2           
        n2 = nth          
        count += 1
    return llst[n-2]

# def sum_series(n, x=0, y=1):
#     if n == 0:
#         return x
#     if n == 1:
#         return y
#     slst = [] * n + 1
#     slst[0] = x
#     slst[1] = y

#     for items in slst:
#         slst[items] = slst[items - 1] + slst
#         return slst[n]

    