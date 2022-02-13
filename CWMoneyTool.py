import os

def main():
    fileName = chooseFile('.iDB')
    print(fileName)

def chooseFile(fileType):
    stop = 0
    errorMsg = ""
    # 初始目錄
    originalPath = os.getcwd()

    while stop == 0:
        # 初始化
        fileList = []
        folderList = [".."]
        count = 0
        os.system('cls')
        # 取得目前目錄下的檔案與資料夾
        currentPath = os.getcwd()
        files = os.listdir(currentPath)
        # 顯示資訊
        print("\n  輸入目錄編號或檔案編號進行操作\n")
        print("  目前路徑為{path}\n".format(path = currentPath))
        # 遞迴分類及檢查
        for f in files:
            fullpath = os.path.join(currentPath, f)
            if os.path.isfile(fullpath):
                # 檔案:檢查副檔名
                extension = os.path.splitext(f)[1]
                if(extension == fileType):
                    fileList.append(f)
            elif os.path.isdir(fullpath):
                # 資料夾:新增到列表
                if(f[0] != "."):
                    folderList.append(f)
        # 顯示目錄
        print('目錄：')
        for folderName in folderList:
            print('  "{number}" {name}'.format(number = count, name = folderName))
            count+=1
        # 顯示檔案
        print('\n檔案：')
        if len(fileList) == 0:
            print('  找不到 iDB 檔')
        for fileName in fileList:
            print('  "{number}" {name}'.format(number = count, name = fileName))
            count+=1
        # 其他
        print('\n若要離開，請輸入 "q" or "Q"')
        if errorMsg != "":
            print(errorMsg)
        # 等待使用者操作
        action = input()
        # 離開
        if action == "q" or action == "Q":
            return ""
        # 編號
        elif action.isdigit():
            action = int(action)
            folderCount = len(folderList)
            fileCount = len(fileList)
            # 選擇資料夾
            if action >= 0 and action < folderCount:
                os.chdir(folderList[action])
                errorMsg = ""
            # 選擇檔案
            elif action >= folderCount and action < folderCount+fileCount:
                os.chdir(originalPath)
                return fileList[action - folderCount]
            # 編號有誤
            else:
                errorMsg = '資料有誤 請重新輸入'
        # 資料不符合
        else:
            errorMsg = '資料有誤 請重新輸入'

if __name__ == '__main__':
    main()
