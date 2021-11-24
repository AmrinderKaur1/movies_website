from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CREATE A DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-webb.db"
# optional- but will silent the deprecation warning in the console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TODO: create table to add movie in the database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


# TODO: CREATE A NEW TABLE IN THE SAME DATABASE TO ADD FAVOURITE MOVIES INTO IT.
class FavorMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    # ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


# TODO: ADD MOVIES IN THE DATABASE TABLE MOVIE👇

# After adding the new_movie the code needs to be commented out/deleted.
# So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="Caller was the most liked character.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# new_movie = Movie(
#     title="The Shawshank Redemption",
#     year=1994,
#     description="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
#     rating=9.3,
#     ranking=9,
#     review="Great for halloween nights scary kinda movie.",
#     img_url="https://i.pinimg.com/736x/b1/dd/9f/b1dd9f13822549b23064ca77914e74bb.jpg"
#
# )
# new_movie = Movie(
#     title="The Godfather",
#     year=1972,
#     description="The Godfather follows Vito Corleone Don of the Corleone family as he passes the mantel to his son Michael.",
#     rating=9.2,
#     ranking=8,
#     review="From it's stellar opening wedding scene to it's bittersweet conclusion, The Godfather is a groundbreaking and brilliantly made film.",
#     img_url="https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"
#
# # )
# new_movie = Movie(
#     title="The Dark Knight",
#     year=2008,
#     description="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
#     rating=9.0,
#     ranking=7,
#     review="The Dark Knight is one of the finest films ever made. It's an entertaining comic book movie, a compelling crime drama.",
#     img_url="https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg"
#
# )
# new_movie = Movie(
#     title="Soorarai Pottru",
#     year=2020,
#     description="Nedumaaran Rajangam 'Maara' sets out to make the common man fly and in the process takes on the world's most capital intensive industry and several enemies who stand in his way.",
#     rating=9.1,
#     ranking=6,
#     review="Soorarai Pottru is one of the best movie of surya. such an excellent making by sudha kongara.",
#     img_url="https://m.media-amazon.com/images/M/MV5BOGVjYmM0ZWEtNTFjNi00MWZjLTk3OTItMmFjMDAzZWU1ZDVjXkEyXkFqcGdeQXVyMTI2Mzk1ODg0._V1_.jpg"
#
# )
# new_movie = Movie(
#     title="The Lord of the Rings: The Return of the King",
#     year=2003,
#     description="Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
#     rating=8.9,
#     ranking=5,
#     review="The Return of the King is widely regarded as one of the greatest and most influential films ever made.",
#     img_url="https://m.media-amazon.com/images/M/MV5BZGMxZTdjZmYtMmE2Ni00ZTdkLWI5NTgtNjlmMjBiNzU2MmI5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_FMjpg_UX1000_.jpg"
#
# )
# new_movie = Movie(
#     title="12 Angry Men ",
#     year=1957,
#     description="The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.",
#     rating=9.0,
#     ranking=4,
#     review="To create such a riveting story in the confines of a solitary room is a victory unto itself.",
#     img_url="https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_QL75_UX190_CR0,6,190,281_.jpg"
#
# )
# new_movie = Movie(
#     title="Pulp Fiction ",
#     year=1994,
#     description="The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
#     rating=8.9,
#     ranking=3,
#     review="It is considered such a great movie because it was something that the audience had never seen before.",
#     img_url="https://i.pinimg.com/originals/e7/48/2b/e7482b62d42b691a7e0f37facba1796b.jpg"
#
# )
# new_movie = Movie(
#     title="The Matrix",
#     year=1999,
#     description="When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
#     rating=9.1,
#     ranking=2,
#     review="The Matrix is a top-notch action movie on top of being science fiction.",
#     img_url="https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg"
#
# )
# new_movie = Movie(
#     title="Interstellar",
#     year=2014,
#     description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
#     rating=8.9,
#     ranking=1,
#     review="It is the best sci-fi movie ever.",
#     img_url="https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg"
#
# )
#
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)


@app.route("/fav")
def fav():
    movie_id = request.args.get("id")
    exists = FavorMovie.query.filter_by(id=movie_id).first() is not None

    if exists:
        # True
        my_movies = FavorMovie.query.all()
        return render_template('fav.html', my_movies=my_movies, exist=exists)

    if not exists:
        # False - add movie to the FavorMovies record
        movie = Movie.query.get(movie_id)
        new_fav = FavorMovie(
            title=movie.title,
            year=movie.year,
            description=movie.description,
            rating=movie.rating,
            review=movie.review,
            img_url=movie.img_url
        )
        db.session.add(new_fav)
        db.session.commit()

        # read all the movies from FavorMovies table
        my_movies = FavorMovie.query.all()

        return render_template('fav.html', my_movies=my_movies, exist=exists)


@app.route("/un-favourite")
def un_favourite():
    movie_id = request.args.get("id")
    movie = FavorMovie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
