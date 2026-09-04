# What is Kerberos?
- It is a system in windows which is used to verify our messaging so that we don't have to verify it every single time.
- It contains a Authentication Server (AS) and a Ticket-Granting Service (TGS).
- Like if we enter in a network, we will enter a password which is sent to AS which checks if it is valid and if it is correct we get the TGS.
- Now every time we need to go somewhere in that network our system just needs to show the TGS.

## Why is it safe?
- Our password does not travel with the TGS. It is only used once and then not. That way our password stays secure.
