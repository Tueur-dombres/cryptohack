def gcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y
print(7**16%17)