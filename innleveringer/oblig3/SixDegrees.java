import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Map;

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
            // printShortestPath(graph, "nm2255973", "nm0000460");
            // printShortestPath(graph, "nm0424060", "nm8076281");
            // printShortestPath(graph, "nm4689420", "nm0000365");
            // printShortestPath(graph, "nm0000288", "nm2143282");
            printShortestPath(graph, "nm0637259", "nm0931324");

        } else if (args[0].toLowerCase().equals("chilleste") || args[0].toLowerCase().equals("chillest")) {
            printChillestPath();
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

        System.out.println(formattedString);
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
        if (visited.size() == actors.size()) { // all nodes have been tried, the search is impossible. maybe throw an
                                               // error?
            return null;
        }
        // *this loop should be functional. i thought really hard when i wrote it :)
        for (Movie mov : currentActor.getMovies()) {
            for (Actor act : mov.getActors()) {
                if (!(visited.contains(act))) {
                    ArrayList<Node> newPath = new ArrayList<>(currentPath);
                    newPath.add(mov);
                    newPath.add(act);
                    toVisit.add(newPath);
                }
            }
        }
        ArrayList<Node> next = toVisit.remove();
        return BFSVisit(actors, next, goalID, visited, toVisit);
    }

    public static void printChillestPath() {
    }
}
