noOfSeries = 10
def fibonaci(noOfSeries):
    if noOfSeries == 0:
        return 0
    elif noOfSeries == 1:
        return 1
    else:
        return fibonaci(noOfSeries-1)+fibonaci(noOfSeries-2)

for i in range(noOfSeries):
    print(fibonaci(i))