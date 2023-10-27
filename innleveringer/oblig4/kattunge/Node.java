class Node<E> {
    Node<E>[] children;
    Node<E> parent;
    E data;

    public Node(E data) {
        this.data = data;
    }

    public void addChildren(Node<E>[] c) {
        children = c;
        for (Node<E> child : children) {
            child.setParent(this);
        }
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
