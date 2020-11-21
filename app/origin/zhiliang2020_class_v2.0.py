#!/usr/bin/python
#  coding=utf-8（Python编辑器的“设置文件编码”设置成utf-8）
# ==============================================================================
#
#        Version:  2.0
#       Filename:  zhiliang2020_class2.0.py
#    Description:  2020成都海派质量月知识竞赛答题系统
#        Created:  2020-10-26
#         Author:  NiBinbin
#
# ==============================================================================

from tkinter import *
from tkinter.ttk import *
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.ttk as ttk
import xlrd  #调用Excel数据前需先导入（需要先在CMD下运行：pip3 install xlrd）
import random  #随机数函数调用导入
from PIL import Image,ImageTk #图像函数调用导入（需要先在CMD下运行：pip3 install pillow）
from datetime import datetime

global teams
teams = {'SMT':100,'组包':100,'质量':100,'工程':100,'资材':100,'行政':100,'HR':100}

#显示首页面
class basedesk():
    def __init__(self,master):
        self.window = master
        self.window.config()
        self.window.title('2020年成都海派质量月知识竞赛')
        self.window.geometry('1280x720')
        initface0(self.window)

class initface0():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='lightblue')
        self.initface0 = tk.Frame(self.master,width=1200,height=650,relief=RAISED)
        self.initface0.pack()
        self.f_style()
        self.face00()

    def f_style(self,):
        self.f = ttk.Style()
        self.f.configure('R40.TLabel',font=('Arial',40,'bold'),foreground='red')
        self.f.configure('R20.TLabel',font=('Arial',20),foreground='blue')         
        self.f.configure('A20.TLabel', font=('Arial', 20))
        self.f.configure('B24.TButton', font=('Arial', 24))
        self.f.configure('Q.TButton', font=('Arial', 24),background='blue')  	
        
    def face00(self,):
        main_title = '2020年成都海派质量月知识竞赛'
        dt = datetime.today()
        main_title1 = '主办单位：品质部、公司工会'
        lab0 = Label(self.initface0,text='  ',style='A20.TLabel')
        lab0.pack(pady=40)                
        lab = Label(self.initface0,text=main_title,style='R40.TLabel',width=90)
        lab.pack(padx=240)
        lab1 = Label(self.initface0,text=main_title1,style='R20.TLabel')
        lab1.pack(pady=40)
        lab1 = Label(self.initface0,text='（ '+dt.strftime('%Y年%m月%d日')+' ）',style='R20.TLabel')
        lab1.pack()        
        btn1 = Button(self.initface0,text='答题开始',style='B24.TButton',command=self.change1)
        btn1.pack(side=LEFT,padx=230)
        btn0 = Button(self.initface0,text=' 退出 ',style='B24.TButton',command=self.master.quit)
        btn0.pack(side=RIGHT,padx=230)
        lab9 = Label(self.initface0,text='  ')
        lab9.pack(pady=200)

    def change1(self,):       
        self.initface0.destroy()
        initface(self.master)
        
