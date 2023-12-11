​	`@Transactional` 注解可以用于方法级别或类级别。

​	使用该注解可以将方法或整个类标记为需要进行事务管理的地方。

#### 1.使用步骤：

1. 确保项目中引入了适当的依赖项。通常，`spring-boot-starter-data-jpa` 或 `spring-boot-starter-jdbc` 已经包含了必要的依赖项。
2. 在启动类上添加 `@EnableTransactionManagement` 注解，以启用事务管理功能。这将自动配置一个合适的事务管理器。（可以不添加）
3. 在需要进行事务管理的方法上或类上添加 `@Transactional` 注解，并根据需要配置相关属性。

#### 2.@Transactional：

​	`@Transactional(transactionManager =)` 注解是 Spring Framework 提供的用于事务管理的注解之一。它用于将方法或类标记为需要进行事务管理的地方，并可以配置相关的事务管理器。

​	在 `@Transactional` 注解中，`transactionManager` 属性用于指定要使用的事务管理器。事务管理器负责管理事务的开始、提交或回滚等操作。

​	`transactionManager` 属性的取值通常是一个字符串，用于指定事务管理器的名称或 ID。该名称或 ID 是在 Spring 配置文件或注解配置中定义的事务管理器的 bean 名称。

例如:(已经在 Spring 配置文件中定义了一个名为 "myTransactionManager" 的事务管理器)

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional(transactionManager = "myTransactionManager", readOnly = true)
public class MyService {

    @Transactional
    public void myTransactionalMethod() {
        // 在此方法中执行需要进行事务管理的操作
    }
}
```

#### 3.对于常见的事务管理器的名称，可根据不同情况选择适当的事务管理器：

- DataSourceTransactionManager：用于基于 JDBC 数据源的事务管理。
- HibernateTransactionManager：用于与 Hibernate 框架集成的事务管理。
- JpaTransactionManager：用于与 JPA (Java Persistence API) 框架集成的事务管理。
- JtaTransactionManager：用于 JTA (Java Transaction API) 实现的分布式事务管理。

