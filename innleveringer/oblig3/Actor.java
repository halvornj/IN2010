import java.util.ArrayList;

public class Actor implements Node {

    public final String ID;
    public final String name;

    ArrayList<Movie> movies;

    public Actor(String ID, String name) {
        this.ID = ID;
        this.name = name;
        movies = new ArrayList<Movie>();
    }

    public String getID() {
        return ID;
    }

    public String getName() {
        return name;
    }

    public ArrayList<Movie> getMovies() {
        return movies;
    }

    public void addMovie(Movie mov) {
        movies.add(mov);
    }

    public ArrayList<Actor> getNeighbourActors() {
        ArrayList<Actor> ls = new ArrayList<>();
        for (Movie mov : movies) {
            for (Actor act : mov.getActors()) {
                ls.add(act);
            }
        }
        return ls;
    }

    @Override
    public String toString() {
        return name;
    }
}