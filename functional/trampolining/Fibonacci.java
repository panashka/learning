import java.util.Optional;
import java.util.function.Supplier;

/**
 * @author Eugene Pankov
 * on 19/11/2020
 */
public class Fibonacci {
    public static void main(String[] args) {
//        for (int i = 0; i < 20; i++) {
//            System.out.print(fibonacci(i) + " ");
//        }
//
//        System.out.println("");
//        for (int i = 0; i < 20; i++) {
//            System.out.print(fibonacci2(i, 0, 1) + " ");
//        }

        for (int i = 0; i < 20; i++) {
            System.out.print(trampolinedFibonacci(i, 0, 1).get() + " ");
        }
    }

    /*
        Recursive version
     */
    public static long fibonacci(int n) {
        if (n == 0 || n == 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    /*
        Tail recursive version
     */
    public static long fibonacci2(int n, long a, long b) {
        if (n == 0) {
            return a;
        }

        return fibonacci2(n - 1, b, a + b);
    }

    /*
        Trampolined version which generalizes tail recursion approach
     */
    public static Trampoline<Long> trampolinedFibonacci(int n, long a, long b) {
        return n == 0
                ? Trampoline.done(a)
                : Trampoline.more(() -> trampolinedFibonacci(n - 1, b, a + b));
    }

    public interface Trampoline<T> extends Supplier<T> {
        default Optional<Trampoline<T>> next() {
            return Optional.empty();
        }

        static <T> Trampoline<T> done(T value) {
            return () -> value;
        }

        static <T> Trampoline<T> more(Supplier<Trampoline<T>> next) {
            return new Trampoline<T>() {
                @Override
                public Optional<Trampoline<T>> next() {
                    return Optional.of(next.get());
                }

                @Override
                public T get() {
                    Trampoline<T> trampoline = this;
                    while(trampoline.next().isPresent()) {
                        trampoline = trampoline.next().get();
                    }
                    return trampoline.get();
                }
            };
        }
    }
}
