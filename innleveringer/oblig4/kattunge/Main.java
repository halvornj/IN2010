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
            for (String s : split) {
                System.err.println("!" + s + "!");
            }
            int parentInteger = Integer.parseInt(split[0]);
            Node<Integer> parent = null;
            if (nodes.size() == 0) {// wasn't found in dict. means node is root of a component.
                parent = new Node<Integer>(parentInteger);
                nodes.put(parentInteger, parent);
            }
            parent = nodes.get(parentInteger);

            for (int i = 1; i < split.length; i++) {
                Node<Integer> child = new Node<Integer>(Integer.parseInt(split[i]));
                parent.addChild(child);
                nodes.put(Integer.parseInt(split[i]), child);
            }

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

        // !temp
        System.err.println(tree.root);
    }
}