import java.util.ArrayList;

public class Tree<T> {

    Node<T> root;

    public Tree() {
        this.root = null;
    }

    public Tree(Node<T> root) {
        this.root = root;
    }

    // all children added will be new created nodes from the TreeBuilder-class, this
    // means we don't have to worry about back-linking or checking for existing
    // nodes
    /**
     * Adds the given array of child nodes to the specified parent node.
     *
     * @param parent   the parent node to add children to
     * @param children the array of child nodes to add
     */
    public void addChildren(Node<T> parent, Node<T>[] children) {
        if (root == null) {
            root = parent;
        }
        parent.addChildren(children);
    }

    /**
     * Returns the path from the current node to the root of the tree.
     * 
     * @param path the current path from the node to the root
     * @return the path from the current node to the root of the tree
     */
    public ArrayList<Node<T>> pathToRoot(ArrayList<Node<T>> path) {
        Node<T> current = path.get(path.size() - 1);
        if (current.parent == null) {
            System.err.println(current);
            System.err.println(current.children);
            return path;
        }
        path.add(current.parent);
        return pathToRoot(path);
    }
}
