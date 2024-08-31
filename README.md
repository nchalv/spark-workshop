# Workshop Introduction: Hands-On with Apache Spark on YARN

Welcome to the hands-on workshop on Apache Spark, designed for the participants of the RELAX Doctoral Network. This workshop will delve into the theoretical and architectural concepts upon which Apache Spark has been built, as well as the practical aspect of setting up and running Apache Spark on a YARN-managed cluster using VirtualBox VMs. With the increasing relevance of big data processing in both academic research and industry applications, proficiency in tools like Apache Spark is invaluable. By the end of this workshop, you will have a solid understanding of the Spark ecosystem, and hands-on experience in deploying and managing a Spark cluster.

## Why Apache Spark?

Apache Spark has emerged as a leading framework for large-scale data processing, owing to its versatility, speed, and ease of use. It provides powerful abstractions for distributed data processing, making it a go-to tool for handling complex computational tasks over large datasets. Unlike its predecessor, Apache Hadoop MapReduce, Spark offers in-memory processing, which significantly boosts performance for iterative algorithms common in machine learning and data analysis.

For researchers and data scientists, Spark’s support for various programming languages (Scala, Python, Java, R) and its rich ecosystem (including libraries like MLlib for machine learning, GraphX for graph processing, and Spark SQL for structured data) make it an ideal choice for a wide range of data-driven tasks.

## Workshop Objectives
This workshop is addressed to an audience with a strong technical background. Therefore, its goal is not to highlight every detail of the software stack featured here or its individual components. Instead, it serves as an introduction, providing accurate information and assistance with some of the most obscure technical details one can face as a new Apache Spark user. We will focus on some of Spark's cornerstone concepts, make a quick introduction on how to set up and configure a full-fledged, albeit limited in terms of resources, distributed cluster and, finally, expose the ways in which the command line tools that Spark offers out-of-the-box can be leveraged for application development and testing purposes. The material available here is organised in a manner that will optimise the familiarity levels of participants in a short span of time.

The goal is to provide a safe and isolated environment where experimentation is encouraged as people get more acquainted with the concepts and programming mannerisms of Spark. The latter, the task of learning how to write efficient Spark applications, is left to the participants entirely.  

## Structure
The material available here is organised in three discreet parts. This structure will not follow a linear path, as the guide that covers the prerequisites delves into some very technical details, without discussing them in length. However, this approach will allow participants to take their time setting up their own isolated working environments which will be used and explained in great detail later. The second and third parts will be presented in person and cover a relatively short introduction and the application of lessons learned in a real use case.

### Prerequisites
#### [00. Apache Spark over YARN installation guide](https://github.com/nchalv/spark-workshop/blob/main/00.%20Apache%20Spark%20over%20YARN%20installation%20guide.md)
This part is entirely dedicated to providing participants with all necessary information on how to set up and configure an Apache Spark distributed cluster running over YARN from scratch. To achieve that, we have chosen to utilise Oracle's VirtualBox, a powerful, cross-platform virtualization software that enables developers and IT professionals to run multiple operating systems simultaneously on a single physical machine, facilitating testing, development, and deployment in diverse environments. 

Specifically, we will cover:

 -  Setting Up Virtual Machines: Using VirtualBox, we will create a small cluster of virtual machines running Ubuntu 22.04.4.
 -  Installing and Configuring Apache Hadoop: Understanding the fundamentals of Hadoop's distributed file system (HDFS) and resource management using YARN (Yet Another Resource Negotiator).
 -  Installing and Configuring Apache Spark: Deploying Spark on top of YARN and configuring it for efficient distributed computing.

Although it is preferable that this part will have already been completed by the time the Spark training session take place, there will be time and guidance for people who failed to complete it to catch up.


### Part I - Introduction
#### [Apache Spark](https://github.com/nchalv/spark-workshop/blob/main/Apache%20Spark.pdf)
#### [01. Basic Command-Line Operations on HDFS](https://github.com/nchalv/spark-workshop/blob/main/01.%20Basic%20HDFS%20operations.md)
#### [02. Running Spark Applications and Command-Line Configurations](https://github.com/nchalv/spark-workshop/blob/main/02.%20Running%20Spark%20Applications%20and%20Command-Line%20Configurations.md)
#### [03. [Introduction to Programming in Spark using Python](https://github.com/nchalv/spark-workshop/blob/main/03.%20Introduction%20to%20Programming%20in%20Spark%20using%20Python.md)
The first part of this hands-on session will focus on providing participants with all necessary background information on the basics of Apache Spark and the Hadoop ecosystem. Through dedicated guides and examples, participants can grasp the most important elements of the popular framework. Additional information on how to use HDFS and an introduction to programming in Spark is given. The second part of the session will focus on participants taking the lead and using their newly acquired skills to implement queries using real datasets.


### Part III - Hands-On Session
#### [04. Advanced Analytics on Los Angeles Crime Data](https://github.com/nchalv/spark-workshop/blob/main/04.%20Advanced%20Analytics%20on%20Los%20Angeles%20Crime%20Data.md)
The second part of the workshop focuses on giving participants the time and space to hone their data analytics skills using a real, publicly available data set. Since this course isn't focused on teaching participants how to actually write Spark code, solutions to the suggested queries to be implemented are provided for reference. 


## What to Expect

Throughout the workshop, you will engage in hands-on exercises designed to reinforce key concepts and provide practical experience. You will gain insights into the inner workings of Spark, from data partitioning and task scheduling to memory management and fault tolerance. By the end of this session, you will not only be able to set up and manage a Spark cluster but also understand how to leverage Spark's capabilities for advanced data processing tasks.

We assume that you already have a solid understanding of distributed systems, programming, and data structures, allowing us to dive deep into the technical aspects without spending much time on foundational concepts.

## Getting Started

Before we begin, please ensure that you have the required software installed on your laptop. Detailed installation instructions and configuration files will be provided, but a basic familiarity with Linux command-line operations will be beneficial.

Let’s embark on this journey to master Apache Spark and unlock the full potential of distributed data processing!

<div align="center">
	<img src="https://blogs.qub.ac.uk/relax-dn/wp-content/uploads/sites/328/2023/03/cropped-logo-230x230.jpg">
</div>
