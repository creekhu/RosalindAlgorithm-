def calculate(k,m,n):
    total = k+m+n

    dominant = float(k)/total
    heter = float(m)/total
    recessive = float(n)/total

    bothrecessive = recessive * (float(n-1)/(total-1))
    bothheter = heter * (float(m-1)/(total-1)) * 0.25
    both = 2 *  recessive * (float(m)/(total-1)) * 0.5

    num = 1 - bothrecessive - bothheter - both
    print num
    
calculate(17,26,30)
