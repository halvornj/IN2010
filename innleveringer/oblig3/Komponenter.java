import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;

public class Komponenter {
    public static void main(String[] args) {
        HashMap<String, HashSet<Node>> graph = GraphBuilder.populateGraph(
                "six-degrees-of-imdb-ressursside/actors.tsv",
                "six-degrees-of-imdb-ressursside/movies.tsv");

        HashSet<Node> allActors = graph.get("actors");
        System.out.println(allActors.size());
        HashMap<Integer, Integer> componentSizes = new HashMap<>(); // key is the num of nodes in a component, value is
                                                                    // the num of components with said node-count.
        while (!allActors.isEmpty()) {
            Actor start = (Actor) allActors.iterator().next();
            Stack<Actor> stack = new Stack<>();
            stack.push(start);
            int count = 0;
            HashSet<Actor> visited = new HashSet<>();
            while (!stack.isEmpty()) {
                Actor current = stack.pop();
                if (!visited.contains(current)) {
                    visited.add(current);
                    count++;
                    allActors.remove(current);
                    for (Actor neighbour : current.getNeighbourActors()) {
                        stack.push(neighbour);
                    }
                }
            }
            componentSizes.put(count, componentSizes.getOrDefault(count, 0) + 1);
        }

        System.out.println("aaaaaaaaa");
        for (Integer i : componentSizes.keySet()) {
            System.out.println("There are " + componentSizes.get(i) + " components of size " + i + ".");
        }
    }
}
