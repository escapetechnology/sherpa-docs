---
layout: default
title: Multi Factor Authentication
parent: Admin Guide
nav_order: 11
---
# Multi Factor Authentication

For additional security, you can enable Multi-Factor Authentication. With MFA enabled for a Sherpa project the user will not only be required to supply their username and password but they will also be required to provide a six digit code which will be sent to the email address associated with their Sherpa username.

To enable MFA for a Sherpa project, go to the Project Detail page.

1. Click on the pencil icon to edit the project details
2. Tick *Enable One Time Password authentication*
3. Press *Update Details*

![enable-otp](/sherpa-docs/images/enable-otp.png)

The user logs in using the PCoIP client as normal.

![otp-phase1](/sherpa-docs/images/otp-phase1.png)

With OTP/MFA enabled the user will be presented with a second screen requesting the input of a verification code.

![otp-phase2](/sherpa-docs/images/otp-phase2.png)

The verification coed is sent to the email address associated with the user's Sherpa login. The email will look similar to the below.

![otp-email](/sherpa-docs/images/otp-email.png)

Paste the verification code from the email into the OTP box and then press LOGIN.

![otp-phase3](/sherpa-docs/images/otp-phase3.png)

You will then be presented with a list of workstations as normal.
