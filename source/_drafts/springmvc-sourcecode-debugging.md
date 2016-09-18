---
title: Spring MVC源码调试
tags: Spring
---

这里调试Spring MVC的环境是：

* OS: Windows 7

* IDE: Eclipse Java EE IDE for Web Developers,Version: Neon Release (4.6.0).Build id: 20160613-1800

* JDK 1.8

* Spring MVC 4.2.3

* Apache Tomcat 8.0

想了解平时学习的理论知识在实际的代码是如何实现的，比较好的方式是阅读源码，如果能在阅读过程中根据疑问动手调试源码验证猜想和疑问，那就更加完美了。如果想看看Spring MVC一个HTTP请求从开始到结束到底是怎么运行的，经过了那些流程和步骤，Spring MVC怎么处理，这里选取了4.2.3版本的源码进行源码的调试。

首先从GitHub上下载spring-Framework 4.2.3版本的源码（jar包的版本和源码对应），在项目的Maven Dependencies找到名为spring-webmvc-4.2.3.REALEASE的jar包，单击右键build-path-->Configure build path,在Libraries中找到对应的jar包，选中source attachment-->Edit，将对应版本的源码附加到对应的jar包上.

{% asset_img springmvc-attach-source.png Spring MVC关联源码%}

在spring-webmvc-4.2.3.REALEASE.jar中找到dispatchservlet类，打断点，在前端页面中随意请求一个页面，即可命中断点进入调试，接下来就可以观察Spring MVC如何handle请求了。