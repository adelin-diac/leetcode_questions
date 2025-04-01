public class Fibonacci {
    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }

    public static void main(String[] args) {
        long startTime = System.nanoTime();
        fibonacci(40);
        long endTime = System.nanoTime();

        System.out.println("Time taken: " + (endTime - startTime) / 1e9 + "seconds");
    }
}
