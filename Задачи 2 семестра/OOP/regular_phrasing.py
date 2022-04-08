import re

#task 1

def right_email(a):
   sample = r"[a-z0-9_-]+@[a-z0-9_-]+\.([a-z]{2,})"
   if re.fullmatch(sample, a) is not None:
       print("Сопоставилось")
   else:
       print("Неее")


line = "v5ik_-a4@yandex.ru"
right_email(line)

#task 2

def number(a):
    sample = r'\+?([-\s()]*\d){7,11}'
    for m in re.finditer(sample, a):
        print(m)
    #comp_sample = re.compile(sample)
    #print(comp_sample.findall(a))?
    #print(re.findall(sample, a))?

s = "Привет привет как дела я не знаю о смотри +34578128 даааа вот так вот о смотри еще есть 456627-3 5-6 такие вот номера да а еще +8 (913)-45-64 ну и 46"
number(s)

#task 3

def spaces(a):
    sample = r"\s+,"
    f = re.findall(sample,a)
    for i in f:
        a = a.replace(i, ",")
    return a

print(spaces(("Привет    , друг  , мой друг")))

#task 4

def backward(a):
    sample = r"(A-Za-z)+-(A-Za-z)+"
    return re.findall(sample, a) #не работает

print(backward("Wha-aaaat are yo-ou doing?"))

#task 5

def cat(a):
    sample = r"(^|\s)*(К|к)(О|о)(Т|т)($|\s)+"
    n =0
    for m in re.finditer(sample, a):
        n+=1
    return(n)

print(cat("КоТ а еще есть который кот и конечно Кот же еще некоторый кот кот"))



