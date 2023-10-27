import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Set<Integer> set = new Set<>();
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int outLineN = 0;
        for (int i = 0; i < n; i++) {
            String[] input = sc.nextLine().split(" ");
            String command = input[0];
            int arg = 0;

            if (input.length > 1) {
                arg = Integer.parseInt(input[1]);
            }
            switch (command) {
                case "contains":
                    System.out.println(set.contains(arg));
                    outLineN++;
                    break;
                case "insert":
                    if (outLineN > 74 && outLineN < 80) {
                        System.out.println("outline: " + outLineN + " command: " + command + "(" + arg + ")");
                    }
                    set.insert(arg);
                    break;
                case "remove":
                    if (outLineN > 74 && outLineN < 80) {
                        System.out.println("outline: " + outLineN + " command: " + command + "(" + arg + ")");
                    }
                    set.remove(arg);
                    break;
                case "size":
                    System.out.println(set.size());
                    outLineN++;
                    break;
            }
        }

    }

}
