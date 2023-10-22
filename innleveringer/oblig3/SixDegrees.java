import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Map;
import java.util.List;
import java.util.PriorityQueue;

public class SixDegrees {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println(
                    "error: kjør programmet med argument \"korteste\"/\"shortest\" for korteste vei, eller \"chilleste\"/\"chillest\" for chilleste vei.");
            System.exit(1);
        }
        HashMap<String, HashSet<Node>> graph = GraphBuilder.populateGraph(
                "six-degrees-of-imdb-ressursside/actors.tsv",
                "six-degrees-of-imdb-ressursside/movies.tsv");

        if (args[0].toLowerCase().equals("korteste") || args[0].toLowerCase().equals("shortest")) {
            printShortestPath(graph, "nm2255973", "nm0000460");
            printShortestPath(graph, "nm0424060", "nm8076281");
            printShortestPath(graph, "nm4689420", "nm0000365");
            printShortestPath(graph, "nm0000288", "nm2143282");
            printShortestPath(graph, "nm0637259", "nm0931324");

        } else if (args[0].toLowerCase().equals("chilleste") || args[0].toLowerCase().equals("chillest")) {
            printChillestPath(graph);
        } else {
            System.out.println(
                    "error: gjennkjenner ikke argumentet. vennligst kjør programmet med enten \"korteste\" eller \"chilleste\" som argument, for hhv. korteste og chilleste sti mellom 2 skuespillere.");
            System.exit(1);
        }
    }

    public static void printShortestPath(HashMap<String, HashSet<Node>> graph, String id1, String id2) {
        Actor startActor = null;
        HashSet<Node> actors = graph.get("actors");
        for (Node actorNode : actors) {
            Actor actor = (Actor) actorNode;
            if (actor.getID().equals(id1)) {
                startActor = actor;
                break;
            }
        }
        if (startActor == null) {
            System.out.println("error: fant ikke skuespillere med id du spesifiserte. avslutter programmet...");
            System.exit(1);
        }

        ArrayList<Node> startPath = new ArrayList<>();
        startPath.add(startActor);
        ArrayList<Node> path = BFSVisit(graph.get("actors"), startPath, id2, new HashSet<>(), new LinkedList<>());
        String formattedString = path.get(0).toString();
        for (int i = 1; i < path.size(); i++) {
            formattedString += "===>";
            formattedString += path.get(i);
        }

        System.out.println(formattedString + "\n");
    }

    // *trenger ikke bry oss om å besøke alle komponenter, om nodene ikke er i samme
    // komponent er søket umulig. fang dette utenfor.

    /**
     * @param actors      a set of all actors in the graph. only used for
     *                    size-comparison, could be optimized.
     * @param currentPath an arrayList of all nodes from the start-node, leading to
     *                    the current node in the search.
     * @param goalID      the ID of the actor we want to find.
     * @param visited     a set of all the visited nodes so far.
     * @param toVisit     a queue of the nodes to visit, with their paths as the
     *                    arrayList. the acual node will always be the last element
     * @return the path from the startnode, to the end-node, with all actor- and
     *         movie-nodes in between.
     */
    public static ArrayList<Node> BFSVisit(HashSet<Node> actors, ArrayList<Node> currentPath,
            String goalID,
            HashSet<Node> visited, Queue<ArrayList<Node>> toVisit) {
        Actor currentActor = (Actor) currentPath.get(currentPath.size() - 1);
        visited.add(currentActor);
        if (currentActor.getID().equals(goalID)) {
            return currentPath;
        }
        // all nodes have been tried, the search is impossible. maybe throw an error?
        if (visited.size() == actors.size()) {
            return null;
        }
        // *this loop should be functional. i thought really hard when i wrote it :)
        for (Movie mov : currentActor.getMovies()) {
            for (Actor act : mov.getActors()) {
                if (!(visited.contains(act))) {
                    ArrayList<Node> newPath = new ArrayList<>(currentPath);
                    newPath.add(mov);
                    newPath.add(act);
                    if (act.getID().equals(goalID)) {
                        return newPath;
                    }
                    toVisit.add(newPath);
                }
            }
        }
        ArrayList<Node> next = toVisit.remove();
        return BFSVisit(actors, next, goalID, visited, toVisit);
    }

    @SuppressWarnings("unchecked")
    public static void printChillestPath(HashMap<String, HashSet<Node>> graph) {
        HashMap<String, List<HashMap>> startActors = new HashMap<>();
        HashMap<String, Actor> stopActorLinks = new HashMap<>();
        // startLoop
        for (Node actNode : graph.get("actors")) {
            Actor actor = (Actor) actNode;
            if (actor.getID().equals("nm2255973")) {
                startActors.put(actor.getID(), weightedSearch(actor));
            } else if (actor.getID().equals("nm0424060")) {
                startActors.put(actor.getID(), weightedSearch(actor));
            } else if (actor.getID().equals("nm4689420")) {
                startActors.put(actor.getID(), weightedSearch(actor));
            } else if (actor.getID().equals("nm0000288")) {
                startActors.put(actor.getID(), weightedSearch(actor));
            } else if (actor.getID().equals("nm0637259")) {
                startActors.put(actor.getID(), weightedSearch(actor));
            } else if (actor.getID().equals("nm0000460")) {
                stopActorLinks.put("nm2255973", actor);
            } else if (actor.getID().equals("nm8076281")) {
                stopActorLinks.put("nm0424060", actor);
            } else if (actor.getID().equals("nm0000365")) {
                stopActorLinks.put("nm4689420", actor);
            } else if (actor.getID().equals("nm2143282")) {
                stopActorLinks.put("nm0000288", actor);
            } else if (actor.getID().equals("nm0931324")) {
                stopActorLinks.put("nm0637259", actor);
            }
            if (startActors.size() == 5 && stopActorLinks.size() == 5) {
                break;
            }
        }

        for (String startID : startActors.keySet()) {
            HashMap<Node, Node> parents = startActors.get(startID).get(0);
            HashMap<Node, Double> weights = startActors.get(startID).get(1);
            ArrayList<Node> path = new ArrayList<>();
            Node current = stopActorLinks.get(startID);
            while (current != null) {
                path.add(current);
                current = parents.get(current);
            }
            Collections.reverse(path);
            System.out.println(path);
            System.out.println(weights.get(stopActorLinks.get(startID)));
        }

    }

    // ja dette er et raw hashmap, og det er vell strengt tatt ulovlig, men er den
    // enkleste måten å jukse og få tupler i java.
    // kunne jeg importert javatuples-library, men jeg gidder ikke begynne å styre
    // med pom.xml. dette er ikke et java-fag, algoritmen fungerer som den skal.
    public static List<HashMap> weightedSearch(Actor start) {
        HashMap<Node, Node> parents = new HashMap<>();
        HashMap<Node, Double> distances = new HashMap<>();
        List<HashMap> tuple = Arrays.asList(parents, distances);
        parents.put(start, null);
        distances.put(start, 0.0);
        PriorityQueue<Actor> queue = new PriorityQueue<>(100000, new Comparator<Node>() {
            @Override
            public int compare(Node node1, Node node2) {
                if (distances.get(node1) < distances.get(node2)) {
                    return -1;
                }
                if (distances.get(node1) > distances.get(node2)) {
                    return 1;
                }
                return 0;
            }
        });
        queue.add(start);
        while (!queue.isEmpty()) {
            Actor current = queue.remove();
            for (Movie mov : current.getMovies()) {
                for (Actor neighbour : mov.getActors()) {
                    Double c = distances.get(current) + weight(mov);
                    if (c < distances.getOrDefault(neighbour, Double.POSITIVE_INFINITY)) {
                        distances.put(neighbour, c);
                        queue.add(neighbour);
                        parents.put(neighbour, mov);
                        parents.put(mov, current);
                    }
                }
            }
        }
        return tuple;
    }

    private static double weight(Movie m) {
        return 10 - m.getRating();
    }
}
