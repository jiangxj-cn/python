import tkinter
import tkinter.messagebox,tkinter.simpledialog
import os,os.path
import threading
rubbishExt=['.tmp1','.old1']


def GetDrives():
    drives=[]
    for i in range(65,91):
        vol=chr(i)+':/';
        if os.path.isdir(vol):
            drives.append(vol)
    return tuple(drives)


class Window:
    drives=[];
    def __init__(self):
        self.root=tkinter.Tk()
        #create menu
        menu=tkinter.Menu(self.root)

        submenu=tkinter.Menu(menu,tearoff=0)
        submenu.add_command(label="关于..",command=self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label="退出",command=self.MenuExit)
        menu.add_cascade(label="系统",menu=submenu)

        submenu=tkinter.Menu(menu,tearoff=0)
        submenu.add_command(label="查找垃圾文件",command=self.MenuScanRubbish)
        submenu.add_separator()
        submenu.add_command(label="删除垃圾文件",command=self.MenuDelRubbish)
        menu.add_cascade(label="清理",menu=submenu)


        submenu=tkinter.Menu(menu,tearoff=0)
        submenu.add_command(label="搜索大文件",command=self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label="按名字寻找文件",command=self.MenuSearchFile)
        menu.add_cascade(label="搜索",menu=submenu)



        self.root.config(menu=menu)
        self.progress=tkinter.Label(self.root,anchor=tkinter.W, text="状态",compound='left')
        self.progress.place(x=10,y=370,width=480,height=15)

        self.flist=tkinter.Text(self.root)
        self.flist.place(x=10,y=10,width=480,height=350)



        self.vscroll=tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side='right',fill='y')
        self.flist['yscrollcommand']=self.vscroll.set
        self.vscroll['command']=self.flist.yview

    def mainLoop(self):
        self.root.title("FindFat")
        self.root.minsize(500,400)
        self.root.maxsize(500,400)
        self.root.mainloop()
    def MenuAbout(self):
        tkinter.messagebox.showinfo("Findfat","this is a window program by Python")
    def MenuExit(self):
        self.root.quit();
    def MenuScanBigFile(self):
        s=tkinter.simpledialog.askinteger("FindFat","请设置大文件的大小（M）:")
        t=threading.Thread(target=self.ScanBigFiles, args=(s,))
        t.start()
    def MenuSearchFile(self):
        s=tkinter.simpledialog.askstring("FindFat","请输入要查找的文件名称:")
        t=threading.Thread(target=self.ScanFilesByName, args=(s,))
        t.start()
    def MenuScanRubbish(self):
        result=tkinter.messagebox.askquestion("FindFat","ScanRubbish?")
        if result=='no':
            return
        tkinter.messagebox.showinfo("FindFat","begin ScanRubbish")
        #self.ScanRubbish()
        self.drives=GetDrives()
        t=threading.Thread(target=self.ScanRubbish, args=(self.drives,))
        t.start()

    def MenuDelRubbish(self):
        result=tkinter.messagebox.askquestion("FindFat","DelRubbish?")
        if result=='no':
            return
        tkinter.messagebox.showinfo("FindFat","begin DelRubbish")
        self.drives=GetDrives()
        t=threading.Thread(target=self.DelRubbish, args=(self.drives,))
        t.start()
    def ScanBigFiles(self,fileSize):
        total=0
        fileSize=fileSize*1024*1024
        for dirve in GetDrives():
            for root,dirs,files in os.walk(dirve):
                for fil in files:
                    try:
                        fname=os.path.join(os.path.abspath(root),fil)
                        fsize=os.path.getsize(fname)
                        self.progress['text']=fname
                        if fsize>fileSize:
                            total+=1
                            self.flist.insert(tkinter.END,'%s,%.f2 M \n' %(fname,fsize/1024/1024))
                    except:
                        pass
    def ScanFilesByName(self,fileName):
        total=0
        fileName=fileName.upper()
        for dirve in GetDrives():
            for root,dirs,files in os.walk(dirve):
                for fil in files:
                    try:
                        fname=os.path.join(os.path.abspath(root),fil)
                        self.progress['text']=fname
                        if fil.upper().find(fileName)>=0:
                            total+=1
                            self.flist.insert(tkinter.END,fname+'\n')
                    except:
                        pass
    def ScanRubbish(self,scanpath):
        global rubbishExt
        total=0
        filesize=0
        for dirve in scanpath:
            for root,dirs,files in os.walk(dirve):
                try:
                    for fil in files:
                        filesplit=os.path.splitext(fil)
                        if filesplit[1]=='':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1])>=0:
                                fname=os.path.join(os.path.abspath(root),fil)
                                filesize+=os.path.getsize(fname)
                                if total%20==0:
                                    self.flist.delete(0.0,tkinter.END)
                                self.flist.insert(tkinter.END,fname+'\n')
                                l=len(fname)
                                if l>60:
                                    self.progress['text']=fname[:30]+'...'+fname[l-30:l]
                                else:
                                    self.progress['text']=fname
                                total+=1
                        except Exception as ex:
                            print(ex)
                            pass
                except Exception as e:
                    print(e)
                    pass
            self.progress["text"]="找到 %s 个文件，共占用 %.2f M磁盘空间" %(total,filesize/1024/1024)

    def DelRubbish(self,scanpath):
        global rubbishExt
        total=0
        filesize=0
        for dirve in scanpath:
            for root,dirs,files in os.walk(dirve):
                try:
                    for fil in files:
                        filesplit=os.path.splitext(fil)
                        if filesplit[1]=='':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1])>=0:
                                fname=os.path.join(os.path.abspath(root),fil)
                                filesize+=os.path.getsize(fname)
                                try:
                                    os.remove(fname)
                                    if total%20==0:
                                        self.flist.delete(0.0,tkinter.END)
                                    self.flist.insert(tkinter.END,fname+'\n')

                                    l=len(fname)
                                    if l>60:
                                        self.progress['text']=fname[:30]+'...'+fname[l-30:l]
                                    else:
                                        self.progress['text']=fname
                                    total+=1
                                except:
                                     pass
                        except Exception as ex:
                            print(ex)
                            pass
                except Exception as e:
                    print(e)
                    pass
            self.progress["text"]="找到 %s 个文件，共占用 %.2f M磁盘空间" %(total,filesize/1024/1024)
if __name__=="__main__":
    window=Window()
    window.mainLoop()





