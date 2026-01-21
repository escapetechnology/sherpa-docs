---
layout: default
title: Generic servers in a Sherpa project
parent: Admin Guide
nav_order: 8
---
# Generic servers in a Sherpa project

Sherpa has pre-defined resource types; workstations, render nodes etc. There will be times when you want to create something that Sherpa does not provide out of the box; license server, build server, monitoring server etc

These generic servers can be built during the initial creation of a Sherpa project or can be added to an existing Sherpa project as shown below.

![add-generic-resource](/sherpa-docs/images/add-generic-resource.png)

Below is an example of a project in which I have built a license server and a monitoring server.

![generic-servers](/sherpa-docs/images/generic-servers.png)

If you have created a generic server that is providing a service that you need to access from your home, all you have to do is to add you IP address to the list as highlighted in red below.

![generic-resource-allow-list](/sherpa-docs/images/generic-resource-allow-list.png)
