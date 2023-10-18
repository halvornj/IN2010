import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.HashSet;

public class GraphBuilder {

    public static void main(String[] args) {
        String actor_filePath = "six-degrees-of-imdb-ressursside/actors.tsv";
        String movie_filePath = "six-degrees-of-imdb-ressursside/movies.tsv";
        if (args.length == 1) {
            if (args[0].toLowerCase().equals("marvel")) {
                actor_filePath = "six-degrees-of-imdb-ressursside/marvel_actors.tsv";
                movie_filePath = "six-degrees-of-imdb-ressursside/marvel_movies.tsv";
            }

        }
        HashMap<String, HashSet<Node>> nodes = populateGraph(actor_filePath, movie_filePath);
        // actors-set now contains all actors, which are connected to their respective
        // movies
        HashSet<Node> actors = nodes.get("actors");
        HashSet<Node> movies = nodes.get("movies");

        printGraphSize(nodes);
    }

    public static HashMap<String, HashSet<Node>> populateGraph(String actor_tsv_filePath, String movie_tsv_filePath) {
        HashSet<Node> actors = new HashSet<Node>();
        HashMap<String, Movie> movies = new HashMap<String, Movie>();
        String line;

        // *trying the movie-node-aproach. first create all movies, then connect actors
        // to said movies.
        try (BufferedReader reader = new BufferedReader(new FileReader(movie_tsv_filePath))) {
            while ((line = reader.readLine()) != null) {
                // løsningen hadde vært bedre med en dedikert TSV-parser, men finner ingen i
                // javas standard-bibliotek.

                String[] fields = line.split("\\t");

                Movie mov = new Movie(fields[0], fields[1], Double.parseDouble(fields[2]), Integer.parseInt(fields[3]));
                movies.put(mov.getID(), mov);
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }
        try (BufferedReader reader = new BufferedReader(new FileReader(actor_tsv_filePath))) {
            while ((line = reader.readLine()) != null) {
                String[] fields = line.split("\\t");
                Actor a = new Actor(fields[0], fields[1]);
                for (int i = 2; i < fields.length; i++) {
                    Movie movie = movies.get(fields[i]);
                    if (movie != null) {
                        a.addMovie(movie);
                        movie.addActor(a);
                    }
                }
                actors.add(a);
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(1);
        }

        HashMap<String, HashSet<Node>> map = new HashMap<>();
        map.put("actors", actors);
        map.put("movies", new HashSet<Node>(movies.values()));

        return map;
    }

    public static void printGraphSize(HashMap<String, HashSet<Node>> graph) {
        int movieNodeCount = graph.get("movies").size();
        int actorNodeCount = graph.get("actors").size();
        int edgeCount = 0;
        for (Node movieNode : graph.get("movies")) {
            Movie movie = (Movie) movieNode;
            edgeCount += movie.getActors().size();
        }

        System.out.println("Movie Nodes: " + movieNodeCount);
        System.out.println("Actor Nodes: " + actorNodeCount);
        System.out.println("edges: " + edgeCount);
    }
}
