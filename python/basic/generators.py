def gen(n):                            
   while True:                              
       yield n                                
       n += 1                                                      

G = gen(3)     # starts at 3                      
print(next(G)) # 3                       
print(next(G)) # 4                       
print(next(G)) # 5                       
print(next(G)) # 6