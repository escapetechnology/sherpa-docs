---
layout: default
title: Allowed IP addresses and security
parent: Admin Guide
nav_order: 3.2
---
# Allowed IP addresses and security

The IP Allow List is used to control access to a Sherpa project from the outside world.

## IP Addresses and CIDR notation

Most of the time you will be using the IP address to control access to workstations in a Sherpa project. The user will have to tell you their public IP. Get them to type "what's my IP" into a browser or get them to visit <https://ifconfig.co/> or  <https://www.whatsmyip.org/>. If they see an option it is the IPv4 address that is required.

### Subnet masks

#### /32

Using /32 is the **preferred** option when specifying an IP address. The "/32" is the subnet mask. The /32 subnet mask means all 32 bits of the IP address are fixed. Therefore, 81.82.83.84/32 refers to exactly one single IP address, and no others.

There may be situations where the user's IP address is not fixed. They may be with an Internet Service Provider that changes their IP address on a regular basis.

#### /24

If the user's IP address keeps changing but the first three numbers are always the same you can use /24 when specifying the IP address. The /24 means the subnet mask is 255.255.255.0. That's because 24 ones in binary is: 11111111.11111111.11111111.00000000. So 81.82.83.0/24 would allow any IP addresses between 81.82.83.0 and 81.82.83.255.

#### /16

Similarly /16 is even more permissive. If the user's IP address keeps changing but the first two numbers are always the same, you can use /16 when specifying the IP address. The /16 means the subnet mask is 255.255.0.0. That's because 16 ones in binary is: 11111111.11111111.00000000.00000000. So 81.82.0.0/16 would allow any IP addresses between 81.82.0.0 and 81.82.255.255.

#### 0.0.0.0/0

In extreme circumstances it may be necessary to allow access to the Sherpa project from anywhere. In that case you can use 0.0.0.0/0 as the IP address. This allow-all IP address can only be applied to a Display Gateway (see the scope section below). We strongly advise not using this IP as it opens up the Display Gateway to a potentially infinite attack vector.

If you have to use 0.0.0.0/0 we would recommend turning on **Enable One Time Password** authentication on the Sherpa project. This will require the user to type in their username, their password and a six digit number that is emailed to the email address they used when signing up to Sherpa.

## Scope

When you add an IP address to the allow list you get to specify the scope of the IP address.

### Display Gateway

Most of the time you will be using the IP address to control access to a Sherpa workstation through the **Display Gateway**. If this is the case you should select **Display Gateway** for the Scope.

### Virtual Private Networks

If you have created a **Remote Access VPN** inside your Sherpa project for remote administrative access, you should select **Virtual Private Networks** for the Scope.

If you have created a **Site-To-Site VPN** inside your Sherpa project you should add the public IP address of the other end of the VPN tunnel to the allow list and set the Scope to **Virtual Private Networks**.

### Generic Servers

If you have created a **Generic Resource** that is providing a service you can add the public IP address of the system that is allowed access to that service and select **Generic Servers** for the Scope.

## Administration

Make sure to keep access to your Sherpa project as tight as possible and delete any IPs in the allow list that are no longer required.