class initface():
    def __init__(self,master):
        self.master = master
        self.master.config(bg='lightblue')
        self.initface = tk.Frame(self.master,width=1200,height=650,relief=RAISED)
        self.initface.pack()
        
        self.z_style()
        self.f_title()           
        self.point_rules()
        self.slogan()
        self.add_point()
        self.add_pointB()
        self.change_point()
        self.face0()

    def z_style(self,):
        self.z = ttk.Style()
        self.z.configure('red.TFrame',font=('Arial',24),foreground='red')
        self.z.configure('red.TLabelFrame',font=('Arial',24),foreground='red')        
        self.z.configure('A14.TLabel',font=('Arial',12))         
        self.z.configure('A20.TLabel', font=('Arial', 20))
        self.z.configure('A14.TCombobox',font=('Arial',14))
        self.z.configure('A20.TButton', font=('Arial', 18))
        self.z.configure('Q.TButton', font=('Arial', 16,'bold'),background='blue')  		

    def f_title(self,):
        main_title = '2020年成都海派质量月知识竞赛选题与计分页面'
        lab = tk.Label(self.initface,text=main_title,font=('Arial', 28,'bold'),foreground='red',width=90)
        lab.pack(padx=120,pady=20)		
        
    def point_rules(self,):
        point_rule = tk.LabelFrame(self.initface,text='比赛积分规则',font=(16),fg='blue',width=600,height=300)
        rule11 = '一、抢答题'
        lab_rule11 = Label(point_rule,text=rule11,style='A14.TLabel')
        lab_rule11.grid(row=0,column=0,padx=10,pady=10,sticky=W)                
        rule1 = '1、单选题答对加1分，答错扣1分。'
        lab_rule1 = Label(point_rule,text=rule1,style='A14.TLabel')
        lab_rule1.grid(row=1,column=0,padx=10,pady=5)
        rule2 = '2、多选题答对加2分，答错扣2分。'
        lab_rule2 = Label(point_rule,text=rule2,style='A14.TLabel')
        lab_rule2.grid(row=2,column=0,padx=10,pady=5)
        rule3 = '3、判断题答对加1分，答错扣1分。'
        lab_rule3 = Label(point_rule,text=rule3,style='A14.TLabel')
        lab_rule3.grid(row=3,column=0,padx=10,pady=10)
        rule22 = '二、必答题'
        lab_rule22 = Label(point_rule,text=rule22,style='A14.TLabel')
        lab_rule22.grid(row=4,column=0,padx=10,pady=5,sticky=W)        
        rule4 = '4、每组1道简答题20分，裁判评分。'
        lab_rule4 = Label(point_rule,text=rule4,style='A14.TLabel')
        lab_rule4.grid(row=5,column=0,padx=10,pady=5)                
        point_rule.place(x=50,y=100)

    def slogan(self,):
        slogan1 = ' 质 量 第 一 '
        slogan2 = ' 客 户 至 上 '
        lab = tk.Label(self.initface,text=slogan1,font=('Arial', 28,'bold'),foreground='red',relief=RAISED)
        lab.place(x=80,y=370)
        lab = tk.Label(self.initface,text=slogan2,font=('Arial', 28,'bold'),foreground='red',relief=RAISED)
        lab.place(x=80,y=430)        		

    def add_point(self,):
        add_points = tk.LabelFrame(self.initface,text='抢答题计分区域',font=(16),fg='blue',width=400,height=300)
        tixing0 = Label(add_points,text='  题型  ',style='A14.TLabel')
        tixing0.grid(row=0,column=1,padx=10,pady=10)
        team0 = Label(add_points,text='  组别  ',style='A14.TLabel')
        team0.grid(row=0,column=0)
        TorF = Label(add_points,text='  正误  ',style='A14.TLabel')
        TorF.grid(row=0,column=2,padx=10,pady=5)
        self.var1 = StringVar()
        self.var1.set('单选题')
        tixings = ['单选题','多选题','判断题']
        self.TX = Combobox(add_points,textvariable=self.var1,value=tixings,style='A14.TCombobox',width=12)
        self.TX.grid(row=1,column=1,pady=10)
        self.var2 = tk.StringVar()
        self.var2.set('SMT')
        keys1 = teams.keys()
        keys = []
        for key in keys1:
            keys.append(key)
        self.team = Combobox(add_points,textvariable=self.var2,value=keys,width=12)
        self.team.grid(row=1,column=0,padx=5)
        self.var3 = tk.StringVar()
        self.var3.set('回答正确')      
        TFs = ['回答正确','回答错误']
        self.TF = Combobox(add_points,textvariable=self.var3,value=TFs,width=12)
        self.TF.grid(row=1,column=2)                 
        add_button = Button(add_points,text=' OK ',width=8,command=self.add_point1)        
        add_button.grid(row=1,column=3)
        add_points.place(x=800,y=100)        
        
    def add_point1(self,):
        self.var10 = self.var1.get()
        self.var20 = self.var2.get()        
        self.var30 = self.var3.get()        
        # 判断题型
        self.add_point = 0
        if self.var10 == '单选题' or self.var10 == '判断题':
            self.add_point = 1
        else:
            self.add_point = 2
		# 根据抢答对错，对抢答组加减分
        point = teams[self.var20]
        if self.var30 == '回答正确':
            teams[self.var20] = point+self.add_point
        else:
            teams[self.var20] = point-self.add_point
        point = teams[self.var20]     
        self.initface.destroy()
        initface(self.master)

    def add_pointB(self,):
        add_pointsB = tk.LabelFrame(self.initface,text='必答题（简答题）计分区域',font=(16),fg='blue',width=400,height=200)
        self.var4 = tk.StringVar()
        self.var4.set('SMT')
        keys1 = teams.keys()
        keys = []
        for key in keys1:
            keys.append(key)
        self.team = Combobox(add_pointsB,textvariable=self.var4,value=keys,width=12)
        self.team.grid(row=0,column=0,padx=10,pady=15)        
        BLabel = Label(add_pointsB,text='请输入裁判评分： ',width=15)
        BLabel.grid(row=0,column=1)
        self.BEntry = tk.Entry(add_pointsB,width=12)
        self.BEntry.grid(row=0,column=2,padx=5,pady=5)
        B_OK = Button(add_pointsB,text=' OK ',width=8,command=self.add_pointB1)
        B_OK.grid(row=0,column=3)
        add_pointsB.place(x=800,y=260)        	

    def add_pointB1(self,):
        self.add_pointB = self.BEntry.get()		
        self.var40 = self.var4.get()
        point = teams[self.var40]
        teams[self.var40] = point+int(self.add_pointB)
        point = teams[self.var40]     
        self.initface.destroy()
        initface(self.master)
        
    def change_point(self,):
        change_points = tk.LabelFrame(self.initface,text='更正积分区域',font=(16),fg='blue',width=400,height=200)
        self.var5 = tk.StringVar()
        self.var5.set('SMT')
        keys1 = teams.keys()
        keys = []
        for key in keys1:
            keys.append(key)
        self.team = Combobox(change_points,textvariable=self.var5,value=keys,width=12)
        self.team.grid(row=0,column=0,padx=10,pady=15)        
        BLabel = Label(change_points,text='请输入正确积分： ',width=15)
        BLabel.grid(row=0,column=1)
        self.CEntry = Entry(change_points,width=12)
        self.CEntry.grid(row=0,column=2,padx=5,pady=5)
        B_OK = Button(change_points,text=' OK ',width=8,command=self.change_point1)
        B_OK.grid(row=0,column=3)
        change_points.place(x=800,y=400)        	

    def change_point1(self,):
        self.change_point = self.CEntry.get()
        self.var50 = self.var5.get()        		
        teams[self.var50] = int(self.change_point)
        self.initface.destroy()
        initface(self.master)        	               	        

    def face0(self,):
        top_points = tk.LabelFrame(self.initface,text='成绩排行榜',font=(16,),fg='red',width=600,height=300)
        number0 = Label(top_points,text='  名次  ',style='A20.TLabel')
        number0.grid(row=0,column=0,padx=20,pady=5)
        team0 = Label(top_points,text='  组别  ',style='A20.TLabel')
        team0.grid(row=0,column=1)
        point0 = Label(top_points,text='  积分  ',style='A20.TLabel')
        point0.grid(row=0,column=2,padx=20,pady=5)
        
        # 根据得分排序（teams倒排序）
        abc = zip(teams.values(),teams.keys())
        aaa = sorted(list(abc),reverse = True)
        teams.clear()
        for y,x in aaa:
            teams.update({x:y})
        
        keys1 = teams.keys()
        keys = []
        for key in keys1:
            keys.append(key)		
        for i in range(7):
            number = Label(top_points,text='  '+str(i+1)+'  ',style='A20.TLabel',relief=RAISED)
            number.grid(row=i+1,column=0)
            team = Label(top_points,text='  '+keys[i]+'部  ',style='A20.TLabel',relief=RAISED)
            team.grid(row=i+1,column=1,padx=5,pady=5)
            team_key = keys[i]
            point = Label(top_points,text='  '+str(teams[team_key])+'  ',style='A20.TLabel',relief=RAISED)
            point.grid(row=i+1,column=2)
        top_points.place(x=375,y=100)
        
        lab00 = ttk.Label(self.initface,text=' ',style='A20.TLabel')
        lab00.pack(padx=1200,pady=160)
        btn10 = ttk.Button(self.initface,text='返回首页',style='Q.TButton',command=self.change0)
        btn10.pack(side=LEFT,padx=50,pady=90,fill=Y)        
        btn1 = ttk.Button(self.initface,text=' 单选题 ',style='A20.TButton',command=self.change1)
        btn1.place(x=280,y=535)        
        btn2 = ttk.Button(self.initface,text=' 多选题 ',style='A20.TButton',command=self.change2)
        btn2.place(x=480,y=535)        
        btn3 = ttk.Button(self.initface,text=' 判断题 ',style='A20.TButton',command=self.change3)
        btn3.place(x=680,y=535)        
        btn4 = ttk.Button(self.initface,text=' 简答题 ',style='A20.TButton',command=self.change4)
        btn4.place(x=880,y=535)                        
        btn0 = ttk.Button(self.initface,text=' 退出 ',style='Q.TButton',command=self.master.quit)
        btn0.place(x=1100,y=535)

    def change0(self,):       
        self.initface.destroy()
        initface0(self.master)

    def change1(self,):       
        self.initface.destroy()
        face1(self.master)
                
    def change2(self,):       
        self.initface.destroy()
        face2(self.master)
        
    def change3(self,):       
        self.initface.destroy()
        face3(self.master)
        
    def change4(self,):       
        self.initface.destroy()
        face4(self.master)
    
