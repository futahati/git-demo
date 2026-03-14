# Markdown

- https://hackmd.io/@howkii-studio/markdown_intro

# Git

## 安裝／更新／建立

### 安裝

- 網站 https://git-scm.com/ => Install
- (2026/3/8)下載 Git for Windows/x64 Setup.
- (2026/3/8)Setup => Next到底 (最後畫面的 View Release Notes 取消勾勾) => Finish

### 更新至最新版本

- 打開 Git CMD 或 git Bash
- 指令 => git update-git-for-windows
  - Git Bash的貼上指令(Ctrl+V不能用！)
    - 滑鼠右鍵 => 選擇 Paste
    - 鍵盤 shift + Ins

### 確認是否安裝成功

- 呼叫CMD視窗(2擇1)
  - git CMD (Windows命令提示字元)
  - git Bash (Linux)
- 指令 => git (是否安裝Git)
- 指令 => git version (檢視Git版本)

### 建立／設定基本(全域)資訊 例：姓名 + email信箱

- 呼叫CMD視窗
  - git CMD (Windows命令提示字元)
    - 指令 => git config -- global user.name 英文名字
      - 例 指令： git config -- global user.name irw
    - 指令 => git config -- global user.email email信箱
      - 例 指令： git config -- global user.email futahati@gmail.com
  - 確認上述操作的基本資訊內容
    - 至 C:\Users\user\ 尋找 .gitconfig
    - 可直接「雙擊」，系統自動選擇程式開啟
    - 姓名、email資訊有誤，可直接修改後，Ctrl + S 儲存即可

## 指令介紹

### 建立專案 Git 初始化設定

