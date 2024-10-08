public class Main {
    public static void main(String[] args) {
        HeshMep<String, Integer> map = new HeshMep<>();
        System.out.println("Adding initial value a:0");
        map.put("a", 0);
        System.out.println(map);
        System.out.println("Adding values b:1, c:3, d:4, e:5");
        map.put("b", 1);
        map.put("c", 3);
        map.put("d", 4);
        map.put("e", 5);
        System.out.println(map);
        System.out.println("changing value a:99");
        map.put("a", 99);
        System.out.println(map);
        System.out.println("removing key c");
        map.remove("c");
        System.out.println(map);
        System.out.println("adding value f:6");
        map.put("f", 6);
        System.out.println(map);
        System.out.println("passing rehash-threshold");
        map.put("g", 7);
        map.put("h", 8);
        map.put("j", 9);
        map.put("k", 10);
        map.put("l", 11);
        map.put("m", 12);
        System.out.println(map);
        map.errorPrint();
        System.out.println("pushing for larger buckets");
        map.put("n", 13);
        map.put("o", 14);
        map.put("p", 15);
        map.put("q", 16);
        map.put("r", 17);
        map.put("s", 18);
        map.put("t", 19);
        map.put("u", 20);
        map.put("v", 21);
        map.put("w", 22);
        map.put("x", 23);
        map.put("y", 24);
        map.put("z", 25);
        map.put("aa", 27);
        map.put("ab", 28);
        map.put("ac", 29);
        map.put("ad", 30);
        map.put("ae", 31);
        map.put("af", 32);
        map.put("ag", 33);
        map.put("ah", 34);
        map.put("ai", 35);
        map.put("aj", 36);
        map.put("ak", 37);
        map.put("al", 38);
        map.put("am", 39);
        map.put("an", 40);
        map.put("ao", 41);
        map.put("ap", 42);
        map.put("aq", 43);
        map.put("ar", 44);
        map.put("as", 45);
        System.out.println(map);
        System.out.println(map.size() + " " + map.getCapacity());

    }
}
