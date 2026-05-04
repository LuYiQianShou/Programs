#START:Import modules
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from functools import partial
#END:Import modules
#endregion
#region
#START:Window
Window=Tk()
ScreenWidth=Window.winfo_screenwidth()
ScreenHeight=Window.winfo_screenheight()
WindowX=ScreenWidth/2-1040/2
WindowY=round(ScreenHeight/2-635/2-35)
Window.title("Tkinter控件展览季")
Window.geometry(f"1040x635+{int(WindowX)}+{int(WindowY)}")
#END:Window
#endregion
#region
#Start:TextFrame
TextFrame=LabelFrame(Window,text="文字区",bg="lightgray",font=("仿宋",16,"bold"),
                     width=450,height=235)
TextFrame.grid(row=0,column=0,padx=5,pady=5)
TextFrame.grid_propagate(False)
texts=[
    ("你好！","green"),("别来无恙啊！","red"),("今天心情怎么样？","orange"),
    ("色彩缤纷！","blue"),("今天我们去动物园怎么样？那有很多小动物！","gray"),
    ("我去药店买药，你去买碗！","orange"),("GUI真强大呀！","blue")
]
for i,(t,c) in enumerate(texts):
    Label(TextFrame,text=t,bg="lightgray",fg=c,
          font=("楷体",16)).grid(row=i,column=0,sticky="w")
#END:TextFrame
#endregion
#region
#START:ButtonFrame
Money=0
ButtonFrame=LabelFrame(Window,text="按钮区",bg="lightgray",
                       font=("仿宋",16,"bold"),width=570,
                       height=235)
ButtonFrame.grid(row=0,column=1,padx=5,pady=5)
ButtonFrame.grid_propagate(False)
money_label=Label(ButtonFrame,text=f"您的余额：${Money}",
                  bg="lightgray",fg="black",font=("黑体",
                  16))
money_label.grid(row=0,column=0,pady=10,sticky="w")
def add_money(amount):
    global Money
    if Money<100000:Money+=amount;money_label.config(
        text=f"您的余额：${Money}")
def sub_money(amount):
    global Money
    if Money>=amount:Money-=amount;money_label.config(
        text=f"您的余额：${Money}")
def money_to_0():
    global Money;Money=0;money_label.config(text=f"您的余额：${Money}")
Button(ButtonFrame,text="余额清零",font=("宋体",16),fg="gray",
       width=18,command=money_to_0).grid(row=0,
       column=1,padx=0,pady=0,sticky="w")
Button(ButtonFrame,text="我要十美元来买菜！",font=("宋体",
       16),fg="green",width=18,command=partial(add_money,10\
       )).grid(row=1,column=0,padx=0,pady=0,sticky="w")
Button(ButtonFrame,text="我拿十美元去买菜",font=("宋体",
       16),fg="green",width=18,command=partial(sub_money,10\
       )).grid(row=1,column=1,padx=0,pady=0,sticky="w")
Button(ButtonFrame,text="我要一百美元，来买机器！",font=(
       "宋体",16),fg="red",width=23,command=partial(add_money,100\
       )).grid(row=2,column=0,padx=0,pady=0,sticky="w")
Button(ButtonFrame,text="我拿一百美元，去买机器！",font=(
       "宋体",16),fg="red",width=23,command=partial(sub_money,100\
       )).grid(row=2,column=1,padx=0,pady=0,sticky="w")
Button(ButtonFrame,text="我买一台电脑，要一千美元！",font=(
       "宋体",16),fg="purple",width=25,command=partial(add_money,1000\
       )).grid(row=3,column=0,padx=0,pady=0,sticky="w")
Button(ButtonFrame,text="我用一千美元，去买台电脑！",font=(
       "宋体",16),fg="purple",width=25,command=partial(sub_money,1000\
       )).grid(row=3,column=1,padx=0,pady=0,sticky="w")
Button(ButtonFrame,text="我要一万美元，去造机房！",font=(
       "宋体",16),fg="purple",width=23,command=partial(add_money,10000\
       )).grid(row=4,column=0,padx=0,pady=0,sticky="w")
Button(ButtonFrame,text="我用一万美元，去造机房！",font=(
       "宋体",16),fg="purple",width=23,command=partial(sub_money,10000\
       )).grid(row=4,column=1,padx=0,pady=0,sticky="w")
#END:ButtonFrame
#endregion
#region
#START:ScrollInputFrame
ScrollInputFrame=LabelFrame(Window,text="输入区",bg="lightgray",font=("仿宋",16,
                            "bold"),width=450,height=180)