# 单选题界面 face1
class face1():
	def __init__(self,master):
		self.master = master
		self.master.config(bg='blue')
		self.face1 = tk.Frame(self.master,)
		self.face1.pack()
		self.f1_style()
		self.display_tixing()
		self.display_sub()
		self.radio_1()
		self.comeback()
		
	def f1_style(self,):
		self.f1 = ttk.Style()
		self.f1.configure('red.TLabel',font=('Arial',24),foreground='red')
		self.f1.configure('A20.TLabel', font=('Arial', 20))
		self.f1.configure('R20.TLabel', font=('Arial', 20),foreground='red')
		self.f1.configure('B16.TRadiobutton', font=('Arial', 16))
		self.f1.configure('Q.TButton', font=('Arial', 24,'bold'),foreground='red',background='blue') 	 		
        		
	def display_tixing(self):
		tixing_title = '2020年质量知识竞赛（单选题）'
		lab0 = Label(self.face1,text='  ',style='A20.TLabel')
		lab0.pack(pady=20)  		
		tixing = Label(self.face1, text=tixing_title, style='red.TLabel',width=1280)
		tixing.pack(padx=390)
		lab00 = Label(self.face1,text='  ',style='A20.TLabel')
		lab00.pack()
		
	def display_sub(self):
	# 显示题目
		self.xl = xlrd.open_workbook(r'2020zhiliang.xls')
		self.table = self.xl.sheets()[0]		
		self.qty = self.table.nrows-1 # 获取excel表格总行数
		self.abc = random.randint(1,self.qty)
		timu_and_keys = []
		self.display_timu()
		timu_and_keys.append(self.timu)
		timu_and_keys.append(self.answerkey1)
		timu_and_keys.append(self.answerkey2)
		timu_and_keys.append(self.answerkey3)
		timu_and_keys.append(self.answerkey4)
		timu_and_keys.append(self.key_00)
		self.timu_and_keys = timu_and_keys
		tk_message1 = tk.Message(self.face1,text=self.timu_and_keys[0],font=('Arial', 16,'bold'),width=800)
		tk_message1.pack()

	def display_timu(self):
		self.timu = self.table.cell(self.abc,2).value
		self.answerkey1 = self.table.cell(self.abc,3).value
		self.answerkey2 = self.table.cell(self.abc,4).value
		self.answerkey3 = self.table.cell(self.abc,5).value
		self.answerkey4 = self.table.cell(self.abc,6).value
		self.answerkey0 = self.table.cell(self.abc,7).value
		self.key_00 = self.answerkey0[0:1]
	def letter_to_number(self):
		if self.timu_and_keys[5] == "A":
			self.number1 = 1
		elif self.timu_and_keys[5] == "B":
			self.number1 = 2
		elif self.timu_and_keys[5] == "C":
			self.number1 = 3
		else:
			self.number1 = 4
	def selection(self):
		self.letter_to_number()
		if self.number1 == self.radio.get():
			selection1 = "回答正确 " 
		else:
			selection1 = "回答错误！ 正确答案是 " +self.timu_and_keys[5]
		self.label.config(text = selection1)
	def radio_1(self):
		self.radio = IntVar()
		tk.answer1_message = Radiobutton(self.face1,text=self.timu_and_keys[1],style='B16.TRadiobutton',variable=self.radio, value=1,command=self.selection,width=800)
		tk.answer1_message.place(x=400,y=230)
		tk.answer2_message = Radiobutton(self.face1,text=self.timu_and_keys[2],style='B16.TRadiobutton',variable=self.radio, value=2,command=self.selection,width=800)
		tk.answer2_message.place(x=400,y=270)
		tk.answer3_message = Radiobutton(self.face1,text=self.timu_and_keys[3],style='B16.TRadiobutton',variable=self.radio, value=3,command=self.selection,width=800)
		tk.answer3_message.place(x=400,y=310)
		tk.answer4_message = Radiobutton(self.face1,text=self.timu_and_keys[4],style='B16.TRadiobutton',variable=self.radio, value=4,command=self.selection,width=800)
		tk.answer4_message.place(x=400,y=350)
		self.label = Label(self.face1,style='R20.TLabel')
		self.label.place(x=500,y=420)
		
	def comeback(self):
		lab0 = Label(self.face1,text='  ')
		lab0.pack(anchor=E,pady=150)  			
		btn1 = Button(self.face1,text=' 返回 ',style='Q.TButton',command=self.change1)
		btn1.pack(anchor=SE,padx=200)
		lab0 = Label(self.face1,text='  ')
		lab0.pack(pady=150)  					
		
	def change1(self,):
		self.face1.destroy()
		initface(self.master)

