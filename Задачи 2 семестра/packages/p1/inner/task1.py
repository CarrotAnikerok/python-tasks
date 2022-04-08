#Дано n, нарисуйте шахматную доску из 1 и 0 размера n×n. Например, при n = 7:

def doska(n):
	stroka = ""
	for i in range(1, n+1):
		if i%2==0:
			stroka+= "01"*((n+1)//2) + "\n"
		if i%2!=0:
			stroka+= "10"*((n+1)//2) + "\n"
		if n%2!=0:
			stroka = stroka[0:len(stroka)-2] + "\n"
	return stroka


			

