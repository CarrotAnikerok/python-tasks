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
    comp_sample = re.compile(sample)
    print(comp_sample.findall(a))

s = "Привет привет как дела я не знаю о смотри +34578128 даааа вот так вот о смотри еще есть 456627-3 5-6 такие вот номера да а еще +8 (913)-45-64 ну и 46"
number(s)