# 多选题界面 face2
class face2():
	def __init__(self,master):
		self.master = master
		self.master.config(bg='blue')
		self.face2 = tk.Frame(self.master,)
		self.face2.pack()
		self.f2_style()
		self.display_tixing()
		self.display_sub()
		self.checkbutton()
		self.comeback()

	def f2_style(self,):
		self.f2 = ttk.Style()
		self.f2.configure('red.TLabel',font=('Arial',24),foreground='red')
		self.f2.configure('A20.TLabel', font=('Arial', 20))
		self.f2.configure('R20.TLabel', font=('Arial', 20),foreground='red')
		self.f2.configure('B24.TButton', font=('Arial', 24))		
		self.f2.configure('B16.TCheckbutton', font=('Arial', 16))
		self.f2.configure('Q.TButton', font=('Arial', 24,'bold'),foreground='red',background='blue') 	
        		
	def display_tixing(self):
		tixing_title = '2020年质量知识竞赛（多选题）'
		lab0 = Label(self.face2,text='  ',style='A20.TLabel')
		lab0.pack(pady=20)  		
		tixing = Label(self.face2, text=tixing_title, style='red.TLabel',width=1280)
		tixing.pack(padx=390)
		lab00 = Label(self.face2,text='  ',style='A20.TLabel')
		lab00.pack()
		
	def display_sub(self):
		# 显示题目
		self.xl = xlrd.open_workbook(r'2020zhiliang.xls')
		self.table = self.xl.sheets()[1]		
		self.qty = self.table.nrows-1 # 获取excel表格总行数
		self.abc = random.randint(1,self.qty)
		timu_and_keys = []
		self.display_timu()
		timu_and_keys.append(self.timu)
		timu_and_keys.append(self.answerkey1)
		timu_and_keys.append(self.answerkey2)
		timu_and_keys.append(self.answerkey3)
		timu_and_keys.append(self.answerkey4)
		self.timu_and_keys = timu_and_keys
		tk_message1 = tk.Message(self.face2,text=self.timu_and_keys[0],font=('Arial', 16,'bold'),width=800)
		tk_message1.pack()
		
	# 出题，调取题库数据
	def display_timu(self):
		self.timu = self.table.cell(self.abc,2).value
		self.answerkey1 = self.table.cell(self.abc,3).value
		self.answerkey2 = self.table.cell(self.abc,4).value
		self.answerkey3 = self.table.cell(self.abc,5).value
		self.answerkey4 = self.table.cell(self.abc,6).value
		self.answerkey0 = self.table.cell(self.abc,7).value
		self.answerkey0 = self.answerkey0.rstrip()

	def selection(self):
		you_key = ''
		t_or_f = True
		if self.checkboxes[0].get() == True:
			you_key = you_key + 'A'
		if self.checkboxes[1].get() == True:
			you_key = you_key + 'B'
		if self.checkboxes[2].get() == True:
			you_key = you_key + 'C'
		if self.checkboxes[3].get() == True:
			you_key = you_key + 'D'
		if self.answerkey0 == you_key.rstrip():
			selection1 = "回答正确 " 
		else:
			selection1 = "回答错误！ 正确答案是: " +self.answerkey0		
		self.label.config(text = selection1)
					
	def checkbutton(self):
		self.checkboxes = {}
		for i in range(4):
			num1 = i*50+220
			self.checkboxes[i] = BooleanVar()
			answer_message = Checkbutton(self.face2,text=self.timu_and_keys[i+1],style='B16.TCheckbutton',variable=self.checkboxes[i],width=800)
			answer_message.place(x=500,y=num1)
		btn = Button(self.face2,text=' 确定 ',style='B24.TButton',command=self.selection)
		btn.place(x=350,y=510)
		self.label = Label(self.face2,style='R20.TLabel')
		self.label.place(x=520,y=420)
		
	def comeback(self):
		lab0 = Label(self.face2,text='  ')
		lab0.pack(anchor=E,pady=150)  			
		btn1 = Button(self.face2,text=' 返回 ',style='Q.TButton',command=self.change1)
		btn1.pack(anchor=SE,padx=300)
		lab0 = Label(self.face2,text='  ')
		lab0.pack(pady=150)  					
		
	def change1(self,):
		self.face2.destroy()
		initface(self.master)		

