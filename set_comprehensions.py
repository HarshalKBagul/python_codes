# set Comprehensions
#reverse of set

dict1={i:f"item{i}" for i in range(1,1001) if i%100==0}
print(dict1)
dict2={value:key for key,value in dict1.items()}
print(dict2)