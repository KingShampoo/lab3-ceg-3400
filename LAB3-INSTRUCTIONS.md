## Lab 3 : CEG 3400

### The Terminalator

Table of contents:
* [Background](LAB3-INSTRUCTIONS.md#background)
* [Objectives](LAB3-INSTRUCTIONS.md#objectives)
* [Preparation](LAB3-INSTRUCTIONS.md#preparation)
* [Task 1: Crafting Packets](LAB3-INSTRUCTIONS.md#task-1-crafting-packets)
* [Task 2: A Shell Game](LAB3-INSTRUCTIONS.md#task-2-a-shell-game)
* [Task 3: Iptables](LAB3-INSTRUCTIONS.md#task-3-iptables)
* [Task 4: Any Port ina Storm](LAB3-INSTRUCTIONS.md#task-4-any-port-in-a-storm)

---

#### Background and Objectives

In this lab you will learn about some basic (and more advanced) network manipulation 
tools by catpuring and creating packets, and exploring a well documented type of 
attack.

This lab assumes you have a basic understanding of networking, IP addresses, ports
and packets (from CEG-2350 and what was covered in class).

Students should become familiar with the following:

* creating, sending, and capturing packets with Scapy
* abusing netcat and pipes
* configuring iptables (firewalls)

---

#### Rubrik
| Item | # Points|
| --- | --- |
| 10 commits | 10 |
| Good markdown style | 20 |
| Task 1 | 30 |
| Task 2 | 30 | 
| Task 3 | 20 |
| Task 4 | 30 |

---

#### Preparation

This lab will require all work be done in AWS.  Please deploy the below instance and work inside the lab.

* [CEG 3400 Lab 3 AWS link](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=ceg3400Lab&templateURL=https:%2F%2Fwsu-cecs-cf-templates.s3.us-east-2.amazonaws.com%2Fcourse-templates%2Fceg3400-mek.yml)
* Identify the IP address of the running EC2 instance created [in the EC2
  page](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Instances:)

---

### Task 1: Crafting Packets

Famliarize yourself with scapy (covered in class) by creating a DNS request for `xkcd.com` and sending
it to `8.8.8.8` (or any DNS server that will respond to you).  Capture the response.

Answer all questions in `README.md`

* [Scapy Documentation](https://scapy.readthedocs.io/en/latest/#interactive-tutorial)


---

### Task 2: A Shell Game

You find the following command in the command history on one of your systems:

```
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc -l 1234 >/tmp/f
```

Investigate this command by running it on your AWS system.  While it is running scan the
***PUBLIC*** IP address of your AWS instance.

A security researcher mentioned that an outbreak of Bind and Reverse shells have been cropping 
up on your network recently.  Do some research on ***Bind Shells*** and ***Reverse Shells***.

After you have an understanding of what a Bind shell and reverse shell are see if you can 
make this one respond!

Hint: Try connecting to the opened port with `nc` from a different system.

Again, answer all questions in `README.md`.

---

### Task 3: Iptables

Clearly the previous command should not be left running.  But we can do better.

Using `iptables` block all incoming access to the malicious shell port on your AWS system.

Hint: you can craft a single `iptables` command or you can use `iptables-save` 
and `iptables-restore` to simplify saving the full firewall rules list.

---

### Task 4: Any Port in a Storm

After successfully blocking that shell your crack team of security researchers start 
seeing more malicious shells running on other ports.  Before you can start yelling at
your co-workers you need to lock your system down.

Identify all NEEDED ports for your standard communications with this server (SSH) and 
block ***ALL OTHER PORTS***.

***Hint:*** you will likely mess this up when deploying, be sure to document and 
`git commit` / `git push` all files including your final task 4 iptables-rules file 
before attempting this task.  If you lock yourself out that is OK, just answer all 
questions for this task.


