### 0. Virtual Machines Creation and OS setup

Among the prerequisites for the hands-on training session on Apache Spark is i) the creation of Virtual Machines (VMs) and ii) the configuration the working environment. A detailed guide follows.

*Please keep in mind that the requirements in terms of processing resources and storage capacity might be significant, so make sure that your computer can support them.*


#### 0.1 Virtual Machines Creation
The first step is the creation of two Virtual Machines (VMs), using Oracle VM VirtualBox software (https://www.virtualbox.org/). Oracle VM VirtualBox is a free and open-source virtualization software developed by Oracle Corporation. It allows users to create and manage virtual machines (VMs) on their computers, enabling them to run multiple operating systems simultaneously on a single physical machine.

In this guide, we suggest that two VMs are created, using the official Ubuntu Server LTS 22.04 image provided by Canonical (https://releases.ubuntu.com/jammy/ubuntu-22.04.4-live-server-amd64.iso).

 You are encouraged to create 2 VMs with the following characteristics:
 - Ubuntu Server LTS 22.04 OS
 - 2 CPUs
 - 4GB RAM
 - 15GB disk capacity


It is recommended that you name your VMs "**controller**" and "**worker**" respectively. During the operating system installation, you will be prompted to provide a username. It is advised that you select "**ubuntu**" as your username for both machines. The screenshots and code snippets that follow, assume this convention.

![image](https://github.com/user-attachments/assets/76d2a448-4480-42df-87df-c2684210c5f4)

![image](https://github.com/user-attachments/assets/543545a1-be9d-4865-93de-8df2a67a8e8c)

![image](https://github.com/user-attachments/assets/2da700ff-c167-46ad-be65-83799a342de2)

![image](https://github.com/user-attachments/assets/9c1827b9-c2df-4ff8-81bf-0f423b0ff2c0)


#### 0.2 OS setup
You next need to finalise your options and proceed to install your VMs' Operating System.
The next screenshots will help guide you through this process.

![image](https://github.com/user-attachments/assets/2e1363ac-dc5a-4932-a766-c7e7e0aa6af3)

![image](https://github.com/user-attachments/assets/38f20270-bddc-4be6-a95a-6dfd3fe79fa6)

![image](https://github.com/user-attachments/assets/5f644697-07d3-40d1-9cad-57ffc96b15ba)

![image](https://github.com/user-attachments/assets/1d992fc0-cd33-42de-83b8-dd9df351dfcf)

![image](https://github.com/user-attachments/assets/fa8c1f03-8437-4f44-8c68-926b77dd9e5d)

![image](https://github.com/user-attachments/assets/ddc1e682-02a5-48ce-9629-88054130a991)

![image](https://github.com/user-attachments/assets/09c50da7-3c8a-42fa-bedf-bafe158b62e5)

![image](https://github.com/user-attachments/assets/3381633e-9ce4-44e6-ab94-470b1ac2f5d6)

![image](https://github.com/user-attachments/assets/b4038daa-f253-44e3-8b94-be45c7faf686)

![image](https://github.com/user-attachments/assets/db370568-8073-47bf-b6d5-e9f76989ff62)


Make sure that the OpenSSH server will be installed in both virtual machines.

![image](https://github.com/user-attachments/assets/0c68d8b4-d3d4-4519-a3f0-32a285bceb69)

![image](https://github.com/user-attachments/assets/f797f126-8b33-4ab4-8efa-3be57487ace8)


After the installation. reboot your VMs, as prompted.

![image](https://github.com/user-attachments/assets/222ae915-ab47-40f6-aa5f-ac846bad7761)


### 1. Network and connectivity tools configuration

#### 1.1 Network configuration

Once the Operating System installation process has been completed, make sure to select "**Bridged Adpapter**" from your VMs network menu.

![image](https://github.com/user-attachments/assets/7329caa8-1524-46f1-9938-12a5dd68e368)

The IP addressess which are attatched to our VMs can be discovered using the following command:

```bash
ip a | grep "inet "
```
The output indicates that the controller is accessible through `192.168.1.9`.
```text
    inet 127.0.0.1/8 scope host lo
    inet 192.168.1.9/24 metric 100 brd 192.168.1.255 scope global dynamic enp0s3
```
Similarly, for the worker we get:

```text
    inet 127.0.0.1/8 scope host lo
    inet 192.168.1.10/24 metric 100 brd 192.168.1.255 scope global dynamic enp0s3
```

The output indicates that the worker is accessible through `192.168.1.10`.

These IP addresses of your private network to both machines need to be available to them. Edit the `/etc/hosts` file of both servers to include that information. The final state of the `/etc/hosts` file for both VMs should be identical and consistent with the following template:

```text
127.0.0.1       localhost
192.168.0.xxx   controller
192.168.0.xxx   worker


# The following lines are desirable for IPv6 capable hosts
::1             localhost ip6-localhost ip6-loopback
ff02::1         ip6-allnodes
ff02::2         ip6-allrouters
```


#### 1.2 SSH access

For our distributed services to maintain communication between the nodes, we need to establish SSH connectivity between them. Connect to the controller and create a new cryptographic key that will be used for the controller node to access both itself and the worker via the SSH protocol. The next command adds the newly created key to the list of keys which are allowed to connect to the local machine :
```bash
ssh-keygen -t rsa #press [ENTER] as many times as promted
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
Print the contents of the controller's public key in the terminal with the following command:
```bash
cat ~/.ssh/id_rsa.pub #@controller to print the controller's key
```
Then connect to the worker and add the controller's public key to the `authorized_keys` list:
```bash
vim ~/.ssh/authorized_keys #@worker: copy the above output, paste it here, save and quit
```
Confirm that SSH connectivity from the controller to both VMs.
```bash
ssh controller
ssh worker
```

### 2. Installation and configuration of Apache Spark over YARN on the small cluster of Virtual Machines
**Note:** The following instructions assume that the actions described above in the same guide have been followed faithfully. Students are free to change the given pieces of code as per their own preferences in the configuration.

#### 2.1 Java Installation
We continue with the installation of Apache Hadoop on our new cluster. Initially, we need to install the Java version supported by the official repositories of our operating system on all nodes:
```
sudo apt install default-jdk -y
```
Successful installation can be verified with the following command:
```
java -version
```
#### 2.2 Installation of Hadoop and Apache Spark
In order to install the latest versions of Apache Spark and Hadoop, we create the `~/opt` directory where we will store the executables of the latest versions of the two Apache projects.
```bash
mkdir ./opt
mkdir ./opt/bin
```
Next, we download the compressed files from the official websites of both projects, extract their contents, move them to the `~/opt/bin` directory, and create links in the main  `~/opt` directory.
```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xvzf hadoop-3.3.6.tar.gz
mv hadoop-3.3.6 ./opt/bin
wget https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
tar -xvzf spark-3.5.2-bin-hadoop3.tgz
mv ./spark-3.5.2-bin-hadoop3 ./opt/bin/
cd ./opt
ln -s ./bin/hadoop-3.3.6/ ./hadoop
ln -s ./bin/spark-3.5.2-bin-hadoop3/ ./spark
cd
rm hadoop-3.3.6.tar.gz
rm spark-3.5.2-bin-hadoop3.tgz
mkdir ~/opt/data
mkdir ~/opt/data/hadoop
mkdir ~/opt/data/hdfs
```

#### 2.3 Configuration of environment variables
To configure environment variables, you will initially edit the `~/.bashrc` file using your preferred text editor. This file is executed every time a terminal connection to your virtual machines is opened. You can add the following lines to it:
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64  #Value should match: dirname $(dirname $(readlink -f $(which java)))
export HADOOP_HOME=/home/ubuntu/opt/hadoop
export SPARK_HOME=/home/ubuntu/opt/spark
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin:$SPARK_HOME/bin;
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
export LD_LIBRARY_PATH=/home/ubuntu/opt/hadoop/lib/native:$LD_LIBRARY_PATH
export PYSPARK_PYTHON=python3
```
Make sure to save the changes to the ~/.bashrc file after adding these lines.
To update the environment, execute the following command to apply the changes from the script:
```bash
source ~/.bashrc
```
#### 2.4 Hadoop Distributed File System configuration
The Hadoop configuration files are located in the `/home/ubuntu/opt/hadoop/etc/hadoop` directory. Since we've already set the `HADOOP_HOME` variable to point to the `/home/ubuntu/opt/hadoop` directory, we refer to the same path by writing: `$HADOOP_HOME/etc/hadoop/`. Below, we record the changes that need to be made:

Start by editing `$HADOOP_HOME/etc/hadoop/hadoop-env.sh`, where the following line needs to be added:
```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

Next, edit `$HADOOP_HOME/etc/hadoop/core-site.xml` so that it contains the following:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/home/ubuntu/opt/data/hadoop</value>
        <description>Parent directory for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS </name>
        <value>hdfs://controller:54310</value>
        <description>The name of the default file system. </description>
    </property>
</configuration>
```
Also. replace the contents of `$HADOOP_HOME/etc/hadoop/hdfs-site.xml` with the following lines:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
        <description>Default block replication.</description>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/home/ubuntu/opt/data/hdfs</value>
    </property>
</configuration>
```
Finally, create a new file, `$HADOOP_HOME/etc/hadoop/workers` and edit it to contain these two lines:
 ```text
 controller
 worker
 ```
That way, we register both VMs as workers. In our cluster, the controller will also act as one.


#### 2.5 Starting HDFS
Start HDFS using the following commands:
 ```bash
 $ $HADOOP_HOME/bin/hdfs namenode -format
 $ start-dfs.sh
 ```
Confirm that the process was successful by accessing the web interface on the master's public IP using a browser: `http://192.168.1.xxx:9870`. 2 available live nodes should be accounted for.

#### 2.6 Hadoop YARN configuration
Edit `$HADOOP_HOME/etc/hadoop/yarn-site.xml`, the contents of which need to be the following:

```xml
<?xml version="1.0"?>
<configuration>
<!-- Site specific YARN configuration properties -->
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>controller</value>
    </property>
    <property>
        <name>yarn.resourcemanager.webapp.address</name>
        <!--Insert the public IP of your master machine here. Please change this line!!!-->
        <value>192.168.1.xxx:8088</value>
    </property>
    <property>
        <name>yarn.nodemanager.resource.memory-mb<gz/name>
        <value>1024</value>
    </property>
    <property>
        <name>yarn.scheduler.maximum-allocation-mb</name>
        <value>3072</value>
    </property>
    <property>
        <name>yarn.scheduler.minimum-allocation-mb</name>
        <value>128</value>
    </property>
    <property>
        <name>yarn.nodemanager.vmem-check-enabled</name>
        <value>false</value>
    </property>
   <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle,spark_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.spark_shuffle.class</name>
        <value>org.apache.spark.network.yarn.YarnShuffleService</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.spark_shuffle.classpath</name>
        <value>/home/user/opt/spark/yarn/*</value>
    </property>
</configuration>

```
Start YARN using the following command:
 ```bash
 $ start-yarn.sh
 ```
Confirm that the process was successful by accessing the web interface on the master's public IP using a browser: `http://192.168.1.xxx:8088/cluster`. The cluster should report 2 available live nodes.


#### 2.7 Spark configuration
Create the file `$SPARK_HOME/conf/spark-defaults.conf`, where we define the basic properties of our job execution environment, and we copy the following contents:
```text
spark.eventLog.enabled          true
spark.eventLog.dir              hdfs://controller:54310/spark.eventLog
spark.history.fs.logDirectory   hdfs://controller:54310/spark.eventLog
spark.master                    yarn
spark.submit.deployMode         client
spark.driver.memory             1g
spark.executor.memory           1g
spark.executor.cores            1
```

We create the directory in HDFS where historical data of our jobs will be stored and start the Spark history server:
```bashn order for our distributed services to maintain communication between the nodes, we need to establish SSH connectivity between them. We connect t
$ hadoop fs -mkdir /spark.eventLog
$ $SPARK_HOME/sbin/start-history-server.sh
```

We confirm that the process has been successful by accessing the web interface at the public IP of the master: `http://192.168.1.xxx:18080`.

#### 2.8 Execution of example application
We are ready to use our fresh infrastructure. Execute:
```bash
$ spark-submit --class org.apache.spark.examples.SparkPi ~/opt/spark/examples/jars/spark-examples_2.12-3.5.2.jar 100
```
You should be able to monitor the progress of the work in both the YARN web application (`http://192.168.1.xxx:8088`) and the history server (`http://192.168.1.xxx:18080`) after it is completed.

