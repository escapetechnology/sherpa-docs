---
layout: default
title: Sherpa Deadline Setup
parent: Admin Guide
nav_order: 5
---
# Sherpa Deadline Setup
<!-- TOC -->

- [Sherpa Deadline Setup](#sherpa-deadline-setup)
  - [Basic functionality](#basic-functionality)
    - [Deadline Super User Mode](#deadline-super-user-mode)
    - [Client Setup](#client-setup)
    - [Worker Settings](#worker-settings)
    - [Pulse Settings](#pulse-settings)
    - [Options](#options)
  - [Power Management](#power-management)
    - [Disable AWSPortal](#disable-awsportal)
    - [Configure Sherpa Event plugin](#configure-sherpa-event-plugin)
    - [Configure Power Management](#configure-power-management)
    - [Add Power Management Group](#add-power-management-group)
    - [Configure Idle Shutdown](#configure-idle-shutdown)
    - [Configure Machine Startup](#configure-machine-startup)
  - [Post configuration](#post-configuration)
    - [Configuration update](#configuration-update)
    - [Idle Shutdown in action](#idle-shutdown-in-action)

<!-- /TOC -->

Deadline is a fully feature render manager. Full documentation can be found at the following link.
<https://docs.thinkboxsoftware.com/>
The purpose of the documentation below is to cover configuration of Deadline in a Sherpa project.

## Basic functionality

For security reasons, Sherpa restricts how different resource types in a Sherpa project are allowed to talk to each other. To make Deadline work correctly in a Sherpa project you will have to make some configuration changes.

### Deadline Super User Mode

In order to make configuration change in Deadline you need to select _Tools -> Super User Mode._

![deadline-super-user-mode](/sherpa-docs/assets/images/deadline-super-user-mode.png)

Once selected you should see many more options. Now, under the _Tools_ menu select _Configure Repository Options..._.

![configure-repository-options](/sherpa-docs/assets/images/configure-repository-options.png)

### Client Setup

In the _Client Setup_ section, under the _General_ tab, select _Automatic Upgrades / Downgrades_.

![automatic-upgrades](/sherpa-docs/assets/images/automatic-upgrades.png)

In the _Client Setup_ section, under the _Remote Control_ tab, select _Remote Administration_ and _Disable the allow list_.

![remote-control](/sherpa-docs/assets/images/remote-control.png)

### Worker Settings

Under _Worker Settings_, make sure that _Global Remote Command Port Override_, _Use Worker's IP address ..._ and _Number of minutes before ..._ are set as indicated in the screen-grab below.

![worker-settings](/sherpa-docs/assets/images/worker-settings.png)

### Pulse Settings

Under _Pulse Settings_ in the _General_ tab, make sure that _Global Remote ..._ and _Use Pulse's IP Address ..._ are set as in the example below.

![pulse-settings](/sherpa-docs/assets/images/pulse-settings.png)

Under _Pulse Settings_ in the _Power Management_ tab, make sure that _Power Management Check ..._ is set to 60 as in the example below.

![pulse-power-management](/sherpa-docs/assets/images/pulse-power-management.png)

### Options

Under _Tools -> Options_ ...

![options](/sherpa-docs/assets/images/options.png)

Make sure _Enable Worker Pinging_ box is ticked.

![enable-worker-ping](/sherpa-docs/assets/images/enable-worker-ping.png)

The above will let you see quickly whether a render node/worker is contactable.

## Power Management

There is a **Sherpa Deadline Event** plugin which helps minimise your spend on render nodes by turning on existing render nodes when they are required and turning them off when they are not required.

To access the Sherpa Event plugin click on _Tools/Configure Events..._
![configure-events](/sherpa-docs/assets/images/configure-events.png)

### Disable AWSPortal

Disable AWS Portal by setting the _State_ to be _Disabled_.

![disable-aws-portal](/sherpa-docs/assets/images/disable-aws-portal.png)

### Configure Sherpa Event plugin

Make sure you have set the following correctly as per the screen-grab below.

- **State:** Globally Enabled
- **API Key:** This is your Sherpa admin username
- **API secret:** This is your Sherpa admin username password
- **Project ID:** This is the Sherpa project ID

![configure-sherpa-event-plugin](/sherpa-docs/assets/images/configure-sherpa-event-plugin.png)

### Configure Power Management

Select _Tools -> Configure Power Management ..._

![configure-power-management](/sherpa-docs/assets/images/configure-power-management.png)

### Add Power Management Group

You can list the render nodes individually but it can be easier just to specify a group that contains all the render nodes. _Machine Groups -> Add_

Make sure you have set the following correctly as per the screen-grab below.

- **Group Name:** All
- **Group Mode:** Enabled
- **Include All Workers in this Group:** Make sure this is enabled

![add-power-management-group](/sherpa-docs/assets/images/add-power-management-group.png)

### Configure Idle Shutdown

Make sure you have set the following correctly as per the screen-grab below.

- **Idle Shutdown Mode:** Enabled
- **Number of Minutes Before Idle Workers Will Be Shutdown:** 30
  - If you have a fixed number of render nodes then you can set this to something smaller like 5 minutes
  - If you are building workstations in Sherpa and have this set too low, you run the risk of Deadline shutting down a workstation before it has been successfully built.
- **Minimum Number of Workers to Leave Running:** 0

![configure-idle-shutdown](/sherpa-docs/assets/images/configure-idle-shutdown.png)

### Configure Machine Startup

Make sure you have set the following correctly as per the screen-grab below.

- **Machine startup Mode:** Enabled
- **Maximum Number of Workers to Wake Up Per Interval:** 5
  - Further up in this documentation we set the _Interval_ to be 60 secs.
  - Hence, if there were jobs in the Deadline queue waiting to be executed, the above settings would result in 5 existing render nodes being turned on every 60 secs.
- **Target Number of Extra Idle Workers:** 0

![configure-machine-startup](/sherpa-docs/assets/images/configure-machine-startup.png)

## Post configuration

### Configuration update

Configuration changes percolate through the system and can take up to 10 mins to take effect. The safest way to make sure that your configuration changes have taken effect is to stop the Deadline server, wait a couple of minutes and then start it up again. Use the following procedure.

- Shut down all the render nodes in Sherpa
- In the Deadline Monitor GUI
  - Select all the Workers
  - Right-click and select _Mark Worker as Offline_
  - Right Click and select _Delete Workers_
- In Sherpa, shut down the Render Manager and wait a couple of minutes
  - When the Render Manager is off the Deadline Monitor GUI will become unresponsive
- In Sherpa, turn on the Render Manager
  - Wait for the Deadline Monitor GUI to become responsive again
- Turn on all the render nodes in Sherpa

### Idle Shutdown in action

If you successfully configured power management then your system should behave as illustrated below.

![idle-shutdown-01](/sherpa-docs/assets/images/idle-shutdown-01.png)

Zooming in on some of the important detail from the screen-grab above ...

A. The render node is on-line and pingable.
![idle-shutdown-01a](/sherpa-docs/assets/images/idle-shutdown-01a.png)

B. The node has successfully checked in with the Sherpa Event plugin and its Sherpa name appears in the description field in the Deadline monitor worker view.
![idle-shutdown-01b](/sherpa-docs/assets/images/idle-shutdown-01b.png)

**Note:** If you do not see the name of the render node in this column then you have probably mistyped something when running through the _Configure Sherpa Event plugin_ section earlier in this document.

C. The render node has been idle for 1.6 minutes.
![idle-shutdown-01c](/sherpa-docs/assets/images/idle-shutdown-01c.png)

In the example below I have set the Idle Shutdown time to be 2 minute.
![idle-shutdown-02](/sherpa-docs/assets/images/idle-shutdown-02.png)

Hence after 2.5 minutes the render node has been switched off and is now being reported as _Timed Out_.
![idle-shutdown-02a](/sherpa-docs/assets/images/idle-shutdown-02a.png)

During the configuration process we set the _Number of minutes before an unresponsive Worker is marked as Stalled_ to 5 mins.
![idle-shutdown-03](/sherpa-docs/assets/images/idle-shutdown-03.png)

So 5 minutes later the render node turns red and gets marked as _Stalled_ (or _Offline_).
![idle-shutdown-03a](/sherpa-docs/assets/images/idle-shutdown-03a.png)

If your list of Workers gets messy, you can delete any stalled Workers from the list. When you turn the render nodes on again in Sherpa they will check in with Deadline and the Sherpa Event plugin and they will re-appear in the list of Workers in Deadline Monitor.
