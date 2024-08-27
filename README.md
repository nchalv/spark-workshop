# Workshop Introduction: Hands-On with Apache Spark on YARN

Welcome to the hands-on workshop on Apache Spark, designed specifically for designed specifically for participants of the RELAX Doctoral Network. This workshop will delve into the practical aspects of setting up and running Apache Spark on a YARN-managed cluster using VirtualBox VMs. With the increasing relevance of big data processing in both academic research and industry applications, proficiency in tools like Apache Spark is invaluable. By the end of this workshop, you will have a solid understanding of the Spark ecosystem, and hands-on experience in deploying and managing a Spark cluster.

## Why Apache Spark?

Apache Spark has emerged as a leading framework for large-scale data processing, owing to its versatility, speed, and ease of use. It provides powerful abstractions for distributed data processing, making it a go-to tool for handling complex computational tasks over large datasets. Unlike its predecessor, Apache Hadoop MapReduce, Spark offers in-memory processing, which significantly boosts performance for iterative algorithms common in machine learning and data analysis.

For researchers and data scientists, Spark’s support for various programming languages (Scala, Python, Java, R) and its rich ecosystem (including libraries like MLlib for machine learning, GraphX for graph processing, and Spark SQL for structured data) make it an ideal choice for a wide range of data-driven tasks.
## Workshop Objectives

This workshop will guide you through the complete setup and configuration of an Apache Spark environment on a commodity laptop. Specifically, we will cover:

 -  Setting Up Virtual Machines: Using VirtualBox, we will create a cluster of virtual machines running Ubuntu 22.04.4.
 -  Installing and Configuring Apache Hadoop: Understanding the fundamentals of Hadoop's distributed file system (HDFS) and resource management using YARN (Yet Another Resource Negotiator).
 -  Installing and Configuring Apache Spark: Deploying Spark on top of YARN and configuring it for efficient distributed computing.
 -  Running Spark Jobs on YARN: Submitting and managing Spark jobs in a multi-node environment, exploring how Spark leverages YARN for resource allocation and job scheduling.
 -  Optimizing and Debugging: Techniques for optimizing Spark jobs and debugging common issues encountered in distributed environments.

## Technical Setup

The software stack for this workshop is carefully selected to balance performance and ease of setup on a typical commodity laptop. We will be using:

  - **VirtualBox 7.0.20**: For managing the virtualized environment.
  - **Ubuntu 22.04.4**: As the guest operating system on each VM, providing a stable and robust platform for running Spark and Hadoop.
  - **Apache Hadoop 3.3.6**: Serving as the underlying framework for HDFS and YARN.
  - **Apache Spark 3.5.2**: The latest version of Spark, offering cutting-edge features and performance improvements.

## What to Expect

Throughout the workshop, you will engage in hands-on exercises designed to reinforce key concepts and provide practical experience. You will gain insights into the inner workings of Spark, from data partitioning and task scheduling to memory management and fault tolerance. By the end of this session, you will not only be able to set up and manage a Spark cluster but also understand how to leverage Spark's capabilities for advanced data processing tasks.

We assume that you already have a solid understanding of distributed systems, programming, and data structures, allowing us to dive deep into the technical aspects without spending much time on foundational concepts.
Getting Started

Before we begin, please ensure that you have the required software installed on your laptop. Detailed installation instructions and configuration files will be provided, but a basic familiarity with Linux command-line operations will be beneficial.

Let’s embark on this journey to master Apache Spark and unlock the full potential of distributed data processing!

<div align="center">
	<img src="https://blogs.qub.ac.uk/relax-dn/wp-content/uploads/sites/328/2023/03/cropped-logo-230x230.jpg">
</div>