- 在Vscode(新增終端機)呼叫終端機
  - Terminal => New Terminal 或 Ctrl + Shift + `
- 初始化
  - 指令 => git init
- 讓.git形成可見(初始化後，會產生 .git/ 隱藏資料夾)
  - File => Preferences => Settings
    - Files:Exclude (刪除 =>\*\*/.git ，形成可見的資料夾)
    - 注意 .git / Objects(所有變動歷程這裡可見) / info
    - 只控管「文字」，不控管「圖案、二進制檔案」
    - **.git/ ←資料夾勿手殘刪除**
- 建立不需要追蹤及版本記錄的隱藏檔
  - 新增檔名→ .gitignore
  - 將不需追蹤的檔案或資料夾，一行寫一個
    - 若是單檔案 => 檔案名稱.副檔名 例：3.txt
    - 若是資料夾 => 資料夾名稱 例：images/
- 建立說明文字檔(上傳GitHub前置作業，在push前)
  - 新增檔名→ README.md

### 控管狀態說明

- U => Untrack(未追蹤、未控管)
- A => Added(已加入控管)
- D => Deleted(刪除，因為已控管，可恢復刪除！git restore)
- M => Modified(已變更)

### 控管指令操作說明

- 檔案加入控管
  - git add
    | 指令| 說明 |
    | - | - |
    | git add 1.txt | 單一檔案加入控管 |
    | git add . | 將所有檔案加入控管(要注意是否有不需要加入控管的檔案) |

- 檢視控管狀態
  - git statust
    | 指令 | 說明 |
    | - | - |
    | git status | 檢視檔案狀態 |
    | git status -s | |
    | git status --short | |
  - 可見「所有」已控管，以及「所有」未控管的檔案
    | 狀態 | 說明 |
    | - | - |
    | 綠色字／A(added)模式 | 已加入控管/追蹤 |
    | 紅色字／U(Untrack)模式 | 未加入控管/追蹤(工作目錄區) |

- 檢視暫存區
  - git ls-files
    | 指令| 說明 |
    | - | - |
    | git ls-files | 每次最新的檔案，只顯示檔案名稱 |
    | git ls-files -s | 每次最新的檔案，顯示檔案編碼+檔案名稱 |

- 回復至上一步
  - git checkout
    | 指令 | 說明 |
    | - | - |
    | git checkout 檔案名稱.副檔名 | |
    | git checkout . | |

- 恢復刪除(Shift + Del永久刪除，若加入控管的檔案，可恢復)
  - git restore 1.txt

- 將暫存區資料，儲存/提交(儲存庫)倉庫區
  - git commit
    | 指令 | 說明 |
    | - | - |
    | git commit -m "說明文字" | |
    | git commit -a |(不用git add)一次性提交所有已被追蹤的檔案的修改，而不需要先用 git add 手動加入暫存區|
    | git commit -am "說明文字" | (不用git add)一步完成「加入修改」＋「提交」＋「寫訊息」 ※若有未被追蹤的檔案，不能使用|
    | git commit -a -m "說明文字"|同上|
    | git commit --amend | (要git add)回到上一個 commit，重新修改它 |
    | git commit --amend -m "說明文字"| 同上，**只是會覆蓋掉上一個 commit 的訊息** |
    | git commit | 有長文字輸入需求時，進入 vim 編輯器 |
  - **vim編輯器簡易指令**
    |指令|說明|
    |:-:|-|
    |i|進入「編輯模式」|
    |ESC鍵|退出「編輯/插入模式」|
    |:wq|儲存後離開|
    |:q!|不儲存，強制離開|

- 檢視(儲存庫)倉庫區
  - git log  
    | 指令 | 說明 |
    | - | - |
    | git log | 檢視commit過後的資訊；若資訊過多時，按enter，最後按 q 離開 |
    | git log --oneline | 檢視commit過後的簡易資訊；將每一筆提交顯示成單獨一行，對於檢視大量的提交時很有用 |

- 【分支】建立、新增、修改、刪除
  - git branch
    | 指令 | 說明 |
    | - | - |
    | git branch | 檢視所有分支名及所在分支名 |
    | git branch 分支名 | 建立／新增分支名 |
    | git branch -m 舊分支名 新分支名 | 修改分支名 |
    | git branch -D 分支名 | 刪除分支名 |
    | git log --oneline | 檢視(儲存庫/)倉庫區 |

- 切換分支
  - git checkout 用於在不同的分支之間切換、恢復文件、建立新分支等操作
    | 指令 | 說明 |
    | - | - |
    | git checkout 分支名 | 切換至分支名 |
    | git checkout -b 分支名 | 新增 + 切換至分支名 |
    | git log --oneline | 檢視(儲存庫/)倉庫區 |

- 將當下所有檔案加入控管(暫存區) + 提交(儲存庫)倉庫區
  - git status
  - git add .
  - git commit -m "說明文字"

#### 無分支時，常用固定步驟

- 開始使用git後，(無分支時)常用固定步驟
  - git pull
  - git status
  - git add .
  - git commit
  - git status
  - git checkout . --------恢復到 commit 前一個狀態
  - git log / git log --oneline

#### 有分支時，常用固定步驟(2合1：新增+切換)

- git pull
- git checkout -b 分支名 -------新增 + 切換至分支名
- git log --oneline ------------檢視(儲存庫)倉庫區
- git checkout -b text ------ 新增+切換至 text
  - 目前在 text 分支
    - git status
    - git add .
    - git commit
    - git status
    - git log / git log --oneline

- git checkout master ----------切換至主分支
- git merge 分支名 -------------合併分支(將分支合併至主分支)
- git log --oneline ------------(第2次)檢視(儲存庫/)倉庫區
- git branch -D 分支名 ---------刪除分支名
- git push ---------------------上傳GitHub

# github

- 申請github
- 上傳(綁定)到雲端 git remote add origin https://github.com/futahati/git-demo.git
- 檢視雲端網址 git remote -v
- (第一次)推送至雲端 git push -u origin 主支名稱 例：git push -u origin master
- 從雲端「推上」git push
- [強推] git push -f(-force 強制)

## 上傳(git push) GitHub 空間(第一次 + 後續上傳的指令；編輯至一段落，要記得上傳雲端。)

- 於 GitHub 建立遠端儲存庫
- 取得遠端儲存庫位址
  - git remote add origin 遠端儲存庫位址
- 新增『說明檔』(←確認是否已建立／新增)
  - README.md
- 上傳本地端儲存庫至『遠端儲存庫』
  - git push -u origin master(第一次push使用)
- 爾後，常用固定步驟、指令
  - git status
  - git add .
  - git commit
    - ##### 如果使用 git commit --amend 時
      - 進入➡️➡️vim
      - i → Esc → ：wq
      - 上傳遠端儲存庫時的指令要改為
      - git push -f

  - git checkout . --------恢復到 commit 前一個狀態
  - git push(第二次開始都用這個)
  - git status
  - git log / git log --oneline

## 下載(git clone／git pull)本地端

- 無專案在本地端時：
  - Git Bash(Git軟體內建的，Windows版的 Git 模擬器，使用 Linux 指令)
    - 使用 git clone 指令(會下載.git)
    - 登入GitHub取得儲存庫位址(複製)
    - 回到／開啟VScode，或使用…
      - git clone 貼上儲存庫位址
  - 使用 GitHub 提供的 Download Zip(不會有.git資料夾)
- 有專案在本地端時：
  - git pull

# Vscode

### 安裝

- 網站 https://code.visualstudio.com/
- (2026/3/8)點擊 Download for Windows 後會直接下載exe檔
- (2026/3/8)安裝程式 => (詢問不使用系統管理員安裝，按確定)我同意 => (打勾)建立桌面圖示 => 完成

### 設定布局樣式

- File => Preferences => Settings
  - Workbench:Color Theme (佈景模式 =>自行選用)
  - Editor:Mouse Wheel Zoom (打勾 =>使用滑鼠縮放視窗)
  - Editor:Format On Paste (打勾)
  - Files:Exclude (刪除 =>\*\*/.git ，形成可見的資料夾)

### 視窗設定

- Terminal視窗
  - View => Appearance => Align Panel => Justify
  - 快捷鍵 Ctrl + J 或 Ctrl + ` ==> 開啟／隱藏Terminal視窗
- 選單(File/Edit/Selection...)
  - View => Appearance => Menu Bar(取消勾勾，會在左側出現三條橫線)

### 專案開發，使用Open Folder

- File => Open Folder
  - Do you trust the authors of the files in this folder?
    - 打勾 Trust the authors of all files in the parent folder 'git'
    - 點擊 Yes, I trust the authors(我信任這個作者)

- Do you want to install the recommended 'Python' extension from Microsoft for the Python language?
  - 這個程式碼需安裝Python，是否安裝？ Install

### Terminal終端機設定(改為cmd) + Python環境設定

- PS開頭 是 Bash 的終端機
  - ctrl + shift + p => python:Select Interpreter => Python x.xx.x[版本號] ---------- Recommended
  - Ctrl + Shift + P => 進階尋找 Default => 選 Terminal:Select Default Profile => 選 Command Prompt

### 下載外部插件(快捷鍵Ctrl + Shift + X)

- python (Microsoft) / install
  - （右下角）選擇直譯器
- Black Formatter (Microsoft)
  - shift + alt + F(快捷鍵)
  - 程式碼上 → 按右鍵 → Format Document / Format Document With →設定
- Dracula Theme Official (Dracula Theme) / install ← 模板(Theme)
  - Dracula Official更換模板 → 點選插件/Set Color Theme
