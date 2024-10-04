

class Movie:
    def __init__(self,title,release,director,rating,genre,cast):
        self.title=title
        self.release=release
        self.director=director
        self.rating=rating
        self.genre=genre
        self.cast=cast
    def __str__(self):
        return f"Title: {self.title}\nRelease: {self.release}\nDirector: {self.director}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {self.cast}\n"
    def alphabetical(self,movielist):
        list=movielist.copy()
        newlist=[]
        for _ in range(len(list)):
            min=list[0]
            for i in list:
                if i.title<min.title:
                    min=i
            newlist.append(min)
            list.remove(min)
        return newlist
    def chronilogical(self,movielist):
        list=movielist.copy()
        newlist=[]
        for _ in range(len(list)):
            min=list[0]
            for i in list:
                if i.release<min.release:
                    min=i
            newlist.append(min)
            list.remove(min)
        return newlist
    def searchgenre(self,movielist,genre):
        list=movielist.copy()
        newlist=[]
        for i in list:
            if genre.lower() in i.genre.lower():
                newlist.append(i)
        return newlist
    def searchdirector(self,movielist,director):
        list=movielist.copy()
        newlist=[]
        for i in list:
            if director.lower() in i.director.lower():
                newlist.append(i)
        return newlist
    def searchcast(self,movielist,cast):
        list=movielist.copy()
        newlist=[]
        for i in list:
            for k in i.cast:
                if cast.lower() in k.lower():
                    newlist.append(i)
                    break
        return newlist

f=open("movie list","r")
movies=f.read()
f.close()
movies2=[]
temp=""
for i in movies:
    if i!="\n":
        temp+=i
    else:
        movies2.append(temp)
        temp=""
movies2.append(temp)
movies3=[]
tempmov=[]
temp=""
brak=False
for i in movies2:
    for k in i:
        if k=="[" or k=="]":
            if brak:
                brak=False
            else:
                brak=True
            temp+=k
        elif k!="," or brak:
            temp+=k
        else:
            tempmov.append(temp)
            temp=""
    tempmov.append(temp)
    movies3.append(tempmov)
    tempmov=[]
    temp=""
m=[]
for i in movies3:
    newlist=[]
    temp=""
    newcomma=False
    for k in i[5][2:-1]:
        if newcomma and k==" ":
            pass
        elif k!=",":
            temp+=k
            newcomma=True
        else:
            newlist.append(temp)
            temp=""
    newlist.append(temp)
    m.append(Movie(i[0],int(i[1][2:-1]),i[2][1:],i[3][1:],i[4][1:],newlist))
print(movies3)
print()
for i in m:
    print(i)



"""
m=[Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"]),

    Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]),

    Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),

    Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]),

    Movie("The Matrix", 1999, "Lana Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]),

    Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"]),

    Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),

    Movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"]),

    Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]),

    Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta", "Joe Pesci"]),

    Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"]),

    Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]),

    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]),

    Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]),

    Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"]),

    Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks", "Matt Damon", "Tom Sizemore"]),

    Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"]),

    Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"]),

    Movie("The Lion King", 1994, "Roger Allers", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"]),

    Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"]),

    Movie("Inglourious Basterds", 2009, "Quentin Tarantino", "R", "War", ["Brad Pitt", "Christoph Waltz", "Mélanie Laurent"]),

    Movie("The Sixth Sense", 1999, "M. Night Shyamalan", "PG-13", "Thriller", ["Bruce Willis", "Haley Joel Osment", "Toni Collette"]),

    Movie("The Usual Suspects", 1995, "Bryan Singer", "R", "Mystery", ["Kevin Spacey", "Gabriel Byrne", "Chazz Palminteri"]),

    Movie("Memento", 2000, "Christopher Nolan", "R", "Thriller", ["Guy Pearce", "Carrie-Anne Moss", "Joe Pantoliano"]),

    Movie("Braveheart", 1995, "Mel Gibson", "R", "Biography", ["Mel Gibson", "Sophie Marceau", "Patrick McGoohan"]),

    Movie("The Terminator", 1984, "James Cameron", "R", "Sci-Fi", ["Arnold Schwarzenegger", "Linda Hamilton", "Michael Biehn"]),

    Movie("Back to the Future", 1985, "Robert Zemeckis", "PG", "Adventure", ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"]),

    Movie("Alien", 1979, "Ridley Scott", "R", "Horror", ["Sigourney Weaver", "Tom Skerritt", "John Hurt"]),

    Movie("The Truman Show", 1998, "Peter Weir", "PG", "Drama", ["Jim Carrey", "Laura Linney", "Noah Emmerich"])
   ]
"""
mo=m.copy()
def help():
    print("A.Alphabetical sort")
    print("B.Chronilogical Sort")
    print("1.Search Genre")
    print("2.Search Director")
    print("3.Search Cast")
    print("4.refresh list")
    print("?.Show help screen")
help()
while True:
    inp=input(">>> ").lower()
    if inp=="?":
        help()
    elif inp=="a":
        m=m[0].alphabetical(m)
        for i in m:
            print(i)
    elif inp=="b":
        m=m[0].chronilogical(m)
        for i in m:
            print(i)
    elif inp=="1":
        inp=input("What genre: ")
        if len(m[0].searchgenre(m,inp))>0:
            m=m[0].searchgenre(m,inp)
            for i in m:
                print(i)
        else:
            print("Genre not found")
    elif inp=="2":
        inp=input("What Director: ")
        if len(m[0].searchdirector(m,inp))>0:
            m=m[0].searchdirector(m,inp)
            for i in m:
                print(i)
        else:
            print("director not found")
    elif inp=="3":
        inp=input("What Actor: ")
        if len(m[0].searchcast(m,inp))>0:
            m=m[0].searchcast(m,inp)
            for i in m:
                print(i)
        else:
            print("cast not found")
    elif inp=="4":
        m=mo.copy()
        for i in m:
            print(i)