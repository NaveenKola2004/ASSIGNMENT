#Problem 1: Supermarket Cart Management

cart = ["Apples", "Bananas", "Grapes", "Chocolates"]
cart[0]="Milk"
cart.pop()
k=cart.reverse()
cart.reverse()
print(cart)

#Problem 2: Playlist Organizer

songs = ["Song1", "Song2", "Song3", "Song4"]
songs.append("Song5")
print(songs[2:])

#Problem 3: GPS Coordinates

loacation=(17.3850, 78.4867, 2.1)
latitude,longitude,altitude=loacation
altitude_meter=round(altitude*1000)
value=latitude,longitude,altitude_meter
print(value)

#Problem 4: Student Attendance

class_A = {101, 102, 103, 104, 105}
class_B = {103, 104, 106, 107}
print("Common : ",class_A.intersection(class_B))
print("only  A :",class_A-class_B)
print("Totle unique :",class_B.union(class_A))

#Problem 5: Email Username Extractor

email=input()
email=email.split('@')[0].upper()
print(email)

#Problem 6: Bakery Profit Calculation

#Problem 7: Sentence Reversal
sentance="hello naveen kola"
sentance=sentance.split()
rev=' '.join(reversed(sentance))
print(rev)

#Problem 8: Favorite Fruits
friend1 = {"Apple", "Banana", "Grapes"}
friend2 = {"Grapes", "Mango", "Orange"}
print("common : ",friend1.intersection(friend2))
print("friend1",friend1-friend2)
print("Total unique : ",friend1|friend2)

#Problem 9: Movie Ratings
movies = [("Inception", 9.0), ("Titanic", 8.8), ("Avatar", 7.9), ("Interstellar", 9.2)]

movie_name,ratings=movies[3][0:]
con=ratings<10

print(movies[3])
print(movies[0:3])

#Problem 10: Shopping Discounts
price=int(input())
discount=price*0.10
total_price=price-discount
print(total_price)

#Problem 11: Stock Market Analysis
prices = [150, 200, 250, 180, 300, 220]
print("maxprice : ",max(prices))
print("minmum :",min(prices))
print("difference : ",max(prices)-min(prices))
prices.sort()
print("sort : ",prices)

#Problem 13: Movie Ratings Processing
ratings = [9.0, 8.8, 7.9, 9.2, 8.5]
print(f"maxrating : ",max(ratings))
print(f"minrating : {min(ratings)}")

print(f"total_ratings : {sum(ratings):.1f}")
ratings=sum(ratings)/len(ratings)
print(f"Average_ratings : {ratings:.2f}")