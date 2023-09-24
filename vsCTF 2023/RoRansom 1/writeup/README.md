# RoRansom 1

## **Motivation**
Growing up, Roblox played a significant role in my life. I have memories of exploiting the game back in 2016. Drawing from this nostalgia, I aimed to craft a challenge combining forensics, log analysis, and OSINT. Moreover, I wanted to elevate the difficulty in comparison to the previous year's vsCTF Roblox challenges.

## **Solution Steps**

### **1. Extracting from the Disk Image**
Given the context of the challenge, the initial step would be to identify any game join logs. This leads us to:
\Users\ftcsvisgreat\AppData\Local\Roblox\logs

### **2. Analyzing Log Files**
Upon inspecting the log files, a recurring parameter `placeId` becomes evident. This parameter is crucial as it helps in determining which game was accessed. This can be achieved by manipulating the URL on the Roblox website: 
https://www.roblox.com/games/placeID 
(For those familiar with the previous year's vsCTF, this technique should ring a bell.)

### **3. Identifying the Unique Log**
One log, in particular, stands out: `0.594.0.5940525_20230923T090345Z_Player_C1E0B_last.log`

`0.594.0.5940525_20230923T090345Z_Player_C1E0B_last.log`
```2023-09-23T09:03:47.080Z,2.080817,7e7c,6 [FLog::GameJoinUtil] GameJoinUtil::joinGamePostStandard: URL: https://gamejoin.roblox.com/v1/join-game BODY: {"placeId":14853367450,"gameJoinAttemptId":"1a9f943e-6d6b-44d8-a4e6-50b15171c737"}```

Following this `placeId` directs us to a basic game at:
https://www.roblox.com/games/14853367450/ftcsvthrowaways-Place


### **4. Investigating for Leftover Code**
The challenge description hints at the possibility of some remnant code within the game, left behind due to the hacker's oversight. In real-world scenarios, developers sometimes inadvertently leave debug code in production environments. Some detective work or basic OSINT could lead you to the Roblox debugger console, which can be accessed using the F9 key. Alternatively, checking the log file where you joined the game and searching for "vsctf" could yield results.

Upon investigation, you'll stumble upon this message:

`[ftcsvisgreatisnotgr8's Debugger] FATAL ERROR! Error Code: vsctf{d0nt_l3av3_y0ur_d3bug_c0de_1n_4_pr0d_env!}`

### **Conclusion**
GG! You've now identified the hacker's actual Roblox username and successfully retrieved the flag for this challenge.