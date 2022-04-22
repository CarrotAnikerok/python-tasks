from bs4 import BeautifulSoup as BS


# task 1

def courses(year, season):
    with open('posov.html', mode='r', encoding='utf8') as f:
        document = BS(f, features="html.parser")
    semester = document.find("nav")
    nav = semester.find_all("a")
    tags = []
    for a in nav:
        href = a.get("href")
        tags.append(href)
    coincidence = []
    for i in tags:
        if i.find(str(year)) != -1 and i.find(season) != -1:
            coincidence.append(i)
    course = []
    for i in coincidence:
        for a in nav:
            if a.get("href") == i:
                course.append(a.text)
    course.pop(0)
    return course

print(courses(21, "spring"))



