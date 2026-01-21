---
layout: default
title: How do I build my first Sherpa project?
parent: Admin Guide
nav_order: 2
---
# How do I build my first Sherpa project?

The goal of this exercise is to walk you through creating your first Sherpa project. During the process we will bring to light various decision points and best practices.

Log into Sherpa using your admin account details. Select **Projects** in the left hand menu and then click on **Create a new project**.

![Create a new project](/sherpa-docs/images/create-a-new-project.png)

We will be building a Sherpa project that contains all the required infrastructure for a team of creative professionals. Select **Born In The Cloud**.

![Select-born-in-the-cloud](/sherpa-docs/images/select-born-in-the-cloud.png)

Give the project a **Name** and select the cloud **Provider**.

![Project name and cloud provider](/sherpa-docs/images/project-name-and-cloud-provider.png)

Currently, Sherpa is capable of managing infrastructure in AWS. In the near future it will be capable of handling infrastructure in other cloud providers.

Sherpa can manage infrastructure in any location run by the cloud provider. By default you will be shown a small subset of what is available.

**Select a location that is geographically closest to the bulk of your team.**

![Select a location](/sherpa-docs/images/select-a-location.png)

Choosing a location close to you will minimise the latency and lead to a better user experience. If the locations listed seem too far away for you, we can make other locations available to you.

Press **Next**.

On this page you will now be presented with a kit of parts; **Workstations**, **Shared Storage**, **Render Manager** and **Render Nodes**.

**We will be building one of each**. This is the normal approach. Once built, we can then install all our favourite software on the workstation and the render nodes and test that everything works as expected. Once it is all built we can create **Golden Images** of the workstation and render node and then create as many workstations and render nodes of whatever spec is required.

Let's fill in some details for the workstation.

![Workstation build spec](/sherpa-docs/images/workstation-build-spec.png)

Under **Select build profile** we can see that we are building a Linux workstation. If the **?** icon is clicked/hovered, it will also shows us the versions of the PCoIP agent and Deadline client that will be installed.

The pricing is shown as a running total on the bar at the bottom of the screen in a nice simple fashion. In the screen-grab above, we can see that the **Workstation** will cost us £42.87 if we use it for 50 hours a week. The estimate also shows a **Display Gateway**. There is one **Display Gateway** for each Sherpa project. All artists connect through the **Display Gateway** in order to gain access to their workstations. **If the Display Gateway is off, no-one will be able to access their workstations.**

If a workstation, is off, there is still a small charge associated with things like software licensing costs and storage. If you wish to pay nothing for your workstation you should delete it. Generally speaking the cost of a workstation that isn't being used so generally it is OK to leave it sitting there and switched off.

Managing costs in a cloud environment is all about **right-sizing**. Given that this is your first Sherpa project and you are just experimenting, keep everything small.

Let's complete the configuration for the **Shared Storage**, **Render Manager** and **Render Nodes**. Remember, keep everything small.
Note: The **?** will offer more information about your selection.

![Shared storage](/sherpa-docs/images/shared-storage.png)

![Render manager](/sherpa-docs/images/render-manager.png)

![Render node](/sherpa-docs/images/render-node.png)

The **Weekly Estimate** bar from the bottom of the screen shows the cost estimate, if you click on the **^**, it will expand and you can see a more detailed view.

![Updated estimate](/sherpa-docs/images/updated-estimate.png)

Go to the bottom of the page and press **Next**.

On the next page make sure you select an SSH key. When we create your admin Sherpa account we create an SSH key for you. SSH keys are used for accessing Linux machines. Creation of SSH keys and their use is covered in another document. For now select the key that appears in your dropdown.

![SSH key selection](/sherpa-docs/images/ssh-key-selection.png)

We will cover **VPNs** and **Snowflakes** in another document. For now press **Next** and confirm your choice.

You will now be directed to **Summary** page. Once your happy with your choices, click **Create**.

![Summary page](/sherpa-docs/images/summary-page-1.png)

Your project will initially go into a **Saved** state.

![Project saved](/sherpa-docs/images/project-saved.png)

Shortly after it should go into a **Building** state.

![Project building](/sherpa-docs/images/project-building.png)

After some time it will finish **Building** and go into a **Built** state.

![Project built](/sherpa-docs/images/project-built.png)

It takes about 25 minutes to build a Sherpa project containing Linux workstations. Windows workstations take longer to build at about 45 minutes.

You only build a Sherpa project once. You can then turn on and off the servers and workstations as required. It takes about 1 to 2 minutes for a workstation to become ready after you have turned it on. In order to control costs, a workstation will automatically shut itself down after 30+ minutes if nobody has logged into it.

Now we can move onto the next stage which is allowing a user access to the Sherpa project and inviting them to a workstation.