ScrollInputFrame.grid(row=1,column=0,padx=5,pady=5)
ScrollInputFrame.grid_propagate(False)
scrolledtext.ScrolledText(ScrollInputFrame,width=36,height=7,font=("黑体",
                          16)).grid(row=0,column=0,padx=0,pady=0)
#END:ScrollInputFrame
#START:MenuFrame
MenuChoiceFrame=LabelFrame(Window,text="列选区",bg="lightgray",font=("仿宋",16,
                     "bold"),width=570,height=180)
MenuChoiceFrame.grid(row=1,column=1,padx=5,pady=5)
MenuChoiceFrame.grid_propagate(False)
Label(MenuChoiceFrame,text="选择你最喜欢的编程语言：",bg="lightgray",fg="green",
      font=("黑体",16)).grid(row=0,column=0,padx=0,pady=0,sticky="w")
LANGUAGES=["Python","C","C++","C#","Java","JavaScript","TypeScript",
           "PHP","Go","Rust","Swift","Kotlin","B","HTML","Other"]
ttk.Combobox(MenuChoiceFrame,values=LANGUAGES,font=("仿宋",14),width=20,
             state="readonly").grid(row=1,column=0,padx=0,pady=0)
Label(MenuChoiceFrame,text="选择你最喜欢的水果：",bg="lightgray",fg="green",
      font=("黑体",16)).grid(row=0,column=1,padx=0,pady=0,sticky="w")
FRUIT=["Apple","Banana","Watermelon","Blueberry","Strawberry","Grape",
       "Cucumber","Tomato","Other"]
ttk.Combobox(MenuChoiceFrame,values=FRUIT,font=("仿宋",14),width=20,state="readonly")\
.grid(row=1,column=1,padx=0,pady=0)
Label(MenuChoiceFrame,text="选择你最喜欢的操作系统：",bg="lightgray",fg="green",
      font=("黑体",16)).grid(row=2,column=0,padx=0,pady=0,sticky="w")
OS=["Windows","macOS","iOS","Linux","Unix","Other"]
ttk.Combobox(MenuChoiceFrame,values=OS,font=("仿宋",14),width=20,state="readonly")\
.grid(row=3,column=0,padx=0,pady=0)
Label(MenuChoiceFrame,text="选择你最喜欢的季节：",bg="lightgray",fg="green",
      font=("黑体",16)).grid(row=2,column=1,padx=0,pady=0,sticky="w")
SEASONS=["Spring","Summer","Autumn","Winter","Sunny Season","Rainy Season"]
ttk.Combobox(MenuChoiceFrame,values=SEASONS,font=("仿宋",14),width=20,state="readonly")\
.grid(row=3,column=1,padx=0,pady=0)
Label(MenuChoiceFrame,text="选择你最喜欢的电子设备：",bg="lightgray",fg="green",
      font=("黑体",16)).grid(row=4,column=0,padx=0,pady=0,sticky="w")
COMPUTERS=["PC","iPhone","iPad","Other"]
ttk.Combobox(MenuChoiceFrame,values=COMPUTERS,font=("仿宋",14),width=20,
             state="readonly").grid(row=5,column=0,padx=0,pady=0)
Label(MenuChoiceFrame,text="选择你最喜欢的地方：",bg="lightgray",fg="green",
      font=("黑体",16)).grid(row=4,column=1,padx=0,pady=0,sticky="w")
PLACES=["Park","Garden","Sea","City","Village","Forest","Beach","Other"]
ttk.Combobox(MenuChoiceFrame,values=PLACES,font=("仿宋",14),width=20,state="readonly")\
.grid(row=5,column=1,padx=0,pady=0)
#END:MenuFrame
#endregion
#region
#START:ChoiceFrame
ChoiceFrame=LabelFrame(Window,text="复选区",bg="lightgray",font=("仿宋",16,"bold"),
                       width=450,height=180)
