class Node<E> {
    HashMap<E, Node<E>> children;
    Node<E> parent;
    E data;

    public Node(E data) {
        this.data = data;
    }

    public void addChildren(Node<E>[] c) {
        for (Node<E> child : c) {
            children.put(child.data, child);
            child.setParent(this);
        }
    }

    public void addChild(Node<E> c) {
        children.put(c.data, c);
        c.setParent(this);
    }

    public void setParent(Node<E> p) {
        parent = p;
    }

    public E value() {
        return data;
    }

    @Override
    public String toString() {
        return data.toString();
    }
}
