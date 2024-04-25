def tower( pegs,a ,b ,c):
    if pegs<1:
        return
    tower(pegs-1 , a,b,c)
    print(f'move peg from {a} to {b} ')
    tower(pegs-1 , b,c,a)
    
# a is the 1st pole , b is the intermediate pole and c is the target pole
tower(3,'a','b','c')