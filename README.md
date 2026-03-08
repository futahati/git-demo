###1.安裝git
git version
- 檢視版本號

###2.安裝vscode
	
###3.使用git指令
建立「全域資訊」
- git config --global user.name your-name
- git config --global user.email futahati@gmail.com

- 查看上述指令是否成功，使用下述路徑看
- C:\Users\User\.gitconfig


###4.git初始化
- git init（下完指令後，會產生 .git/ 隱藏資料夾）
- .git/ ←資料夾勿手殘刪除


###5.git控管狀態說明
- U => Untrack(未追蹤、未控管)
- A => Added(已加入控管)
- D => Deleted(已刪除)
- M => Modified(已變更)

###6.git加上控管指令
- git add 1.txt
- git add .(加入所有變動，小心使用！！可一次控管全部，全部的 U=>A )
- git add guess_game.py(只控管一個檔案)

###7.git檢視控管狀態
- git status

###8.git恢復刪除
- git restore 1.txt

###9.vscode相關設定
- ctrl + shift + P
- 更改終端機(ps → C:開頭)
	- default termindl => cmd.exe

###10.設定git環境
- 要看到.git資料夾
- （加入不需要控管的檔案）新增.gitignore
	- 檔案名稱.副檔名 例：3.txt
	- 資料夾名稱/ 例：images/

###11.git檢視暫存區
- git ls-files
- git ls-files -s

###12.git（回復至上一動）
- git checkout 檔案名稱.副檔名
- git checkout .

###13.git(加入倉庫區)
- git commit -m "專案初始化完成"

###14.git（檢視倉庫）
- git log
- git log --oneline
- 若資訊過多時，按enter，最後按 q 離開

###15.git 分支概念
- master(主分支)
- git branch

###16.git 切換commit
- git checkout +commit sha的前5碼
	- 觀察當時的程式碼
- git checkout master

###17.git 新增分支
- git branch 分支名稱 例： - git branch test

###18.git 切換分支
- git checkout test

###19.git 合併分支
- git checkout master  (回到主分支)
- git merge test  (將分支合併到主分支)

###20.git 刪除分支
- git branch -D test

###21.github
- 申請github
- 上傳(綁定)到雲端 git remote add origin https://github.com/futahati/git-demo.git
- 檢視雲端網址 git remote -v
- (第一次)推送至雲端 git push -u origin 主支名稱 例：git push -u origin master
- 從雲端「拉取／拉下／下拉」git pull


###22.
###23.
###24.
###25.

