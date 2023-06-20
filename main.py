
import pandas as pd

usernames = ['user_id', 'gender', 'age', 'occupation', 'zip']

users = pd.read_table('./ml-1m/users.dat', sep='::',
                      header=None, names=usernames, engine='python')

ratingnames = ['user_id', 'movie_id', 'rating', 'timestamp']

ratings = pd.read_table('./ml-1m/ratings.dat', sep='::',
                        header=None, names=ratingnames, engine='python')

movienames = ['movie_id', 'title', 'genres']

movies = pd.read_table('./ml-1m/movies.dat', sep='::', header=None,
                       names=movienames, engine='python', encoding='latin-1')

#
print('\nThe first 5 rows of movies are:')
print(movies[:5])
print('*' * 40)
# ****************************************************
print('\nTher first 5 rows of users are:')
print(users[:5])
print('*' * 40)
# ****************************************************
print('\nThe first 5 rows of ratings are:')
print(ratings[:5])
print('*' * 40)
# ****************************************************

data = pd.merge(pd.merge(ratings, users), movies)

print("\nThe number of records in 'movies.dat' are:", len(movies.index))

print("\nThe number of records in 'users.dat' are:", len(users.index))

print("\nThe number of records in 'ratings.dat' are:", len(ratings.index))

print("\nThe number of records in 'data.dat' are:", len(data.index))

ocupation = ['0 other/not specified', '1 academic/educator', '2 artist', '3 clerical/admin', '4 college/grad student',
             '5 customer service', '6 doctor/health care', '7 executive/managerial', '8 farmer', '9 homemaker',
             '10 K-12 student', '11 lawyer', '12 programmer', '13 retired', '14 sales/marketing', '15 scientist',
             '16 self-employed', '17 technician/engineer', '18 tradesman/craftsman', '19 unemployed', '20 writer']

for i in range(21):
    data['occupation'].replace(to_replace=i, value=ocupation[i], inplace=True)

print("\nThe last Ten rows of the Dataframe data are:")
print(data[-10:])

print("\nThe 5 occupations that give higher ratings for movies are:")
print(data.occupation.value_counts()[:5])
