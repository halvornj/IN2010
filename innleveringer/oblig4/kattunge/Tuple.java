
public class Tuple<X, Y> {
    X x;
    Y y;

    public Tuple(X x, Y y) {
        this.x = x;
        this.y = y;
    }

    public X getFirst() {
        return x;
    }

    public Y getSecond() {
        return y;
    }

    public void setSecond(Y v) {
        y = v;
    }

    @Override
    public String toString() {
        return (x + " : " + y);
    }

}
