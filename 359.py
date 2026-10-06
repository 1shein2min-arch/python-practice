import json

try :
    with open("movie.json","r") as file :
        movies = json.load(file)

except FileNotFoundError :
    movies = []

except json.JSONDecodeError :
    movies = []

def save_data(movies) :
    with open ("movie.json","w") as file :
        json.dump(movies,file,indent=4)

def add_movie(movies,title,year,genre,rating) :
    movie = {
        "title" : title ,
        "year" : year ,
        "genre" : genre ,
        "rating" : rating
    }
    
    movies.append(movie)
    save_data(movies)

def view_movies(movies) :
    for movie in movies :
        print(f"{movie['title']} - {movie['year']} - {movie['genre']} - {movie['rating']}")

def update_rating(movies,title,rating) :
    for movie in movies :
        if movie["title"] == title :
            movie["rating"] = rating
            save_data(movies)
            break

def delete_movie(movies,title) :
    for movie in movies :
        if movie["title"] == title :
            movies.remove(movie)
            save_data(movies) 
            break

def search_movie(movies,title,genre) :
    for movie in movies :
        if movie["title"] == title and movie["genre"] == genre:
            print(f"{movie['title']} - {movie['year']} - {movie['genre']} - {movie['rating']}")

def movie_summary(movies) :
    total_movie = 0
    total_rating = 0
    average_rating = 0
    for movie in movies :
        total_rating = total_rating + movie["rating"]
        total_movie = total_movie + 1

    average_rating = total_rating/total_movie

    print(f"Total Movies : {total_movie}")
    print(f"Total Rating : {total_rating}")
    print(f"Average Rating : {average_rating}")

def top_rate_movie(movies) :
    for movie in movies:
        if movie["rating"] >= 8 :
           print(f"{movie['title']} - {movie['year']} - {movie['genre']} - {movie['rating']}")

def update_genre(movies,title,genre):
    for movie in movies :
        if movie["title"] == title :
            movie["genre"] = genre
            save_data(movies)
            break

def update_year(movies,title,year) :
    for movie in movies :
        if movie["title"] == title :
            movie["year"] = year
            save_data(movies)
            break

while True :
    print("===== Movie Management =====")

    print("1. Add Movie")
    print("2. View Movies")
    print("3. Update Rating")
    print("4. Delete Movie")
    print("5. Search Movie ")
    print("6. Top Rate Movie")
    print("7. Update Genre")
    print("8. Update Year")
    print("9. Summary")
    print("10. Exit")

    while True :
        try :
            choice = int(input("Enter Choose :"))
            break
        except ValueError:
            print("Please Enter Number")

    if choice == 1 :
        title = input("Enter Title :")
        year = input("Enter Year :")
        genre = input("Ente Genre :")
        while True :
            try :
                rating = float(input("Enter Rating"))
                if rating <= 0 :
                    print("Rating Must Be Greater Than 0")
                    continue
                break
            except ValueError :
                print("Please Enter Number")

        add_movie(movies,title,year,genre,rating)

    elif choice == 2 :
        view_movies(movies)

    elif choice == 3 :
        title = input("Enter Title :")
        while True :
            try :
                rating = float(input("Enter Rating :"))
                if rating <= 0 :
                    print("Rating Must Be Greater Than 0")
                    continue
                break
            except ValueError :
                print("Please Enter Number")  
        update_rating(movies,title,rating)  

    elif choice == 4 :
        title = input("Enter Title :")
        delete_movie(movies,title)

    elif choice == 5 :
        title = input("Enter Title :")
        genre = input("Enter Genre :")
        search_movie(movies,title,genre)

    elif choice == 6 :
        top_rate_movie(movies)

    elif choice == 7 :
        title = input("Enter Title :")
        genre = input("Enter Genre :")
        update_genre(movies,title,genre)

    elif choice == 8 :
        title = input("Enter Title :")
        while True :
            try :
                year = int(input("Enter Year :"))
                if year <= 0 :
                    print("Year Must Be Positive")
                    continue
                break
            except ValueError :
                print("Please Enter Number")
        update_year(movies,title,year)

    elif choice == 9 :
        movie_summary(movies)

    elif choice == 10 :
        print("Goodbye !")
        break

    else :
        print("Invalid Choice")



