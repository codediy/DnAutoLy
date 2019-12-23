dnPath = "E:\\DN\\Game\\DragonNest\\DragonNest.exe"  #龙之谷exe路径
openMaxNum = 20 #开多次分解 建议20
BagKey = "i" #背包快捷键


isRun = 0

def dc(p):       
    # 点击延迟
    Settings.ClickDelay = 0
    click(p)
    
def dRc(p):
    # 点击延迟
    Settings.ClickDelay = 0
    rightClick(p)

def dt(k):
    Settings.TypeDelay = 0.1
    type(k)

def openLyBag():
    global openMaxNum
    
    if not exists("Left"):
        dt(BagKey)
        wait(1)
        
    openNum = 0;
  

    while openNum < openMaxNum :
        if not isRun == 1:
           break
       
        dRc("Dz")
        dc("OpenYes")
        wait(3)
        dc("closeOpen")
        openNum = openNum + 1
    

def openFenJie():
    if not exists("Left"):
        dt(BagKey)
        wait(1)

    dt(Key.ESC)
    wait(1)
    mouseDown(Button.LEFT)
    mouseUp(Button.LEFT)
    wait(1)
    dc("startFenJie")
    wait(3)

def longYuFenJie():
    openFenJie()
    
    ly = ["LongYu1","LongYu2","LongYu3","LongYu4","LongYu5","LongYu6"]
    fenJieNum = 0
    
    allLy = findAnyList(ly)
    
    for match in allLy:
        if not isRun == 1:
           break
        
        dRc(Location(match.getX()+15,match.getY()+20))
        goFenJie()

    closeFenJie()

def longYuFenJiev2():
    openFenJie()
    
    ly = ["LongYu1","LongYu2","LongYu3","LongYu4","LongYu5","LongYu6"]
    fenJieNum = 0
    maxNum = 4
    
    for item in ly:
        if exists(item):
            checkFind = findAll(item)

            # 未找到跳过
            if checkFind == None:
                continue
            
            matches = list(getLastMatches())

            # 遍历
            for match in matches:
                if exists("overNum"):
                    dc("closeOpen")
                    goFenJie()
                    fenJieNum = 0  
                
                else:
                    if fenJieNum < maxNum:
                        dRc(Location(match.getX()+15,match.getY()+20))
                        fenJieNum = fenJieNum + 1
                        
                        
                    else:
                        print "fenJieNum:",fenJieNum
                        goFenJie() 
                        fenJieNum = 0   
           
            # 判定是否还有多余的
            if fenJieNum > 0:
               goFenJie()
               fenJieNum = 0  
         
    fenJieNum = 0
    closeFenJie()
        
def goFenJie():
    dc("fj")       
    wait(0.5)
    dc("fjOk")

def closeFenJie():
    dt(Key.ESC)
    wait(0.5)
    
    if not exists("Left"):
        dt(BagKey)
        wait(1)
    
    wait(1)
    
def Init():
    Settings.setShowActions(True)
    Settings.MoveMouseDelay = 0
    setThrowException(False)
    
    # 提示等待
    popup("CTRL+F2 On/Off")
     
def loop():
    while 1:
        if isRun == 0:
            Debug.user("wait...")
            
        if isRun == 1:
            Debug.user("Run...")
            # 打开龙玉袋子
            openLyBag()
            longYuFenJiev2()
            longYuFenJiev2()

        if isRun == 2:
            Debug.user("Close")
            break;
        
def openApp(event):
    global isRun
    global dnPath
    
    if isRun == 1:
        isRun = 2
        Debug.user("app close")
        return

   
    dn = App("DragonNest")
    
    if not dn.hasWindow():
        App.open(dnPath)
        wait("Title")
        dn.focus()

    
    isRun = 1; 
    Debug.user("app Start")
    
    loop()
   

def testFindFail():
    setThrowException(False)
    allLy = findAll("LongYu1")
    print allLy == None 


Init()
Env.addHotkey(Key.F2, KeyModifier.CTRL, openApp)