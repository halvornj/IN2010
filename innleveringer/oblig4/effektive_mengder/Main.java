import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Set<Integer> set = new Set<>();
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
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
                    break;
                case "insert":
                    set.insert(arg);
                    break;
                case "remove":
                    set.remove(arg);
                    break;
                case "size":
                    System.out.println(set.size());
                    break;
            }
        }
    }
}
