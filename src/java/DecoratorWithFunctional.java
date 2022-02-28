// 用函数式实现 python decorator 的效果
import java.lang.Runnable;

public class DecoratorWithFunctional {
    public void decorator(Runnable runnable) {
        System.out.println("method start");
        runnable.run();
        System.out.println("method end");
    }

    public static void main(String[] args) {
        new DecoratorWithFunctional().decorator(()->{
            System.out.println("method run")
        })
    }
}