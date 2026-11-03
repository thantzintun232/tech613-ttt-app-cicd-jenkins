# VPC Step-by-Step Notes (Week 6)

**Goal:** the app VM is public, the database VM is private, and the app talks to the DB over its private IP.

---

## Why use a VPC?

**What is a VPC?**
A Virtual Private Cloud is your own logically isolated private network inside AWS. You choose the IP range, the subnets and how traffic flows.

**Why is it useful?**
- **Security:** sensitive things (like a database) can sit in a private subnet with no route to the internet.
- **Control over traffic:** route tables decide where traffic can go. A security group only allows or blocks traffic at one VM, so a VPC gives you more control than security groups alone.
- **Isolation:** your resources are separated from other users and from your other projects.
- **Resilience:** subnets can be spread across availability zones, so one outage doesn't take everything down.
- **Cost:** a VPC itself is free to leave running.

**Where is it used?**
- Any real AWS deployment, such as web apps with a public front end and a private database (like this tic-tac-toe app).
- Multi-tier architectures (web tier, app tier, database tier).
- Companies that need to keep internal systems private or meet security and compliance rules.

---

## Step 1: Create the VPC
- Give it a name tag and a CIDR block (e.g. `10.0.0.0/16`).
- **Why:** the VPC is the private network that everything else lives in. You can't put VMs directly into a VPC, so you split its address space into subnets (next step).

## Step 2: Create 2 subnets
- **Public subnet:** `10.0.2.0/24` (256 addresses)
- **Private subnet:** `10.0.3.0/24`, in a different availability zone (the private one was AZ B)
- Add name tags to both.
- **Why two AZs:** if one availability zone fails, the other keeps running.
- **Important:** the CIDR numbers do **not** make a subnet public or private. The route table does (see Step 4).

## Step 3: Create and attach the internet gateway
- Create it and name it after your VPC.
- Click **Attach to VPC** and pick *your* VPC.
- **Why:** the internet gateway is the door between your VPC and the internet. Creating it isn't enough. If it isn't attached, nothing can get in or out.

## Step 4: Create the public route table
- Name it "public route table" and choose your VPC.
- **Routes:** add `0.0.0.0/0` with the target set to your **internet gateway**.
- **Subnet associations:** edit them, tick the **public subnet**, and save.
- **Why:** the route table is the "router" of the network. A subnet is public only if its route table has a direct route to the internet gateway.
- The private subnet uses the default route table, which has no internet route. That is what makes it private.

## Step 5: Launch the database VM (private)
- Use the DB AMI (MongoDB already installed). Instance type is t3 micro, and the key pair is the usual one.
- Choose your VPC and the **private subnet**, with **no public IP**.
- **Create a new security group** (not the default). Name it with your VPC's name so you know it's attached to the right one.
  - **SSH:** source is the public subnet CIDR (`10.0.2.0/24`), not anywhere.
  - **MongoDB (custom TCP):** source is the public subnet too.
- Copy the DB's **private IP**. It should start with `10.0.3`.
- **Why no public IP:** even with one, the DB couldn't be reached from the internet, because there is no route to it. This keeps the database safe.
- **Why use an AMI:** a private VM has no internet access (no NAT), so it can't download or install software. The AMI already has everything installed.
- **Why restrict by CIDR:** only machines in the public subnet can connect, so "anyone from anywhere" is blocked.

## Step 6: Launch the app VM (public)
- Use the app AMI. It has the same instance type and key pair as the DB VM.
- Choose your VPC and the **public subnet**, with **auto-assign public IP = enabled**.
- **New security group:**
  - SSH from **your IP only**
  - HTTP **port 80** from anywhere
- **User data:** set the DB connection string (an environment variable export) using the DB's **private IP**.
- **Why the private IP:** traffic between VMs inside the VPC uses private IPs. The public IP is only for people on the internet reaching the app.
- **Why a public IP:** users need an address they can reach from the internet.

## Step 7: Test
- Open `http://<app public IP>`. Use **http**, not https, because only port 80 is open.
- To reach the DB, SSH into the app VM first (it acts as a **jump box**), then SSH to the DB's private IP.
- **Why a jump box:** the DB has no public IP, so the only way in is through a machine inside the VPC.

---

## Troubleshooting checklist
- Is the internet gateway attached to the right VPC?
- Does the public route table have the `0.0.0.0/0` route to the gateway, and is it associated with the public subnet?
- Is the DB IP in user data the **private** IP (`10.0.3.x`)?
- Did you use the right VPC's security group, not the default one?
- Bad gateway errors usually mean a wrong DB IP or an AMI issue.
- Still stuck? Try Ramon's AMI to rule out an AMI problem.

## Key ideas to remember
| Concept | Meaning |
|---|---|
| Security group | Allows or blocks traffic at a VM |
| Route table | Controls where traffic flows |
| Public subnet | Route table has a route to the internet gateway |
| Private subnet | No route to the internet gateway |
| NAT | Lets private VMs reach the internet (not needed here because the AMIs are pre-built) |
| Jump box | A public VM you SSH through to reach private VMs |

## Why custom VPC is worth the effort?

A custom VPC is worth the effort because it lets you design the network yourself instead of using the default VPC, where everything is public.

- Security: the database sits in a private subnet with no public IP and no route to the internet.
- Control: route tables and the internet gateway decide exactly where traffic flows.
- Least access: the DB only accepts traffic from the app subnet, and the app only accepts SSH from you and HTTP from users.
- Reliability: subnets in different availability zones keep the app running if one zone fails.
- Cost: a VPC is free to leave running.

**Trade-off:** more setup and more troubleshooting, but it’s easy to repeat once you understand it.