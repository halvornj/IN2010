import java.util.HashMap;
import java.util.HashSet;

public class Hovedprogram {
    public static void main(String[] args) {
        System.out.println("---bygger grafen---");
        HashMap<String, HashSet<Node>> graph = GraphBuilder.populateGraph("six-degrees-of-imdb-ressursside/actors.tsv",
                "six-degrees-of-imdb-ressursside/movies.tsv");
        // oppgave 1.2
        GraphBuilder.printGraphSize(graph);

        System.out.println("\n---korteste vei---");
        SixDegrees.printShortestPath(graph);

        System.out.println("\n---chilleste vei---");
        SixDegrees.printChillestPath(graph);

        System.out.println("\n---komponenter---");
        Komponenter.findComponentSizes(graph);
    }
}
