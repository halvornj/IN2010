import java.util.Scanner;
import java.util.ArrayList;

abstract class Main {
    @SuppressWarnings("unchecked")
    public static void main(String[] args) {
        Tree<Integer> tree = new Tree<>();
        HashMap<Integer, Node<Integer>> nodes = new HashMap<>();
        Scanner sc = new Scanner(System.in);
        int cat_position = Integer.parseInt(sc.nextLine());
        String input = "";
        while (!(input = sc.nextLine()).equals("-1")) {
            String[] split = input.split(" ");
            int parentInteger = Integer.parseInt(split[0]);
            Node<Integer> parent = nodes.get(parentInteger);
            if (parent == null) {// wasn't found in dict. means node is root of a component.
                parent = new Node<Integer>(parentInteger);
                nodes.put(parentInteger, parent);
            }
            Node<Integer>[] children = (Node<Integer>[]) new Object[split.length - 1];

            for (int i = 1; i < split.length; i++) {
                Node<Integer> child = new Node<Integer>(Integer.parseInt(split[i]));
                children[i - 1] = (child);
                nodes.put(Integer.parseInt(split[i]), child);
            }
            tree.addChildren(parent, children);
        }

        // tree is now built, now we make the search.
        ArrayList<Node<Integer>> path = new ArrayList<>();
        path.add(nodes.get(cat_position));
        path = tree.pathToRoot(path);
        String pathStr = "";
        for (Node<Integer> node : path) {
            pathStr += node + " ";
        }
        pathStr = pathStr.trim();

        System.out.println(pathStr);
    }
}