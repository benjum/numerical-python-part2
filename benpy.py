def compound_calculator(principal,rate,year,contribution):
    '''
    compound_calculator(p,r,y,c) calculates the value at year y of an investment
    p = principal
    r = interest rate (percent value)
    y = year
    c = contribution at end of each year
    '''

    p = principal
    r = rate/100
    y = year
    c = contribution
    balance = p*(1 + r)**y + c*( ((1 + r)**(y+1) - (1 + r)) / r )
    return balance