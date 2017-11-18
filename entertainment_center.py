import media
import fresh_tomatoes

Shawshank_Redemption = media.Movie("Shawshank Redemption","An innocent man imprisoned for a crime he did not commit learns about life","https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")
Dark_Knight = media.Movie("Dark Knight", "The second part of the epic Batman triology starrring Christian Bale as Batman and Heath ledger as the Joker","https://images-na.ssl-images-amazon.com/images/I/81AJdOIEIhL._SY550_.jpg","https://www.youtube.com/watch?v=yQ5U8suTUw0")
Inception = media.Movie("Inception", "The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious, and is offered a chance to have his criminal history erased as payment for a seemingly impossible tast : Inception , the implantation of another person's idea into a target's subconscious","http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg","https://www.youtube.com/watch?v=8hP9D6kZseM")
Forrest_Gump = media.Movie("Forrest Gump", "The life of Forrest Gump, a slow-witted but kind-hearted, good-natured and athletically prodigious man from Alabama","https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/d1/d14220ee66aeec73c49038385428ec4c_500x735.jpg","https://www.youtube.com/watch?v=uPIEn0M8su0")
Into_The_Wild = media.Movie("Into the wild", "Christopher McCandless, a young graduate, decides to renounce all his possessions and hitchhike across America.", "http://cdn.shopify.com/s/files/1/0151/0741/products/pg1012_1024x1024.jpg?v=1500638917","https://www.youtube.com/watch?v=g7ArZ7VD-QQ")
Rush = media.Movie("Rush","The story about James Hunt and Niki Lauda, two extremely skilled Formula One racers, have an intense rivalry with each other","http://cdn.collider.com/wp-content/uploads/rush-poster-international.jpg","https://www.youtube.com/watch?v=lzNbGH1oZJc")

movies = [Shawshank_Redemption, Dark_Knight, Inception, Forrest_Gump, Into_The_Wild, Rush]
fresh_tomatoes.open_movies_page(movies)
    
