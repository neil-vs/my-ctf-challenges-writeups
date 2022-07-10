# Writeup

We are given an AD1 file and we can open it in FTK Imager through File > Add Evidence Item > Image File > Select.

We end up with 3 folders, Users, Perflogs, and Program Files. Now after completing the first part, we need to find the game that he played on his alt account. If we look through chrome logs, nothing is even mentioned about an alt account. What else can we find? We notice that Roblox is indeed installed in this system, could that mean that there are some debug logs available for us to view, and potentially find the data we seek?

Navigating to `C:\Users\adminbot6000\AppData\Local\Roblox\logs` we can see that there is 28 log files and a folder called `archive`. Going through the log files, we notice a pattern between all of them, they all contain a "joinScriptURL" which when looking at, you can see that userID as a parameter is listed, but the URL is encoded.

`{"jobId":"8a55cae8-f3c4-470c-90ab-3f3efbb062bc","status":2,"joinScriptUrl":"https://assetgame.roblox.com/Game/Join.ashx?ticketVersion=2&ticket=%7b%22UserId%22%3a3635455297%2c%22UserName%22%3a%22ftcsvisgreat%22%2c%22DisplayName%22%3a%22ftcsvisgreat%22%2c%22CharacterFetchUrl%22%3a%22https%3a%2f%2fapi.roblox.com%2fv1.1%2favatar-fetch%2f%3fplaceId%3d9928307557%26userId%3d3635455297%22%2c%22GameId%22%3a%228a55cae8-f3c4-470c-90ab-3f3efbb062bc%22%2c%22PlaceId%22%3a9928307557%2c%22UniverseId%22%3a3663017825%2c%22ServerId%22%3a131789%2c%22ServerPort%22%3a54792%2c%22IsTeleport%22%3afalse%2c%22FollowUserId%22%3anull%2c%22TimeStamp%22%3a%226%2f19%2f2022+6%3a58%3a05+PM%22%2c%22CharacterAppearanceId%22%3a3635455297%2c%22AlternateName%22%3anull%2c%22JoinTypeId%22%3a10%2c%22MatchmakingDecisionId%22%3a%22b38037af-3749-473c-a9f1-7ca6f898a51e%22%2c%22GameJoinMetadata%22%3a%7b%22JoinSource%22%3a0%2c%22RequestType%22` 

Once decoded, we get the following.

`https://assetgame.roblox.com/Game/Join.ashx?ticketVersion=2&ticket={"UserId":3635455297,"UserName":"ftcsvisgreat","DisplayName":"ftcsvisgreat","CharacterFetchUrl":"https://api.roblox.com/v1.1/avatar-fetch/?placeId=9928307557&userId=3635455297","GameId":"8a55cae8-f3c4-470c-90ab-3f3efbb062bc","PlaceId":9928307557,"UniverseId":3663017825,"ServerId":131789,"ServerPort":54792,"IsTeleport":false,"FollowUserId":null,"TimeStamp":"6/19/2022 6:58:05 PM","CharacterAppearanceId":3635455297,"AlternateName":null,"JoinTypeId":10,"MatchmakingDecisionId":"b38037af-3749-473c-a9f1-7ca6f898a51e","GameJoinMetadata":{"JoinSource":0,"RequestType`

In there we see "Username" but the username is the MAIN account of this person, so this cannot be what we seek. Now we proceed to go through all 28 files with the same process until we find a user which is not `ftcsvisgreat`.

Eventually we stumble across `0.531.0.5310423_20220620T033202Z_Player_9BB0E_last.log` which has the the data we are looking for. 
```{"UserId":3638382799,"UserName":"amazingmalt","DisplayName":"amazingmalt","CharacterFetchUrl":"https://api.roblox.com/v1.1/avatar-fetch/?placeId=69184822&userId=3638382799","GameId":"eb55fa0e-46b0-43c0-95b3-0b40340516d3","PlaceId":69184822,"UniverseId":31970568,"ServerId":127625,"ServerPort":50494,"IsTeleport":false,"FollowUserId":null,"TimeStamp":"6/19/2022 10:32:08 PM","CharacterAppearanceId":3638382799,"AlternateName":null,"JoinTypeId":10,"MatchmakingDecisionId":"9a395a8e-c694-4ece-aaea-6465ac869ef0","GameJoinMetadata":{"JoinSource":0,"RequestType":0,%```

Now we have found our anomaly, we need to find the *GAME* that he was playing on his alt account. We notice a field called `PlaceID` which once Googled, you find out that is the "internal" roblox ID for the game.

https://devforum.roblox.com/t/how-to-find-the-placeid-on-roblox/869711

From that forum post that can be found easily googling "how to find game from placeid roblox", we are able to construct this URL https://www.roblox.com/games/69184822/ which redirects us to https://www.roblox.com/games/69184822/Theme-Park-Tycoon-2 which is our flag!

Flag : `vsctf{themeparktycoon2}`