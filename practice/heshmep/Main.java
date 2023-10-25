public class Main {
    public static void main(String[] args) {
        HeshMep<String, Integer> map = new HeshMep<>();

        map.put("a", 0);
        System.out.println(map);
        map.put("b", 1);
        map.put("c", 3);
        map.put("d", 4);
        map.put("e", 5);
        System.out.println(map);
        map.put("a", 99);
        System.out.println(map);
        map.remove("c");
        System.out.println(map);
        map.put("f", 6);
    }
}
