# Azure fundamentals

Modules:

1. [Cloud Concepts - Principles of cloud computing](#cloud-concepts---principles-of-cloud-computing-home)
1. [Introduction to Azure](#core-cloud-services---introduction-to-azure-home)
1. [Azure architecture and service guarantees](#core-cloud-services---azure-architecture-and-service-guarantees-home)
1. [Create an Azure account](#create-an-azure-account-home)
1. [Manage services with the Azure portal](#core-cloud-services---manage-services-with-the-azure-portal-home)
1. [Azure compute options](#core-cloud-services---azure-compute-options-home)
1. [Azure data storage options](#core-cloud-services---azure-data-storage-options-home)
1. [Azure networking options](#core-cloud-services---azure-networking-options-home)
1. [Security, responsibility and trust in Azure](#security-responsibility-and-trust-in-azure-home)
1. [Apply and monitor infrastructure standards with Azure Policy](#apply-and-monitor-infrastructure-standards-with-azure-policy-home)
1. [Control and organize Azure resources with Azure Resource Manager](#control-and-organize-azure-resources-with-azure-resource-manager-home)
1. [Predict costs and optimize spending for Azure](#predict-costs-and-optimize-spending-for-azure-home)

## Cloud Concepts - Principles of cloud computing ([home](#))

### What is cloud computing?

**Cloud computing**: renting resources, like storage space or CPU cycles, on another company's computers.

- The company providing these services is referred to as a **cloud provider**

### Categories of computing services

1. Compute power - such as Linux servers or web applications
1. Storage - such as files and databases
1. Networking - such as secure connections between the cloud provider and your company
1. Analytics - such as visualizing telemetry and performance data

### Benefits of cloud computing

- Pay-as-you-go (consumption-based pricing model)
- Scalable: increase or decrease the resources and services used based on the demand or workload at any given time
    - **Vertical scaling** ("scaling up"): adding resources to increase the power of an existing server. Some examples of vertical scaling are: adding more CPUs, or adding more memory.
    - **Horizontal scaling** ("scaling out"): adding more servers that function together as one unit. For example, you have more than one server processing incoming requests.
- Fault tolerant: includes data backup, disaster recovery, and data replication services
- Secure
- Economies of scale: cloud providers leverage economies of scale and (theoretically) pass savings on to consumer

### Forms of spending

Traditional CapEx costs (on-prem physical infrastructure):

- Server costs
- Storage costs
- Network costs
- Backup and archive costs
- Organization continuity and disaster recovery costs
- Data center infrastructure costs
- Technical personnel

The costs associated with cloud computing are operational expenses (OpEx):

- Leasing software and customized features
- Scaling charges based on usage/demand instead of fixed hardware or capacity
- Billing at the user or organization level

### Cloud deployment models

- **Public cloud**: All hardware is provided by the cloud provider
    - Cheap and scalable
- **Private cloud**: Cloud environment hosted in your own data center, offering simulation of public cloud to users in your organization
    - More control, but organization is responsible for purchase and maintenance
- **Hybrid cloud**: Combines public and private clouds, allowing you to run your applications in the most appropriate location
    - Example: Host a website in the public cloud and link it to a highly secure database hosted in your private cloud

### Types of cloud services

1. Infrastructure as a service (IaaS): rented computing infrastructure (hardware), provisioned and managed over the Internet
    - Example: Azure VM
1. Platform as a service (PaaS): provides an environment for building, testing, and deploying software applications without requiring the user to manage the infrastructure
    - Example: Azure SQL Database
1. Software as a service (SaaS): software that is centrally hosted and managed for the end customer, usually subscription-based
    - Examples: Office 365, Skype, and Dynamics CRM Online

![Service comparison](../imgs/azure-iaas-saas-paas.jpg)

## Core Cloud Services - Introduction to Azure ([home](#))

**Azure**: Microsoft's cloud computing platform.

**Virtualization** separates the tight coupling between hardware and OS using a **[hypervisor](https://en.wikipedia.org/wiki/Hypervisor)**.  Each true server in a cloud provider's data center has a hypervisor.
The hypervisor emulates a real computer and its CPU.  A hypervisor can run multiple VMs.

Tour of Azure services: https://docs.microsoft.com/en-us/learn/modules/welcome-to-azure/3-tour-of-azure-services

### Azure Cloud Shell

- **Azure Cloud Shell**: a browser-based command-line experience for managing and developing Azure resources
- **Azure CLI**: Azure command-line interface, which is accessible via Cloud Shell or a regular shell

## Core Cloud Services - Azure architecture and service guarantees ([home](#))

### Data centers, Regions, and Geographies

Microsoft Azure is made up of on-the-ground **data centers** located around the globe.  Azure resources use physical equipment located in secure data centers.

The specific data centers aren't exposed to end users directly; instead, Azure organizes them into regions.  (You deploy your app to a region, not a data center.)

A **region** is a geographical area on the planet containing _at least one_, but potentially multiple data centers that are nearby and networked together with a low-latency network.

![Azure regions](../imgs/azure-2-regions-large.png)

Special region:

- US DoD Central, US Gov Virginia, US Gov Iowa: Physical and logical network-isolated instances of Azure for US government agencies and partners
    - Operated by screened US persons and include additional compliance certifications
- China East, China North: Available through a unique partnership between Microsoft and 21Vianet
    - Microsoft does not directly maintain the data centers

**Data residency**: physical or geographic location of an organization's data or information. It defines the legal or regulatory requirements imposed on data based on the country or region in which it resides and is an important consideration when planning out your application data storage.

Geographies are broken up into the following areas:

- Americas
- Europe
- Asia Pacific
- Middle East and Africa

### Availability Zones

**Availability Zone**: a cluster of data centers within an Azure region that is physically separate from other zones.

- Each Availability Zone is made up of _one or more_ data centers equipped with independent power, cooling, and networking. It is set up to be an isolation boundary
- For a region to formally support Availability Zones, it must have a _minimum of 3 zones_
- You can use Availability Zones to run mission-critical applications and build high-availability into your application architecture by co-locating your compute, storage, - networking, and data resources within a zone
- Availability Zones are primarily for VMs, managed disks, load balancers, and SQL databases

### Region Pairs

Region pairs: The pairing of two Azure regions, which are at least 300 miles away but within the same geography, as a means of resiliency.

### Service-Level Agreements (SLAs)

SLA: captures the specific terms that define the performance standards that apply to Azure.

- A "what you can expect" contract
- SLAs also specify what happens if a service or product fails to perform to a governing SLA's specification

Characteristics of Azure SLAs:

1. Performance Targets: specific to each Azure product and service, such as uptime or connectivity rates
1. Uptime and Connectivity Guarantees: typically range from 99.9 percent ("three nines") to 99.999 percent ("five nines")
1. Service credits: typically applied when an Azure product under-performs

**Composite SLA**: an SLA that represents SLAs combined across different service offerings

- Combined probability of failure is higher than the individual SLA values if applications are dependent
- Example: 99.95 % (SLA 1) × 99.99 % (SLA 2) = 99.94 % (Composite SLA)

**Application SLA**: an SLA created by you the developer in the interest of setting a performance target for your application.

**Resiliency**: the ability of a system to recover from failures and continue to function.

- High availability and disaster recovery are two crucial components of resiliency
- When designing your architecture you need to design for resiliency, and you should perform a Failure Mode Analysis (FMA)

**Availability**: the time that a system is functional and working.

## Create an Azure account ([home](#))

### Accounts and subscriptions

**Azure account**: an identity in either Azure Active Directory (Azure AD), or a directory that is trusted by Azure AD, such as a work or school organization.

Every Azure account is associated with one or more subscriptions.

**Azure subscription**: a logical container used to provision resources in Azure.

Subscription types:

- Free
- Pay-As-You-Go (PAYG): charges you monthly for the services you used in that billing period
- Enterprise Agreement
- Student

### Using multiple subscriptions under one account

Creating multiple subscriptions under one account is particularly useful for businesses because _access control and billing occur at the subscription level_, not the account level.

- Access management: you could, for example, limit engineering to lower-cost resources, while allowing the IT department a full range
- A single bill is generated for every Azure subscription on a monthly basis
- You can set spending limits on each subscription
- Many large organizations buy their Azure subscriptions through Enterprise Agreements (EAs)
- It is possible to transfer Azure subscriptions between accounts

### Authentication, Azure AD, and tenants

Authentication for your account is performed using Azure Active Directory (**Azure AD**):  a modern identity provider that supports multiple authentication protocols to secure applications and services in the cloud.

When you sign up for a Microsoft cloud service subscription such as Microsoft Azure, Microsoft Intune, or Office 365, a dedicated instance of Azure AD is automatically created for your organization.

An Azure AD **tenant** is a dedicated, isolated instance of the Azure Active Directory service, commonly associated with companies. If you sign up for Azure with an email address that's not associated with an existing tenant, the sign-up process will walk you through creating a tenant, owned entirely by you.

Azure AD tenants and subscriptions have a one-to-many trust relationship: A tenant can be associated with multiple Azure subscriptions, but every subscription is associated with only one tenant.

Each Azure AD tenant has an account owner.

### Azure Support

The support plans available and how you're charged depends on the type of Azure customer you are, and the type of Azure subscription you have.

See [this table](https://docs.microsoft.com/en-us/learn/modules/create-an-azure-account/6-support-options) of paid Azure support plans.

## Core Cloud Services - Manage services with the Azure portal ([home](#))

### Azure management options

**Azure portal**: a public website that you can access with any web browser.

- https://portal.azure.com/
- Customizable via drag-and-drop
- Doesn't provide any way to automate repetitive tasks

[**Azure PowerShell**](https://docs.microsoft.com/en-us/powershell/): a module that you can install for Windows PowerShell or PowerShell Core.

[**Azure Command-Line Interface (CLI)**](https://docs.microsoft.com/en-us/cli/azure/?view=azure-cli-latest): a cross-platform command-line program that connects to Azure and executes administrative commands on Azure resources.

- Can be run on Windows, Linux, or macOS
- Sign in via `az login`

**Azure Cloud Shell**: an interactive, authenticated, browser-accessible shell for managing Azure resources.

- Allows Bash or PowerShell (shells), and both support the Azure CLI and Azure PowerShell module
- Has a suite of developer tools, text editors, and other tools available (git, vim, Python)

**Azure mobile app**: allows you to access, manage, and monitor all your Azure accounts and resources from your iOS or Android phone or tablet.

[**SDKs**](https://azure.microsoft.com/en-us/downloads/): collections of libraries for .NET, Java, JavaScript, and Python.

### Using Azure Portal

The Azure portal uses a **blades model** for navigation. A blade is a slide-out panel containing the UI for a single level in a navigation sequence. For example, each of these elements in this sequence would be represented by a blade: Virtual machines > Compute > Ubuntu Server.

**Azure Marketplace**: allows customers to find, try, purchase, and provision applications and services that are certified to run on Azure.  Example: open-source container platforms, virtual machine images, databases, application build and deployment software, developer tools, threat detection, and blockchain.

**Azure Advisor**: a free service built into Azure that provides recommendations on high availability, security, performance, and cost.

### Azure Portal dashboards

**Dashboard**: a customizable collection of UI tiles displayed in the Azure portal.

- You add, remove, and position tiles to create the exact view you want, and then save that view as a dashboard
- Multiple dashboards are supported, and you can switch between them as needed
- Dashboards are stored as JSON files
- Azure stores dashboards within resource groups, just like virtual machines or storage accounts that you can manage within the portal
- When you define a new dashboard, it is private and visible only to your account. To make it visible to others, you need to share a dashboard. However, as with any other Azure resource, you need to specify a new resource group (or use an existing resource group) in which to store shared dashboards

### Preview features

**Azure Preview Features**: you can test beta and other pre-release features, products, services, software, and regions.

- **Private Preview**: feature is available to specific Azure customers for evaluation purposes
- **Public Preview**: feature is available to all Azure customers for evaluation purposes

**General Availability (GA)**: when a feature has been released to customers as part of Azure's default product set.

## Core Cloud Services - Azure compute options ([home](#))

### Azure compute concepts

There are four common techniques for performing compute in Azure:

1. **Virtual machines**: software emulations of physical computers
    - Each VM includes an operating system and hardware that appears to the user like a physical computer
1. **Containers**: a virtualization environment for running applications
    - Unlike VMs, containers don't include an operating system for the apps running inside the container. Instead, containers bundle the libraries and components needed to run the application and use the existing host OS running the container.
1. **Azure App Service**: a platform-as-a-service (PaaS) offering in Azure that is designed to host enterprise-grade web-oriented applications
1. **Serverless computing**: a cloud-hosted execution environment that runs your code but completely abstracts the underlying hosting environment
    - Run application code without creating, configuring, or maintaining a server. The application is broken into separate functions that run when triggered by some action
    - With serverless, you only pay for processing time.  With VMs/containers, you're charged while they're running

### Azure VMs and Scaling

**Image**: a template used to create a VM. These templates already include an OS and often other software, like development tools or web hosting environments.

Features for scaling Azure VMs:

- **Availability sets**: a logical grouping of two or more VMs that help keep your application available during planned or unplanned maintenance
- **Virtual Machine Scale Sets**: let you create and manage a group of identical, load balanced VMs, without configuring a load balancer
- **Azure Batch**: scale to many VMs.  Enables large-scale job scheduling and compute management

### Containers

**Container**: a modified runtime environment built on top of a host OS that executes your application.

- More lightweight than VMs
- Run multiple apps in a single container

Azure supports Docker containers (a standardized container model):

- **Azure Container Instances** (ACI) - a PaaS offering that allows you to upload your containers and execute them directly
- **Azure Kubernetes Service** (AKS) - a complete orchestration\* service for containers with distributed architectures with multiple containers
    - You _deploy_ containers to a Kubernetes cluster

<sup>\***Orchestration**: The task of automating, managing, and interacting with a large number of containers</sup>

### Microservices

Containers are often used to create solutions using a microservice architecture. This architecture is where you break solutions into smaller, independent pieces.

**Microservice**: Simplify application architecture by creating more focused, autonomous, and independently managed web services that address a single business domain or capability.


Factors that call for microservices:

- High release velocity
- Highly scalable
- Rich domains
- Small development teams

### App Service

- Supports both Windows and Linux
- Enables automated deployments from GitHub, Azure DevOps, or any Git repo to support a continuous deployment model
- Cost: You pay for the Azure compute resources your app uses while it processes requests based on the App Service Plan you choose

Types of apps:

- **Web Apps**: Traditional web apps built using a handful of languages
- **API Apps**: REST-based Web APIs using your choice of language and framework; Swagger support and published API in Azure Marketplace
- **WebJobs**: Run a program or script in the same context as a web app
- **Mobile Apps**: Backend for iOS and Android apps

### Serverless

Serverless computing encompasses three ideas:

- **Abstraction of servers**: the cloud provider takes care of managing the server infrastructure and allocation/deallocation of resources based on demand
- **Event-driven scale**: workloads that respond to incoming events
- **Micro-billing**: pay only for the time your code runs

**Azure Functions**: "pure code" without dependence on underlying platform or infrastructure; trigger logic based on an event.

- Can be either **stateless** (the default) where they behave as if they're restarted every time they respond to an event), or **stateful** (called "Durable Functions") where a context is passed through the function to track prior activity

**Azure Logic Apps**: execute _workflows_ (rather than code) designed to automate business scenarios that start with a trigger.

- You create Logic App workflows using a visual designer on the Azure portal or in Visual Studio
- The workflows are persisted as a JSON file with a known workflow schema

**Orchestration**: a collection of functions or steps, that are executed to accomplish a complex task.

- Can be created by both Azure Functions and Logic Apps

Functions versus Logic Apps:

| Attribute | Functions | Logic Apps |
| --------- | --------- | ---------- |
| State |   Normally stateless, but Durable Functions provide state  |   Stateful |
| Development |     Code-first (imperative)   |  Designer-first (declarative) |
| Connectivity |    About a dozen built-in binding types, write code for custom bindings  |  Large collection of connectors, Enterprise Integration Pack for B2B scenarios, | build custom connectors |
| Actions |     Each activity is an Azure function; write code for activity functions  | Large collection of ready-made actions |
| Monitoring |  Azure Application Insights | Azure portal, Log Analytics |
| Management |  REST API, Visual Studio   |  Azure portal, REST API, PowerShell, Visual Studio |
| Execution context | Can run locally or in the cloud   |  Runs only in the cloud. |

## Core Cloud Services - Azure data storage options ([home](#))

### Introduction

Benefits of cloud storage:

- Automated backup and recovery
- Replication across the globe
- Support for data analytics
- Encryption capabilities
- Multiple data types
- Data storage in virtual disks
- Storage tiers

Types of data that Azure storage is designed to hold:

1. **Structured (relational) data**: Adheres to a schema, stored in relational database
1. **Semi-structured data**: non-relational or NoSQL data
1. **Unstructured data**: completely unstructured, no restrictions on the kinds of data it can hold

### Storage options overview

- **Azure SQL Database**: a relational database as a service (DaaS) based on the latest stable version of the Microsoft SQL Server database engine
    - **Azure Database Migration Service**: used to migrate your existing SQL Server databases with minimal downtime
- **Azure Cosmos DB**: a globally distributed database service
    - Supports schema-less data that lets you build highly responsive and Always On applications to support constantly changing data
- **Azure Blob Storage**: unstructured, meaning that there are no restrictions on the kinds of data it can hold
    - Blobs behave largely like files on a disk when it comes to reading and writing data
    - Commonly used for logs, audio/video data, scientific data, disaster recovery
    - Lets you stream large video or audio files directly to the user's browser
- **Azure Data Lake**: a large repository that stores both structured and unstructured data
    - Allows you to perform analytics on your data usage and prepare reports
**Azure Files**: offers fully managed file shares in the cloud that are accessible via Server Message Block (SMB) protocol
**Azure Queue**: storage service for storing large numbers of messages
    - Provides asynchronous message queueing for communication between application components, whether they are running in the cloud, on the desktop, on-premises, or on mobile devices.
**Disk storage**: an attached virtual hard disk
    - The disks can be managed or unmanaged by Azure, and therefore managed and configured by the user
    - You are storing data that is not required to be accessed from outside the virtual machine to which the disk is attached
    - Offers both solid-state drives (SSDs) and traditional spinning hard disk drives (HDDs)

Tiers for blob object storage:

- **Hot storage tier**: optimized for storing data that is accessed frequently
- **Cool storage tier**: optimized for data that are infrequently accessed and stored for at least 30 days
- **Archive storage tier**: for data that are rarely accessed and stored for at least 180 days with flexible latency requirements

Encryption for storage services:

- **Client-side encryption**: data is already encrypted by the client libraries. Azure stores the data in the encrypted state at rest
- Azure Storage Service Encryption (SSE): server-side encryption done by Azure
    - Encrypts the data before storing it and decrypts the data before retrieving it
    - Transparent to the user

**Replication for storage**: a replication type is set up when you create a storage account.

### Comparison between Azure data storage and on-premises storage

![On-prem versus Azure data storage](../imgs/azure-onprem-v-azure-storage.jpg)

## Core Cloud Services - Azure networking options ([home](#))

**Loosely coupled architecture**: system in which each component has, or makes use of, little or no knowledge of the definitions of other separate components.

**N-tier architecture**: divides an application into two or more logical tiers.

- A higher tier can access services from a lower tier, but a lower tier should never access a higher tier
- Tiers help separate concerns and are designed to be reusable
- Simplifies maintenance
- New tiers can be inserted if needed

Typical design:

- All tiers (parts) sit in the same Azure region and the same virtual network, but in separate subnets
    - Subnet: a logical subdivision of an IP network
    - Computers that belong to a subnet are addressed with an identical most-significant bit-group in their IP addresses
- The user-facing tier has a public and private IP addresses, while other deeper tiers are accessible only via their private IP
- Virtual networks are configured through software

**Network security group** (NSG): allows or denies inbound network traffic to your Azure resources.

- A cloud-level firewall for your network
- Configure to accept specific ports, IP addresses, or combinations of both

### Azure Load Balancer

**Availability**: how long your service is up and running without interruption.  **High availability**: a service that's up and running for a long period of time.

**Resiliency**: a system's ability to stay operational during abnormal conditions.

**Load balancer**: distributes traffic evenly among each system in a pool, helping you achieve high availability.

- The load balancer becomes the entry point to the user
- Multiple VMs (or another resource) sit in a single tier and the load balancer distributes incoming requests between them
- Enables you to run maintenance tasks without interrupting service. (For example, you can stagger the maintenance window for each VM)

**Azure Application Gateway**: a load balancer designed for HTTP web applications.

- Uses Azure Load Balancer at the transport level (TCP)
- Applies sophisticated URL-based routing rules to support several advanced scenarios (application layer/OSI layer 7 load balancing)
- Benefits:
    - **Cookie affinity**: Useful when you want to keep a user session on the same backend server
    - **SSL termination**. Manages your SSL certificates and passes unencrypted traffic to the backend servers to avoid encryption/decryption overhead
    - **Web application firewall**. Application gateway supports a sophisticated firewall (WAF) with detailed monitoring and logging to detect malicious attacks against your network infrastructure
    - **URL rule-based routes**. Application Gateway allows you to route traffic based on URL patterns, source IP address and port to destination IP address and port. This is helpful when setting up a content delivery network
    - **Rewrite HTTP headers**. You can add or remove information from the inbound and outbound HTTP headers of each request to enable important security scenarios, or scrub sensitive information such as server names

**Content delivery network (CDN)**: a distributed network of servers that delivers web content to users with minimal latency.

- Typical usage scenarios include web applications containing multimedia content

**Azure DNS**: a hosting service for DNS domains that runs on Azure infrastructure

- You can bring your own DNS server or use **Azure DNS**
- For example, if you're using Azure DNS and have a load balancer serving contoso.com, Azure DNS routes traffic to the load balancer

### Azure Traffic Manager: reducing latency

A load balancer achieves high availability.  It does _not_ decrease latency or create resiliency across geographic regions.

**Latency**: the time it takes for data to travel over the network.

- Typically measured in milliseconds
- Most heavily influenced by _distance_

**Azure Traffic Manager**: uses the DNS server that's closest to the user to direct user traffic to a globally distributed endpoint.

- Doesn't see the traffic that's passed between the client and server. Rather, it directs the client web browser to a preferred endpoint
- Used when multiple copies of your underlying service are deployed to more than one region

![Azure Traffic Manager](../imgs/azure-traffic-manager.jpg)

## Security, responsibility and trust in Azure ([home](#))

### Key concepts

As you move across the spectrum from IaaS to PaaS to SaaS, the burden of security falls more heavily on Azure rather than you the user.

Regardless of the deployment type, you always retain responsibility for the following:

1. Data
1. Endpoints
1. Accounts
1. Access management

**Defense in depth**: a layered approach to security where eaach layer provides protection so that if one layer is breached, a subsequent layer is already in place to prevent further exposure.

- Designed to slow the advance of an attack

### Azure Security Center

**Azure Security Center**: a monitoring service that provides threat protection.

- Provides security recommendations based on your configurations, resources, and networks
- Monitor security settings across on-premises and cloud workloads
- Use machine learning to detect and block malware from being installed
- Provide just-in-time access control for ports
- Part of the Center for Internet Security (CIS) recommendations

Available in two tiers:

1. Free: available as part of your Azure subscription
    - Limited to assessments and recommendations of Azure resources only
1. Standard: full suite
    - Continuous monitoring, threat detection, just-in-time access control for ports
    - To upgrade, you must be assigned the role of Subscription Owner, Subscription Contributor, or Security Admin

Response stages:

1. Detect: Review the first indication of an event investigation
1. Assess: obtain more information about the suspicious activity
1. Diagnose: identify containment, mitigation, and workaround strategies

### Identity and access

[**Identity management**](https://en.wikipedia.org/wiki/Identity_management), which is the proper authentication and assignment of privileges, has become the new primary security boundary.

- **Authentication**: establishing the identity of a person or service looking to access a resource
- **Authorization**: establishing what level of access an authenticated person or service has

**Azure Active Directory (Azure AD)** is a cloud-based identity service that helps managed authentication and authorization.

- Authentication: verifying identity to access applications and resources
    - Self-service password reset, multi-factor authentication (MFA), custom banned password list, smart lockout services
    - MFA: requires _two or more_ elements for full authentication
        - Something you know: a password or the answer to a security question
        - Something you possess: a mobile app that receives a notification or a token-generating device
        - Something you are: a fingerprint or face scan used on many mobile devices
    - Increases security of your identity by limiting the impact of credential exposure.
- Single-Sign-On (SSO): enables users to remember only one ID and one password to access multiple applications
    - Philosophy: "More identities mean more passwords to remember and change"
- Application management
- Business to business (B2B) identity services: manage guest users and external partners
- Device Management: manage how devices access your corporate data

#### Providing identities to services

An **identity** is not just a user, but anything that can be authenticated, including an app or service.

How can you give a service an identity without putting that identity in a plaintext configuration file?

Azure has two options for this:

- **Service principals**: an identity that is used by a service or application
    - Based off the concept of a **principal**,  is an identity acting with certain (expanded) roles or claims
- **Managed identities for Azure services**: an account created on your Active Directory Tenant, where the Azure infrastructure will automatically take care of authenticating the service and managing the account

#### Role-based access control (RBAC)

**Role**: a set of permissions, like "Read-only" or "Contributor," that users can be granted to access an Azure service instance.

RBAC examples:

- Allow one user to manage VMs in a subscription, and another user to manage virtual networks
- Allow a database administrator (DBA) group to manage SQL databases in a subscription
- Allow a user to manage all resources in a resource group, such as VMs, websites, and virtual subnets
- Allow an application to access all resources in a resource group

**Azure Resource Manager hierarchy**: Roles assigned at a higher scope, like an entire subscription, are inherited by child scopes, like service instances.

Azure AD Privileged Identity Management (PIM): provides access reviews, oversight of role assignments, self-service, and just-in-time role activation.

### Encryption

**Encryption**: the process of making data unreadable and unusable to unauthorized viewers.

Two top-level types of encryption:

1. **Symmetric encryption**: uses the same key to encrypt and decrypt the data.
    - Example: Advanced Encryption Standard (AES)
1. **Asymmetric encryption**: uses a public key and private key pair
    - Either key can encrypt but both keys are required for decryption
    - Used for things like Transport Layer Security (TLS) (used in HTTPS) and data signing

Encryption is typically approached in two ways:

1. **Encryption at rest**: encrypted data stored on a physical medium.
1. **Encryption in transit**: data encrypted when it is actively moving from one location to another.
    - Could be encrypted at several different layers, such as application layer (ex: HTTPS), or network layer (VPN)

#### Encryption on Azure

- **Azure Storage Service Encryption**: encryption at rest for Azure services
    - Automatically encrypts your data before persisting it to Azure Managed Disks, Azure Blob storage, Azure Files, or Azure Queue storage, and decrypts the data before retrieval.
- **Azure Disk Encryption**: encrypts Windows and Linux IaaS virtual machine disks
    - Uses BitLocker (Windows) or dm-crypt (Linux)
    - Ensures that the virtual hard disk (VHD) is encrypted, not just the physical disk (as encrypted by Storage Service Encryption)
- **Azure Key Vault**: a secrets manager---centralized cloud service for storing your application secrets
    - Includes ability to provision, manage, and deploy SSL/TLS certificates

### Azure certificates

Two purposes of certificates in Azure:

1. **Service certificates**: used for cloud services
    - Attached to cloud services and enable secure communication to and from the service
    - Can be managed separately from your services
1. **Management certificates**: used for authenticating with the management API
    - Not really related to cloud services

### Network protection

**Firewall**: a service that grants server access based on the originating IP address of each request.

- Rules typically also include specific network protocol and port information
- **Azure Firewall**: fully stateful firewall as a service with built-in high availability and unrestricted cloud scalability
    - Provides inbound protection for non-HTTP/S protocols (SSH, FTP, SSH)
- **Azure Application Gateway**: a load balancer that includes a Web Application Firewall (WAF)

**Azure DDoS Protection**: identifies DDos, blocks further traffic from reaching Azure services without interrupting legitimate customers

- Provides both _basic_ and _standard_ service tiers
- Notifies you of attack detection via Azure Monitor metrics

**Network Security Groups (NSGs)**: restricts communication between virtual machines by source and destination IP address, port, and protocol.

**Azure ExpressRoute**: provides a dedicated, private connection between your private network and Azure.

- Lets you extend your on-premises networks into the Microsoft cloud over a private connection facilitated by a connectivity provider

**Microsoft Azure Information Protection** (AIP): helps organizations classify and optionally protect documents and emails by applying labels.

- Labels can be applied automatically based on rules and conditions, manually, or a combination of both where users are guided by recommendations
- You can track and control how the content is used after it is classified/labeled: for example, track access to documents

**Azure Advanced Threat Protection (Azure ATP)**: identifies, detects, and helps you investigate advanced threats, compromised identities, and malicious insider actions directed at your organization.

- Azure ATP portal: ATP has its own portal separate from the Azure portal, https://portal.atp.azure.com
- Azure ATP sensor: installed directly on your domain controllers
- Azure ATP cloud service: connected to Microsoft's intelligent security graph

### Application lifecycle management: security considerations

**Microsoft Security Development Lifecycle (SDL)**: introduces security and privacy considerations throughout all phases of the development process.

- Provide training: security is everyone's job
- Define and update security requirements
- Tracking: properly label security defects and security work items
- Perform threat modeling
- Establish design requirements
- Define and use cryptography standards
- Manage security risks from using third-party components
- Define and publish a list of approved tools and their associated security checks
- Static analysis: analyze source code prior to compilation
    - Integrate Static Analysis Security Testing (SAST) into the commit pipeline
- Dynamic analysis: run-time verification of your fully compiled or packaged software
    - Monitor application behavior for memory corruption, user privilege issues, and other critical security problems
- Perform penetration testing
- Establish a standard incident response process

## Apply and monitor infrastructure standards with Azure Policy ([home](#))

### Overview

**Azure Policy**: service to create, assign and, manage IT policies to enforce different rules and effects over your resources

Example: ensure that all resources have the `Department` tag associated with them.

Azure Policy versus RBAC:

- RBAC focuses on user actions at different scopes
- Azure Policy focuses on resource properties during deployment and for already-existing resources
- Unlike RBAC, Azure Policy is a _default-allow-and-explicit-deny system_

> Role-based access control (RBAC) provides _fine-grained_ access management for Azure resources, enabling you to grant users only the rights they need to perform their jobs. RBAC is provided at no additional cost to all Azure subscriber.

How to apply a policy:

1. Create a policy definition: expresses what to evaluate and what action to take, represented as a JSON file
1. Assign a definition to a scope of resources: register a provider, such as  `Microsoft.PolicyInsights` extension, and create a policy assignment
    - **Policy assignment**: a policy definition that has been assigned to take place within a specific scope
        - Policy assignments are inherited by all child resources
    - **Policy effects**: dictate what happens when a policy rule is matched
1. View policy evaluation results: use the Azure Portal to spot non-compliant resources
    - Azure Policy can allow a resource to be created even if it doesn't pass validation---this will trigger an audit event

Overview of different policy effects:

| Policy Effect | What happens? |
| ------------- | ------------- |
| Deny |   The resource creation/update fails due to policy. |
| Disabled |   The policy rule is ignored (disabled). Often used for testing. |
| Append | Adds additional parameters/fields to the requested resource during creation or update. A common example is adding tags on resources such as Cost Center or specifying allowed IPs for a storage resource. |
| Audit, AuditIfNotExists |    Creates a warning event in the activity log when evaluating a non-compliant resource, but it doesn't stop the request. |
| DeployIfNotExists |  Executes a template deployment when a specific condition is met. For example, if SQL encryption is enabled on a database, then it can run a template after the DB is created to set it up a specific way. |

### Initiatives

**Initiative definition**: a set or group of policy definitions to help track your compliance state for a larger goal.

- **Initiative assignment**: an initiative definition assigned to a specific scope
- Helps to organize multiple policy definitions

### Enterprise governance management

**Azure Management Group**: container for managing access, policies, and compliance across multiple Azure subscriptions.

- A further level of classification that is above the level of subscriptions

Examples:

- Limit VM locations to US West Region on the group "Infrastructure Team management group"
- Provide user access to multiple subscriptions in one sweep: create one role-based access control (RBAC) assignment on the management group

### Azure Blueprint

**Azure Blueprint**: define a repeatable set of Azure resources that implements and adheres to an organization's standards, patterns, and requirements.

- Makes it easier, faster, and safer to stand up new environments within organizational compliance
- Blueprint service is backed by Azure Cosmos DB
- Difference from Resource Manager templates:
    - A Resource Manager template is a document that doesn't exist natively in Azure
    - Blueprints preserve the definition (what _should_ be deployed) and the assignment (what _was_ deployed); this is not true for a template
- Difference from Azure Policy: a policy can be included in a blueprint

### How Microsoft manages resource security

This section deals with how Microsoft, the cloud provider, manages the underlying resources you are building on.

- **Microsoft Privacy Statement**: explains what personal data Microsoft processes, how Microsoft processes it, and for what purposes
- **Microsoft Trust Center**: a website resource containing information and details about how Microsoft implements and supports security, privacy, compliance, and transparency
- **Service Trust Portal** (STP): the Microsoft public site for publishing audit reports and other compliance-related information relevant to Microsoft’s cloud services
    - You could maintain and track compliance with FedRAMP, GDPR, etc
- **Compliance Manager**: a workflow-based risk assessment dashboard within the Trust Portal that enables you to track, assign, and verify your organization's regulatory compliance activities
    - Contains detailed information provided by Microsoft to auditors and regulators
    - Provides a Compliance Score to help you track your progress and prioritize auditing controls

### Monitor your service health

**Azure Monitor**: comprehensive solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments.

- **Activity Logs**: record when resources are created or modified
- **Metrics**: tell you how the resource is performing and the resources that it's consuming
- **Application Insights**: monitors the availability, performance, and usage of your web applications
- **Azure Monitor for containers**: monitors the performance of container workloads
- **Azure Monitor for VMs**: monitors your Azure VMs at scale


**Azure Service Health**: provides personalized guidance and support when issues with Azure services affect you.

- **Azure Status**: provides a global view of the health state of Azure services
- **Service Health**: provides you with a customizable dashboard that tracks the state of your Azure services in the regions where you use them
- **Resource Health**: helps you diagnose and obtain support when an Azure service issue affects your resources
    - A more personalized dashboard (relative to Azure Status)

## Control and organize Azure resources with Azure Resource Manager ([home](#))

### Resource groups

**Resource group**: a logical container for resources deployed on Azure.

- All resources must be in a resource group
- A resource can only be a member of a single resource group
- If you delete a resource group, all resources contained within are also deleted
- Function as a scope for applying RBAC permissions
- A resource group sits within a subscription and within a specific region

Use resource groups for organization:

- Consistent naming convention: e.g. `msftlearn-core-infrastructure-rg`
- Organizing principles: by resource type (VMs, DB), purpose (core, helpers), environment (prod, qa, dev), department (marketing, finance, human resources)

### Use tagging to organize resources

**Tags**: name/value pairs of text data that you can apply to resources and resource groups.

- A resource can have up to 50 tags
- The name is limited to 512 characters for all types of resources except storage accounts, which have a limit of 128 characters
- The tag value is limited to 256 characters for all types of resources
- Tags aren't inherited from parent resources
    - Example: tags applied at a resource group level are _not_ propagated to resources within the resource group
- Can be added and manipulated through the Azure portal, Azure CLI, Azure PowerShell, Resource Manager templates, and through the REST API
- Not all resource types support tags

Uses of tags:

- Group your billing data
- Categorize costs by runtime environment
- In automation (example: `shutdown:6PM`)

### Implementing RBAC

TODO: merge this into earlier RBAC section.

Use the **Access control (IAM)** panel to view, grant, or remove access.

- RBAC uses an **allow model** for access
- If one role assignment grants you read permissions to a resource group, and a different role assignment grants you write permissions to the same resource group, you will have write permissions on that resource group

### Resource locks

**Resource lock**: a setting that can be applied to any resource to block modification or deletion.

- **Delete** mode: will allow all operations against the resource but block the ability to delete it
- **Read-only** mode: will only allow read activities to be performed against it, blocking any modification or deletion of the resource
- Resource locks can be applied to subscriptions, resource groups, and to individual resources
- Resource locks are inherited when applied at higher levels

## Predict costs and optimize spending for Azure ([home](#))

### Customer types

1. **Enterprise**: sign an Enterprise Agreement with Azure that commits them to spend a negotiated amount on Azure services
    - Typically billed annually
    - Access to customized Azure pricing
1. **Web direct**: pay general public prices for Azure resources
    - Monthly billing
    - Payments occur through the Azure website
1. **Cloud Solution Provider** (CSP): Microsoft partner companies that a customer hires to build solutions on top of Azure
    - Payment and billing for Azure usage occur through the customer's CSP

### Usage meter

**Usage meter**: track's a resource's usage and generates a usage record that is used to calculate your bill.

- Resources are always charged _based on usage_

> For example, if you de-allocate (but do not delete) a VM, then you will not be billed for compute hours, I/O reads or writes or the private IP address since the VM is not running and has no allocated compute resources. However you will incur storage costs for the disks.

Factors affecting costs:

- Resource type: costs are resource-specific
- Services: rates and billing periods can differ between Enterprise, Web Direct, and Cloud Solution Provider (CSP) customers
- Location
- Azure billing zones: geographical grouping of Azure Regions for billing purposes
    - Inbound data transfers are free; outbound data transfers are priced based on billing zone
    - Billing zones aren't the same as Availability Zones

### Azure pricing calculator

**Azure pricing calculator**: a free web-based tool that allows you to estimate Azure costs

- Input Azure services and modify properties and options of the services
- Outputs the costs per service and total cost for the full estimate
- You can configure parameters:
    - Region
    - Tier
    - Billing Options
    - Support Options
    - Programs and Offers
    - Azure Dev/Test Pricing
- Supports export to Excel or sharing via custom URL

### Other cost management tools

**Azure Advisor**: a free service built into Azure that provides recommendations on high availability, security, performance, and cost.

Advisor makes cost recommendations in the following areas:

1. Reduce costs by eliminating unprovisioned Azure ExpressRoute circuits
1. Buy reserved instances to save money over pay-as-you-go
1. Right-size or shutdown underutilized virtual machines

**Azure Cost Management**: a free, built-in Azure tool for gaining greater insights into where your cloud money is going.

- Historical breakdowns of what services you are spending your money on and how it is tracking against budgets that you have set
- Set budgets, schedule reports, and analyze your cost areas

**Azure Total Cost of Ownership (TCO) calculator**: predict your cost savings from a migration to cloud

- You enter the details of your current on-premises infrastructure into TCO and tweak values of baseline assumptions
- The TCO calculator generates a detailed report based on the details you enter and the adjustments you make

### Ways to save on Azure infrastructure

- Use Azure credits: Visual Studio subscribers can activate a monthly credit benefit
- Use spending limits: help prevent you from exhausting the credit on your account within each billing period
    - When your Azure usage results in charges that use all the included monthly credit, the services that you deployed are disabled and turned off for the rest of that billing period
- Use reserved instances if you have VM workloads that are static and predictable
- Choose low-cost locations and regions
- Research available cost-saving offers
- Right-size underutilized virtual machines
- Deallocate virtual machines in off hours
- Delete unused virtual machines
- Migrate to PaaS or SaaS services: start with IaaS services and then move them to PaaS as appropriate, in an iterative process

### Ways to save on licensing costs

- Linux vs. Windows: the cost of the product can be different based on the OS you choose
- **Azure Hybrid Benefit for Windows Server**: gives customers who have previously purchased Windows Server licenses the right to use these licenses for virtual machines on Azure
- **Azure Hybrid Benefit for SQL Server**: an Azure-based benefit that enables you to use your SQL Server licenses with active Software Assurance to pay a reduced rate
- Dev/Test subscription offers: save costs on your non-production environments
- Use SQL Server Developer Edition: a free product for nonproduction use
