---
title: Spring MVC源码调试
tags: Spring
date: 2016-09-17 13:55:08
---


这里调试Spring MVC的环境是：

* Windows 7

* Eclipse Java EE IDE for Web Developers,Version: Neon Release (4.6.0).Build id: 20160613-1800

* JDK 1.8

* Spring MVC 4.2.3

* Apache Tomcat 8.0

想了解平时学习的理论知识在实际的代码实现中是什么情况，比较好的方式是阅读源码，如果能在阅读过程中根据疑问动手调试源码验证猜想和疑问，那就更加完美了。这里想看Spring MVC一个HTTP请求从开始到结束到底是怎么运行的，Spring MVC怎么处理，选取了4.2.3版本的源码进行调试。

<!-- more -->

首先从GitHub上下载4.2.3版本的源码，在项目的Maven Dependencies找到名为spring-webmvc-4.2.3.REALEASE的jar包，单击右键build-path-->Configure build path,在Libraries中找到对应的jar包，选中source attachment-->Edit.

{% asset_img springmvc-attach-source.png Spring MVC关联源码%}

在spring-webmvc-4.2.3.REALEASE.jar中找到dispatchservlet类，打断点即可进入调试。