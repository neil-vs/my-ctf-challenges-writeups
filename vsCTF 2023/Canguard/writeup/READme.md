# Canguard?

## Motivation
I am an avid game-hacker in my free time, but I love doing forensics/reverse in CTF. I would have made more reversing challenges but we had invited one of my game-hacker friends (shoutout to 3dsboy08 for his difficult rev :P) so we didn't need more rev. I wanted to make a forensics challenge with a game-hacking approach, but without the rigorous amounts of rev, for both legal and difficulty reasons. Then I thought about making Canguard.

## **Solution Steps**

### **1. Identifying the Starting Point**
The initial logical step in such investigations would be to inspect the logs. If this isn't immediately apparent, a cursory exploration of the file system should lead you to a peculiar 'Logs' folder.

#### **Location**:
\Program Files\Riot Vanguard\Logs

### **2. Decrypting the Encrypted Logs**
Within the Logs folder, you'll come across a series of log files, seemingly encrypted. Given the age of these logs and the subsequent updates to Vanguard's encryption methods, our traditional decryption tools may not suffice.

This is where OSINT (Open Source Intelligence) comes into play. A quick Google search with the terms "vanguard log decrypt" leads us to a valuable resource: [Vanguard Log Decryptor](https://www.unknowncheats.me/forum/anti-cheat-bypass/488665-vanguard-log-decryptor.html).

Using the provided decryption code, we're initially met with a series of 'lorem ipsum' texts. Given the multitude of log files, it's advisable to modify the code to automate the decryption process across all files.

### **Flag**:
Upon successful decryption, a meticulous search (perhaps using grep) will reveal the flag embedded within `vgc_5146_2022-17-1_22_34-48.log`.

Flag: `vsctf{0h_w0W!_v4Ngu4rd_l0Gs_d3CrYpt3D_sHh!!_d0Nt_T3Ll_3vErd0X_>:(}`
(everdox is the lead AC dev for riot vanguard, gigachad)
