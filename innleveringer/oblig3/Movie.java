import java.util.ArrayList;

public class Movie implements Node {
    public final String ID;
    public final String title;
    public final double rating;
    public final int votes;
    ArrayList<Actor> actors;

    public Movie(String ID, String title, double rating, int votes) {
        this.ID = ID;
        this.title = title;
        this.rating = rating;
        this.votes = votes;
        actors = new ArrayList<Actor>();
    }

    public String getID() {
        return ID;
    }

    public String getTitle() {
        return title;
    }

    public Double getRating() {
        return rating;
    }

    public int getVotes() {
        return votes;
    }

    public ArrayList<Actor> getActors() {
        return actors;
    }

    public void addActor(Actor a) {
        actors.add(a);
    }

    @Override
    public String toString() {
        return "[" + title + " (" + rating + ")" + "]";
    }
}
