#xgv3cj Christian Camacho
def get_name(movie):
    return movie[0]

'''This function returns the name of the movie from the list given the movie name'''
def get_gross(movie):
    return movie[1]
'''This function returns the gross earnings of the movie from the list given the movie name'''

def get_rating(movie):
    return movie[3]

'''This function returns the rating of the movie from the list given the movie name'''
def get_num_ratings(movie):
    return movie[4]

'''This function returns the number of ratings from the list given the movie name'''

def better_movies(movie_name, movie_list):
    bettermovie = []
    for c in movie_list:
        if movie_name == c[0]:
            for j in movie_list:
                if get_rating(j) > get_rating(c):
                    bettermovie.append(j)
    return bettermovie
'''This function returns the movies who have a higher rating than 
the given movie from the list '''

def average(category, movies_list):
    global totalm
    sum = 0
    if category == 'rating':
        for movie in movies_list:
            sum += (get_rating(movie))
            totalm = len(movies_list)
    if category == 'gross':
        for movie in movies_list:
            sum += (get_gross(movie))
            totalm = len(movies_list)
    elif category == 'number of ratings':
        for movie in movies_list:
            sum += (get_num_ratings(movie))
            totalm = len(movies_list)
    return sum / totalm
'''This function returns the averages of number of ratings or rating or gross earnings 
of all the movies from the provided list'''

