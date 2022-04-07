# Riot-API
Data from Riot's api, for future use in training a model

I drew some graphs to see what impacted the chances of winning a game the most. Damage, Kills, Deaths, etc.
It seems shorter games with higher K/D have the biggest impact. Followed by deaths. Damage dealt seems to be the most consistent factor one can modify.

<img width="631" alt="Screen Shot 2022-04-07 at 8 57 07" src="https://user-images.githubusercontent.com/89398401/162094491-49e280d0-adce-457a-a2ec-923a2dec362b.png">
<img width="631" alt="Screen Shot 2022-04-07 at 8 57 58" src="https://user-images.githubusercontent.com/89398401/162094502-baf03729-5500-4ba5-aff6-51d2b3b6eaf4.png">
<img width="629" alt="Screen Shot 2022-04-07 at 8 58 31" src="https://user-images.githubusercontent.com/89398401/162094506-bf983fd6-3441-4bb0-ab69-8cdd037a2292.png">


<img width="631" alt="Screen Shot 2022-04-07 at 9 05 05" src="https://user-images.githubusercontent.com/89398401/162094508-fbb40eba-53db-418b-b11c-4d8966438bd2.png">

For K/D, I added 1 to Deaths to prevent division by zero. Doesn't really affect that much the result, but there are probably better ways to get around this.

<img width="612" alt="Screen Shot 2022-04-07 at 9 05 47" src="https://user-images.githubusercontent.com/89398401/162094510-ac11b95a-19c1-4ca0-aa86-9a6532431a84.png">
<img width="604" alt="Screen Shot 2022-04-07 at 9 06 25" src="https://user-images.githubusercontent.com/89398401/162094512-7571f16c-8c79-4bc4-96fc-6ec611834cba.png">

After assesing the data, I started buying stopwatch, and Zhonya's first despite outputting less damage. This switch seems to have been beneficial. 
