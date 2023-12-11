#### Lambda表达式

##### 1.基础概念	

​	Lambda就是一个**匿名函数**，使用其主要原因就是为了简化代码。

**使用条件：**

​		当一个接口只有一个非default修饰的方法，即只有一个需要实现的方法，可以使用；

​		有多个非default修饰的方法时，意味着需要实现多个方法，此时Lambda不可以用来实例化接口。

引出：**函数式接口**
    @FunctionalInterface注解。
    当接口中只有一个方法必须被实现时，可以使用@FunctionalInterface注解，表示函数式接口；当有多个方法必须被实现时，使用该注解将报错。

##### 2.语法

**a.基础语法：**
    lambda是一个匿名函数，有： 返回值类型、方法名、参数列表、方法体
  	  ()：描述参数列表。
  	  {}：描述方法体。
  	  ->：lambda运算符，读作goes to

例如：

```Java
TestInterface test = (int a, int b) ->{    return a+b; };
```

**b.语法精简:**

- 参数类型：

  由于在接口中已经规定了参数的类型，因此可以在Lambda表达式中省略参数类型。

  注意，要省略全部省略，不能出现部分省略类型的情况。

  例如：

  ```Java
  TestInterface test = (a, b) ->{    return a+b; };
  ```

- 参数小括号：

  如果参数列表中，参数的数量只有一个，可以省略小括号(）

  例如：

  ```java
  //无返回值单个参数 
  TestInterface test = (int a) -> { System.out.println(a); }; 
  //单个参数省略小括号 
  TestInterface test = a -> { System.out.println(a); };
  ```

- 方法体大括号：

  如果方法体中只有一句，可以省略大括号。

  例如：

  ```java
  //单个参数省略小括号 
  TestInterface test = a -> { System.out.println(a); }; 
  //方法体只有一句，省略大括号 
  TestInterface test = a -> System.out.println(a);
  ```

- 方法体大括号(特殊情况):

  如果方法体中只有一句，且这一句为返回语句，则在省略大括号时，也必须省略 return 关键字。

  例如：

  ```java
  //有返回值单个参数 
  TestInterface test = (int a) -> { return a * 2; }; 
  //方法体只有一个语句，且为return 
  TestInterface test = a -> a * 2;
  ```

**c.语法进阶:**

- 方法引用

  快速的将一个lambda的实现指向一个已经实现的方法。

  语法：

  ​	方法隶属者::方法名
  ​    如果方法是static，隶属者就是类；如果不是static，隶属者就是对象。

  注意：

  ​	被引用方法的参数的数量和类型必须和接口中方法一致。

  ​	被引用方法的返回值必须和接口中方法一致。

  例如：

  ```java
  public class lambdaClass2 { 
      public static void main(String[] args) { 
          //ReturnOneParam是一个接受和返回一个int类型参数的接口，将其直接指向了test()方法
          ReturnOneParam returnOneParam = lambdaClass2::test; 
      } 
      public static int test(int a){
          return a; 
      } 
  }
  ```

- 方法引用-构造方法

  将方法引用语法上，将方法名改为new，意味着构造方法。

  例如：

  ```java
  public class lambdaClass2 { 
      public static void main(String[] args) { 
          //正常简写之后 
          PersonCreator1 personCreator1 = () -> new Person(); 
          //方法引用-构造方法(无参) 
          PersonCreator1 personCreator11 = Person::new; Person byNoParam = personCreator11.createByNoParam(); 
          //方法引用-构造方法(有参) 
          PersonCreator2 personCreator2 = Person::new; Person byParams = personCreator2.createByParams("xiaoming", 20); 
      } 
  } 
  interface PersonCreator1{ 
      Person createByNoParam(); 
  } 
  interface PersonCreator2{ 
      Person createByParams(String name, int age); 
  } 
  class Person{ 
      public String name; 
      public int age; 
      public Person(String name, int age) { 
          this.name = name; this.age = age; 
      } 
      public Person() {
      } 
  }
  ```

------

