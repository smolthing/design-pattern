import io.reactivex.rxjava3.core.Observable;


class MemoryLeak {
    public static void main(String[] args) {
        // Create an Observable that emits a list of strings
        Observable<String> sourceObservable = Observable.just("Hello", "RxJava", "FlatMap");

        // Use flatMap to transform each string into individual characters and flatten them
        sourceObservable
                .flatMap(s -> Observable.fromArray(s.split(""))) // Transform into individual characters
                .flatmap(character -> System.out.println("Character: " + character));
    }
}