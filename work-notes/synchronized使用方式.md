### 1.synchronized 作用介绍：

​	synchronized 是 Java 程序中用于实现线程安全的关键字，其作用是保证同一时间只有一个线程可以访问共享资源，从而避免多个线程同时修改某个共享数据时出现的问题，如数据不一致、数据竞争等。

​	具体而言，当一个方法或代码块被 synchronized 关键字修饰后，它所属的对象（或类对象）将成为锁对象，保证同一时间只有一个线程能够获得该锁对象，其他线程则需要等待。



### 2.针对 synchronized 关键字，可以分为两种锁：

**实例对象锁：**

​	也称为对象锁或监视器锁，是基于对象级别的锁。当使用 synchronized 关键字修饰一个实例方法或使用 synchronized 代码块并以实例对象作为锁定对象时，获取的就是实例对象锁。每个实例对象有各自独立的实例对象锁，不同实例对象之间互不干扰，只有同一个实例对象上的方法调用会竞争该锁。

**类对象锁：**

​	也称为类锁，是基于类级别的锁。当使用 synchronized 关键字修饰一个静态方法或使用 synchronized 代码块并以类对象（通常是通过 Class 对象）作为锁定对象时，获取的就是类对象锁。一个类的类对象锁在整个 JVM 中只有一个，不论有多少个实例对象，它们共享同一个类对象锁。



具体表现为synchronized可以修饰：

1. 普通方法：表示当前对象的实例对象锁，锁定后其他线程无法同时访问当前实例对象的所有被synchronized修饰的方法。
2. 静态方法：表示当前类的锁，锁定后其他线程无法同时访问该类的所有被synchronized修饰的静态方法。
3. 代码块：
   1. 锁定的是变量：表示该变量所代表的实例对象的实例对象锁，与普通方法一致。
   2. 锁定的是类（即类名.class）：表示锁定的是对应类锁，与静态方法类似。



### 3.具体使用方式：

**修饰实例方法：**

​	当 synchronized 关键字用于修饰普通方法时，表示锁定的是实例对象。即对于同一个实例对象，不同的线程在访问该实例对象的 synchronized 实例方法时会相互排斥，保证了同一时间只有一个线程可以执行该方法。

​	注意，是该对象的所有被synchronized 修饰的普通方法同时只允许一个线程使用。

~~~java
public synchronized void sMethod2(){
        System.out.println("synchronized方法2执行");
    }
~~~

**修饰静态方法：**

​	当 synchronized 关键字用于修饰一个静态方法时，表示锁定的是类对象。即对于同一个类对象，不同的线程在访问该类对象的 synchronized 静态方法时会相互排斥，保证了同一时间只有一个线程可以执行该方法。

​	注意，是该类的所有被synchronized 修饰的静态方法同时只允许一个线程使用。

~~~ java
public static synchronized void staticSMethod2(){
        System.out.println("synchronized静态方法2执行");
    }
~~~

**修饰代码块：**

​	当 synchronized 关键字用于修饰一个代码块时，需要指定一个锁对象作为参数。

​	该锁对象可以是任意对象。对于同一个锁对象，不同的线程在访问使用该锁对象包裹的代码块时会相互排斥，保证了同一时间只有一个线程可以执行该代码块。

锁对象为对象实例：

​	与修饰实例方法类似，只是锁的实例对象锁可以指定了，如下例子即为锁定的指定Object类型的对象lock

~~~ java
public class MyClass {
    private Object lock = new Object();

    public int test() {
        synchronized (lock) {
            return lock;
        }
    }
}
~~~

锁对象为类：

​	如下例子中，method1和method2其实就是同一把锁，都是A类的类锁。

~~~ java
public class A {
    public static synchronized void method1() {
        // ...
    }

    public static void method2() {
        synchronized(A.class) {
            // ...
        }
    }
}
~~~

