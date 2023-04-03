import pandas as pd
import time
import random 


#welcome message giving info about the chatbot and storing the user's name.
def welcome():
    global user
    print('welcome to the movie chatbot!')
    time.sleep(2)

    user = input('Hi what is your name? ')
    print('')
    time.sleep(1)

    print(f'Hello {user}, I am the movie chatbot i can help you find the perfect movie for you !!')
    print('I am going to ask you a few questions so i can get general idea of what types of movies you are looking for!\n')
    time.sleep(5)

def goodbye():
    print(f'thank you {user} i hope you are satisfied with my service, enjoy your movie!')
    print('''★─▄█▀▀║░▄█▀▄║▄█▀▄║██▀▄║─★
★─██║▀█║██║█║██║█║██║█║─★
★─▀███▀║▀██▀║▀██▀║███▀║─★
★───────────────────────★
★───▐█▀▄─ ▀▄─▄▀ █▀▀──█───★
★───▐█▀▀▄ ──█── █▀▀──▀───★
★───▐█▄▄▀ ──▀── ▀▀▀──▄───★''')

def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')

while True: #main loop

    welcome()
    movie_list = pd.read_csv('movies.csv')
    directors = movie_list['director'] #returns the directors column and their index number in the csv file
    #print(directors)
    director_name_list = []

    for index, movie in movie_list.iterrows():
        name = directors[index]
        if type(name) == str:
            director_name_list.append(name)

    #print(director_name_list)
    selected_director = input('Name a director that you like: ')
    print('')

    director_movies_list = []
    if director_name_list.__contains__(selected_director):
        #returns every data record where the director = the selected director 
        director_movies = movie_list.loc[movie_list['director'] == selected_director]
        #print(director_movies)
        print(f'Here is a list of all the movies {selected_director} has directed:')
        for movie in director_movies['title']:
            director_movies_list.append(movie)
            print(director_movies_list.index(movie) +1, movie)

        
        
        while True:
            choice = input('Have you found your desired movie? y/n: ')
            print()
            if choice == 'y':
                while True:
                    choice = input('please enter the movie number you want to watch, or rand if you want a randomly selected movie from this list: ')
                    print('...') 
                    time.sleep(1)      
                    print('...')
                    time.sleep(1)      
                    print('...')
                    time.sleep(1)
                    print()                   
                    if choice == 'rand':
                        random_choice = random.choice(director_movies_list)
                        random_movie = director_movies.loc[director_movies['title'] == random_choice]
                        print(f'oohhh so you are feeling a bit spontaneous today? i see i see... well here is a great {selected_director} movie that i think you should try: {random_choice}')
                        time.sleep(2)
                        print('Here is an overview of the movie: ')
                        
                        print_full(random_movie['overview'])
                        time.sleep(4)
                        print()

                        goodbye()
                        break
                    
                    #checking if input is a number within the index of genre_movies
                    elif choice.isdigit():
                        if int(choice) > len(director_movies_list)+1:
                            print('please give a number within the given options')
                        else:
                            chosen_movie = director_movies.loc[director_movies['title'] == director_movies_list[int(choice)-1]]
                            print(f'great choice this movie is one of my favourites! Heres an overview of the movie: ')
                            time.sleep(2)
                            print_full(chosen_movie['overview'])
                            time.sleep(4)
                            print()
                            goodbye()
                            break
                    
                    else:
                        print('please give a number within the given options')

            elif choice == 'n':
 #list of our genre specific movies
                genre_movies = []
                user_genre = input('lets narrow down your options, what genre would you like to watch? ')
                director_movies['genres'] = director_movies['genres'].str.split(' ')
                
                for index, movie in director_movies.iterrows():
                    if user_genre in movie['genres']:
                        genre_movies.append(movie['title'])

                print()
                if len(genre_movies) == 0:
                    random_choice = random.choice(director_movies_list)
                    print(f'''Unforunately {selected_director} does not have any movies in that genre :( let me recommend another one of {selected_director}'s movies instead.
                    How about {random_choice}?''')
                    time.sleep(2)
                    print()
                    print(f"Here is an overview of {random_choice}:")
                    random_movie = director_movies.loc[director_movies['title'] == random_choice]
                    print_full(random_movie['overview'])
                    time.sleep(4)
                    print()
                    goodbye()

                    break 
                elif len(genre_movies) == 1:
                    chosen_movie = director_movies.loc[director_movies['title'] == genre_movies[0]]
                    print(print(f"{user_genre}? Wow i love that genre too, here is {selected_director}'s {user_genre} movie:"))
                    for i in genre_movies:
                        print(genre_movies.index(i) +1, i)
                    print(f'i love this movie!! Here is an overview of {genre_movies[0]}:')
                    print_full(chosen_movie['overview'])
                    time.sleep(4)
                    print()

                    goodbye()
                    break


                elif len(genre_movies) >=2 :
                    print(f"{user_genre}? Wow i love that genre too, here is a list of {selected_director}'s {user_genre} movies:")
                    for i in genre_movies:
                        print(genre_movies.index(i) +1, i)

                    while True:
                        choice = input('please enter the movie number you want to watch, or rand if you want a randomly selected movie from this list: ')
                        print()                    
                        if choice == 'rand':
                            random_choice = random.choice(genre_movies)
                            random_movie = director_movies.loc[director_movies['title'] == random_choice]
                            print(f'oohhh so you are feeling a bit spontaneous today? i see i see... well here is a great {selected_director} {user_genre} movie that i think you should try: {random_choice}')
                            time.sleep(2)
                            print()
                            print('here is an overview of the movie: ')
                            print_full(random_movie['overview'])
                            time.sleep(4)
                            print()
                            goodbye()
                            break
                        
                        #checking if input is a number within the index of genre_movies
                        elif choice.isdigit():
                            if int(choice) > len(genre_movies)+1:
                                print('please give a number within the given options')
                            else:
                                chosen_movie = director_movies.loc[director_movies['title'] == genre_movies[int(choice)-1]]
                                print(f'great choice this movie is one of my favourites! Heres an overview of the movie: ')
                                print_full(chosen_movie['overview'])
                                time.sleep(5)
                                print()
                                goodbye()
                                break
                        
                        else:
                            print('please give a number within the given options')

            else:
                print("please enter 'y' or 'n'")
                continue
        
            break

    else:
        print(f"I do not have {selected_director}'s films in my database")
    break