# 判断题界面 face3
class face3():
	def __init__(self,master):
		self.master = master
		self.master.config(bg='blue')
		self.face3 = tk.Frame(self.master,)
		self.face3.pack()
		self.f3_style()
		self.display_tixing()
		self.display_sub()
		self.checkbutton()
		self.comeback()

	def f3_style(self,):
		self.f3 = ttk.Style()
		self.f3.configure('red.TLabel',font=('Arial',24,'bold'),foreground='red')
		self.f3.configure('A20.TLabel', font=('Arial', 20))
		self.f3.configure('R20.TLabel', font=('Arial', 20),foreground='red')
		self.f3.configure('B24.TButton', font=('Arial', 24,'bold'))		
		self.f3.configure('B16.TCheckbutton', font=('Arial', 16))
		self.f3.configure('Q.TButton', font=('Arial', 24,'bold'),foreground='red',background='blue') 	
        		
	def display_tixing(self):
		tixing_title = '2020年质量知识竞赛（判断题）'
		lab0 = Label(self.face3,text='  ',style='A20.TLabel')
		lab0.pack(pady=20)  		
		tixing = Label(self.face3, text=tixing_title,style='red.TLabel',width=1280)
		tixing.pack(padx=390)
		lab00 = Label(self.face3,text='  ',style='A20.TLabel')
		lab00.pack(pady=20)
		
	def display_sub(self):
	# 显示题目
		self.xl = xlrd.open_workbook(r'2020zhiliang.xls')
		self.table = self.xl.sheets()[2]		
		self.qty = self.table.nrows-1 # 获取excel表格总行数
		self.abc = random.randint(1,self.qty)
		self.timu_and_keys = []
		self.display_timu()
		self.timu_and_keys.append(self.timu)
		tk_message1 = tk.Message(self.face3,text=self.timu_and_keys[0],font=('Arial', 16),width=800)
		tk_message1.pack()
		
	# 出题，调取题库数据
	def display_timu(self):
		self.xl = xlrd.open_workbook(r'2020zhiliang.xls')
		self.table = self.xl.sheets()[2]
		self.timu = self.table.cell(self.abc,2).value
		self.answerkey0 = self.table.cell(self.abc,7).value
		self.answerkey0 = self.answerkey0.rstrip()

	# 显示正确答案
	def display_keys(self):
		if self.answerkey0 == 'T':
			keys_text = '答案是：“正确”'
		else:
			keys_text = '答案是：“错误”'
		keys_message = tk.Message(self.face3,text=keys_text,font=('Arial', 24),fg='red',width=500)
		keys_message.place(x=500,y=320)
					
	def checkbutton(self):
		btn = Button(self.face3,text=' 显示 答案 ',style='B24.TButton',command=self.display_keys)
		btn.place(x=350,y=505)
		
	def comeback(self):
		lab0 = Label(self.face3,text='  ')
		lab0.pack(anchor=E,pady=130)  			
		btn1 = Button(self.face3,text=' 返回 ',style='Q.TButton',command=self.change1)
		btn1.pack(anchor=SE,padx=300)
		lab0 = Label(self.face3,text='  ')
		lab0.pack(pady=150)  					
		
	def change1(self,):
		self.face3.destroy()
		initface(self.master)		

