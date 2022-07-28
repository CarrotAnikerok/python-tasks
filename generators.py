#1
print("Первая задача")
a = [1,2,4,6,7,5]
na = [i*i for i in a]
print(na)

#2
print("Вторая задача")
na = [i for i in a if i%2!=0]
print(na)

#3
print("Третья задача")
a=["red","5","76","cry","111111","45dr"]
na = [int(i) for i in a if i.isdigit()]
print(na)

#4
print("Четвертая задача")
a=[5,67,"tru","well","45",2]
na = [i for i in a for k in range(2)]
print(na)

#5
print("Пятая задача")
n=14
ints=list(range(2,n))
primes=[ints[0]]
for p in ints:
	primes.append(ints[0])
	ints=[i for i in ints if i%p!=0]
	
print(primes)

#6

print("Шестая задача")
n=10
mnoz={(i,n//i) for i in range (1,int(n**1/2)+1) if n%i==0}
b = {j for i in mnoz for j in i}
print(b)

#проверка работы репозитория
