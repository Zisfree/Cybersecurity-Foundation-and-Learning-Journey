# What is the loopback address?
- Loopback address aka 127.0.0.1 is an IP when devices need to send data to themselves. It is written as lo: in ifconfig.

## What is its use?
- Loopback addresses are used to check weather the applications is working or not before going to the internet.
- In servers it is used in the login website, where password and usernames are required.
- The server stores all the information including passwords and usernames in its databases.
- It will not want it to be public, so they use IP 127.0.0.1 so that server communicates its own database and the website as an API between the user and the database.
- The en--- is the users IP info.
- Also the 0.0.0.0 listens to all IP's on the users system. ex: If the user is using 2 different IP's then it listens to both of them.
<img width="728" height="190" alt="Screenshot from 2026-07-17 02-32-05" src="https://github.com/user-attachments/assets/3b3e4249-4a75-4e54-8289-415bb539fb6e" />

# What is netstat?
- Netstat is a tool in terminal which shows network connections, routing tables and interface statistics. In TCP & UDP all in IPv4

## Command info
- One command is to run `netstat -tulnp4` which returns us this:
<img width="1018" height="113" alt="Screenshot from 2026-07-17 02-29-59" src="https://github.com/user-attachments/assets/18187104-0567-4f79-9c18-50491534debd" />
- Removing the 'n' in -tulpn4 will replace IP:PORT from hostname:service.