# 简答题界面 face4
class face4():
	def __init__(self,master):
		self.master = master
		self.master.config(bg='blue')
		self.face4 = tk.Frame(self.master,)
		self.face4.pack()
		self.f4_style()
		self.display_tixing()
		self.display_sub()
		self.checkbutton()
		self.comeback()

	def f4_style(self,):
		self.f4 = ttk.Style()
		self.f4.configure('red.TLabel',font=('Arial',24,'bold'),foreground='red')
		self.f4.configure('A20.TLabel', font=('Arial', 20))
		self.f4.configure('R20.TLabel', font=('Arial', 20),foreground='red')
		self.f4.configure('B24.TButton', font=('Arial', 24,'bold'))		
		self.f4.configure('B16.TCheckbutton', font=('Arial', 16))
		self.f4.configure('Q.TButton', font=('Arial', 24,'bold'),foreground='red',background='blue') 
        		
	def display_tixing(self):
		tixing_title = '2020年质量知识竞赛（简答题）'
		lab0 = Label(self.face4,text='  ',style='A20.TLabel')
		lab0.pack(pady=20)  		
		tixing = Label(self.face4, text=tixing_title,style='red.TLabel',width=1280)
		tixing.pack(padx=390)
		lab00 = Label(self.face4,text='  ',style='A20.TLabel')
		lab00.pack(pady=20)
		
	def display_sub(self):
    # 显示题目
		self.xl = xlrd.open_workbook(r'2020zhiliang.xls')
		self.table = self.xl.sheets()[3]		
		self.qty = self.table.nrows-1 # 获取excel表格总行数
		self.abc = random.randint(1,self.qty)
		self.timu_and_keys = []
		self.display_timu()
		self.timu_and_keys.append(self.timu)
		tk_message1 = tk.Message(self.face4,text=self.timu_and_keys[0],font=('Arial', 16),width=800)
		tk_message1.pack()
		
    # 出题，调取题库数据
	def display_timu(self):
		self.timu = self.table.cell(self.abc,2).value
		self.answerkey0 = self.table.cell(self.abc,7).value
		self.answerkey0 = self.answerkey0.rstrip()

    # 显示正确答案
	def display_keys(self):
		keys_message = tk.Message(self.face4,text=self.answerkey0,font=('Arial', 16),fg='red',width=800)
		keys_message.place(x=300,y=250)
					
	def checkbutton(self):
		btn = Button(self.face4,text=' 显示 答案 ',style='B24.TButton',command=self.display_keys)
		btn.place(x=350,y=490)
		
	def comeback(self):
		lab0 = Label(self.face4,text='  ')
		lab0.pack(anchor=E,pady=120)  			
		btn1 = Button(self.face4,text=' 返回 ',style='Q.TButton',command=self.change1)
		btn1.pack(anchor=SE,padx=300)
		lab0 = Label(self.face4,text='  ')
		lab0.pack(pady=150)  					
		
	def change1(self,):
		self.face4.destroy()
		initface(self.master)	

if __name__ == '__main__':
    window = tk.Tk()
    basedesk(window)
    window.mainloop()
    
