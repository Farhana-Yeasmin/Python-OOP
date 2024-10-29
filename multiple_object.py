"""

"""

class Movie(object):
    def __init__(self,title,mins,hero):
        self.title=title
        self.runtime=mins
        self.hero=hero
    
    def printer(self):
        print(f"Title is : {self.title}\n runtime is: {self.runtime}\n hero is: {self.hero}")

lisst_of_movies=[]

while True:
    title = input("Enter the title of movie: ")
    mins= input("Enter the runtime of movie: ")
    hero= input("Enter the name of hero movie: ")
    obj=Movie(title,mins,hero)
    lisst_of_movies.append(obj)
    print("Movie added into the the list")
    ans=input("Do you want to adda nother movie(y/n)")
    if ans!='y':
        break

print("All movie information")

for obj in lisst_of_movies:
    obj.printer()
    