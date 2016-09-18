---
title: Spring框架搭建
---


Spring的不足：

* 配置太多



## 常见问题

### Could not open ServletContext resource [/WEB-INF/applicationContext.xml]

ContextLoaderListener has its own context which is shared by all servlets and filters. By default it will search /WEB-INF/applicationContext.xml。

```XML
<context-param>
    <param-name>contextConfigLocation</param-name>
    <param-value>/WEB-INF/somewhere-else/root-context.xml</param-value>
</context-param>
```

### Missing artifact org.aspectj:aspectjweaver:jar:1.8.0.M1

According to a reported issue at springsource, aspectjweaver is "basically identical to AspectJ 1.7" except that it has early support for Java 8.As I don't need Java 8 support, I basically added a compile dependency to the latest release version of aspectweaver:

```XML
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.7.4</version>
</dependency>
```

This ensures that the 1.7.4 is used instead of the milestone release, and is an acceptable workaround for me, for the time being.


##### Exception java.lang.ClassNotFoundException: org.apache.commons.dbcp.BasicDataSource

在POM.xml中引入jar包。

```XML
<dependency>
    <groupId>commons-dbcp</groupId>
    <artifactId>commons-dbcp</artifactId>
    <version>1.2.2</version>
</dependency>
```

##### java.lang.NoClassDefFoundError: org/apache/ibatis/session/SqlSessionFactory

引入jar包。

```XML
<dependency>
    <groupId>org.apache.ibatis</groupId>
    <artifactId>ibatis-core</artifactId>
    <version>3.0</version>
</dependency>
```



