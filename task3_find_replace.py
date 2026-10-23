
s = "Python - лучший язык. Учу Python каждый день!"
print("Python" in s, "python" in s)
print(s.find("Python"), s.find("Python",1))
print(s.find("Java"))
print(s.count("Python"))
rus_s = s.replace("Python","Питон",)
print(rus_s)
ukr_s = s.replace("Python","Питон",1)
print(ukr_s)

a = "Клуб"
b = "клуб"
print(a == b,a.lower == b.lower, a.upper == b.upper)

phrase = "А роза упала на лапу Азора"
clean_phrase = phrase.lower().replace(" ", "")
print(clean_phrase == clean_phrase[::-1])
sec_phrase = "Привет, Мир"
clean_sec = sec_phrase.lower().replace(" ","")
print(clean_sec == clean_sec[::-1])