ChoiceFrame.grid(row=2,column=0,padx=5,pady=5)
ChoiceFrame.grid_propagate(False)
Var1=IntVar();Var2=IntVar();Var3=IntVar()
Var4=IntVar();Var5=IntVar();Var6=IntVar()
vars_list=[IntVar() for _ in range(6)]
subjects=["语文","数学","英语","科学","劳动","美术"]
for i,(subject,var) in enumerate(zip(subjects,vars_list)):
    check=ttk.Checkbutton(ChoiceFrame,text=subject,variable=var)
    check.grid(row=i//2,column=i%2,padx=10,pady=5,sticky="w")
Label(ChoiceFrame,text="在上面勾选你喜欢的学科，\n并取消勾选你不喜欢的学科。",
      bg="lightgray",fg="blue",font=("等线",16)).grid(row=3,column=0,
      padx=0,pady=0)
#END:ChoiceFrame
#endregion
#region
#START:TreeFrame
ButtonMenuFrame=LabelFrame(Window,text="菜单区",bg="lightgray",font=("仿宋",16,"bold"),
                           width=570,height=180)
ButtonMenuFrame.grid(row=2,column=1,padx=5,pady=5)
ButtonMenuFrame.grid_propagate(False)
ButtonMenuFrame.grid_rowconfigure(0,weight=1)
ButtonMenuFrame.grid_columnconfigure(0,weight=1)
Tree=ttk.Treeview(ButtonMenuFrame,show="tree",height=8)

Tree.insert("","end","file",text="📁文件操作",open=False)
Tree.insert("file","end","new_file",text="📄新建文件",open=False)
Tree.insert("new_file","end","program",text="📒新建项目")
Tree.insert("new_file","end","text",text="🧾新建文本文件")
Tree.insert("new_file","end","code_text",text="📃新建编程源代码")
Tree.insert("file","end","open_file",text="📂打开文件",open=False)
Tree.insert("open_file","end",text="📦打开项目")
Tree.insert("open_file","end",text="📖打开源代码或文本文件")
Tree.insert("file","end","code_text_do",text="📮源代码操作",open=False)
Tree.insert("code_text_do","end","run_file",text="🔨运行")
Tree.insert("code_text_do","end","stop_run_file",text="🛑终止运行")
Tree.insert("code_text_do","end","compile",text="🔑编译",open=False)
Tree.insert("compile","end","dynamic",text="🧵动态链接库")
Tree.insert("compile","end","static",text="⛓静态链接库")
Tree.insert("code_text_do","end","stop_compile",text="🛑终止编译")
Tree.insert("code_text_do","end","debug",text="😼调试",open=False)
Tree.insert("debug","end","run a sentence",text="➡执行一条语句")
Tree.insert("debug","end","run to stop_dot",text="➡➡🛑执行到断点")
Tree.insert("debug","end","run to function",text="➡➡📦执行到函数")
Tree.insert("debug","end","to function",text="➡📦⬅进入函数")
Tree.insert("debug","end","function to",text="⬅📦➡跳出函数并一次执行完函数剩余部分")
Tree.insert("debug","end","run to over",text="➡➡🆗执行完整个文件剩余语句")
Tree.insert("debug","end","debug_pause",text="⏸暂停以修改代码")
Tree.insert("debug","end","debug_over",text="🛑结束调试")
Tree.insert("code_text_do","end","performance_analysis",text="📊性能分析",open=False)
Tree.insert("performance_analysis","end","quick_analysis",text="🐇快速")
Tree.insert("performance_analysis","end","precise_analysis",text="🎯精准")
Tree.insert("performance_analysis","end","DPI",text="❌📊删除性能信息")
Tree.insert("code_text_do","end","jump_to",text="🏹跳转到",open=False)
Tree.insert("jump_to","end","file_head",text="🤖文件头")
Tree.insert("jump_to","end","next_line_head",text="⬇⬅下一行开头")
Tree.insert("jump_to","end","previous_line_end",text="⬆➡上一行结尾")
Tree.insert("jump_to","end","file_end",text="🐈文件尾")
Tree.insert("file","end","compress",text="📚压缩",open=False)
Tree.insert("compress","end","compress_only",text="📚仅压缩")
Tree.insert("compress","end","pack_only",text="📦仅打包")
Tree.insert("compress","end","compress and pack",text="📚📦压缩并打包")
Tree.insert("compress","end","pack and compress",text="📦📚打包并压缩")

Tree.insert("","end","edit",text="🔪编辑操作",open=False)
Tree.insert("edit","end","cut",text="✂剪切")
Tree.insert("edit","end","copy",text="📄📄复制")
Tree.insert("edit","end","paste",text="📝粘贴")
Tree.insert("edit","end","find",text="🔍查找",open=False)
Tree.insert("find","end","quick_find",text="🐇快速")
Tree.insert("find","end","energy_find",text="🎍节能")
Tree.insert("edit","end","cancel",text="◀◀撤销")
Tree.insert("edit","end","choice_line",text="📏选中此行")
Tree.insert("edit","end","choice_all",text="📐选中文件所有内容")
Tree.insert("edit","end","case_tool",text="🔠🔡🔧英文大小写工具",open=False)
Tree.insert("case_tool","end","uppercase",text="🔠将所选内容中的英文字母大写")
Tree.insert("case_tool","end","lowercase",text="🔡将所选内容中的英文字母小写")
Tree.insert("case_tool","end","toggle_case",text="🔠🔁🔡将所选内容中的英文字母颠倒大小写")
Tree.insert("case_tool","end","special_word_uppercase",text="💮🔠将所选内容中的专有名词首字母大写")
Tree.insert("case_tool","end","caution_uppercase",text="❗🔠将所选内容中的警示语所有字母大写")
Tree.insert("case_tool","end","do_for_sentence",text="💬🔠接下来一次关于大小写的操作只作用于完整的句子")
Tree.insert("case_tool","end","choice_line_many_uppercase_text",text="📏🔗🔠将此行连续最长的大写英文字母选中")
Tree.insert("case_tool","end","choice_line_many_lowercase_text",text="📏🔗🔠将此行连续最长的小写英文字母选中")
Tree.insert("case_tool","end","tool_4_to_6",text="🧮综合操作4~6")

Tree.insert("","end","view",text="👁‍🗨查看操作",open=False)
Tree.insert("view","end","font_size",text="🔢字号",open=False)
Tree.insert("font_size","end","6",text="6")
Tree.insert("font_size","end","8",text="8")
Tree.insert("font_size","end","9",text="9")
Tree.insert("font_size","end","10",text="10")
Tree.insert("font_size","end","11.5",text="11.5")
Tree.insert("font_size","end","12",text="12")
Tree.insert("font_size","end","13",text="13")
Tree.insert("font_size","end","14",text="14")
Tree.insert("font_size","end","15",text="15")
Tree.insert("font_size","end","16",text="16")
Tree.insert("font_size","end","17.5",text="17.5")
Tree.insert("font_size","end","18",text="18")
Tree.insert("font_size","end","20",text="20")
Tree.insert("font_size","end","24",text="24")
Tree.insert("font_size","end","28",text="28")
Tree.insert("font_size","end","32",text="32")
Tree.insert("font_size","end","36",text="36")
Tree.insert("font_size","end","42",text="42")
Tree.insert("font_size","end","48",text="48")
Tree.insert("font_size","end","56",text="56")
Tree.insert("font_size","end","72",text="72")
Tree.insert("font_size","end","96",text="96")
Tree.insert("font_size","end","144",text="144")
Tree.insert("font_size","end","224",text="224")
Tree.insert("font_size","end","256",text="256")
Tree.insert("font_size","end","384",text="384")
Tree.insert("font_size","end","512",text="512")
Tree.insert("font_size","end","640",text="640")
Tree.insert("font_size","end","720",text="720")
Tree.insert("font_size","end","960",text="960")
Tree.insert("font_size","end","1080",text="1080")
Tree.insert("font_size","end","1280",text="1280")
Tree.insert("font_size","end","1540",text="1540")
Tree.insert("font_size","end","2160",text="2160")
Tree.insert("font_size","end","3840",text="3840")
Tree.insert("font_size","end","6400",text="6400")
Tree.insert("font_size","end","9600",text="9600")
Tree.insert("font_size","end","10032",text="10032")
Tree.insert("font_size","end","65536",text="65536")
Tree.insert("font_size","end","18446744073709551616")
Tree.insert("font_size","end",
            "1.1579208923731619542357098500869e+77",
            text="1.1579208923731619542357098500869e+77")
Tree.insert("font_size","end",
            "1.3407807929942597099574024998206e+154",
            text="1.3407807929942597099574024998206e+154")
Tree.insert("font_size","end",
            "1.0907481356194159294629842447338e+2466",
            text="1.0907481356194159294629842447338e+2466")
Tree.insert("view","end","quick_zoom",text="🎚快速缩放",open=False)
Tree.insert("quick_zoom","end","25%",text="25%")
Tree.insert("quick_zoom","end","50%",text="50%")
Tree.insert("quick_zoom","end","75%",text="75%")
Tree.insert("quick_zoom","end","100%",text="100%")
Tree.insert("quick_zoom","end","125%",text="125%")
Tree.insert("quick_zoom","end","150%",text="150%")
Tree.insert("quick_zoom","end","200%",text="200%")
Tree.insert("quick_zoom","end","300%",text="300%")
Tree.insert("view","end","highlight",text="🔠语法高亮",open=False)
Tree.insert("highlight","end","enable",text="✅启用")
Tree.insert("highlight","end","disable",text="❎禁用")

Tree.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
scrollbar=ttk.Scrollbar(ButtonMenuFrame,orient="vertical",command=Tree.yview)
scrollbar.grid(row=0,column=1,sticky="ns")
Tree.configure(yscrollcommand=scrollbar.set)
#END:TreeFrame
#endregion
Window.mainloop()