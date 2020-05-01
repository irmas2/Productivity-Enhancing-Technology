import sys
import pickle

from PyQt5 import QtCore, QtGui, QtWidgets

class Users:
    def __init__(self):
        self.users=dict()

    def add_user(self,username,email,password):
        print("in add user",username,email,password)
        if username not in self.users:
            self.users[username]=[password,email]
        else:
            print("you already have an acct")

    def check_password(self,username,password):
        if username in self.users:
            if password==self.users[username][0]:
                return True
        return False

    def save_to_file(self,filename):
        with open(filename,"wb") as f:
            #print("file is open")
            try:
                pickle.dump(self.users,f)
            except Exception as e:
                print(e)

    def load_from_file(self,filename):
        with open(filename,"rb") as f:
            #print("file is open")
            try:
                self.users=pickle.load(f)
            except Exception as e:
                print(e)
                

class Login_Dialog(QtWidgets.QWidget):
    switch_window=QtCore.pyqtSignal(str)
    def __init__(self,controller):
        QtWidgets.QWidget.__init__(self)
        self.controller=controller
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(556, 530)
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(120, 260, 81, 31))
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(120, 310, 81, 31))
        self.pass_label.setObjectName("pass_label")
        self.uname_lineEdit = QtWidgets.QTextEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(210, 260, 181, 31))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.pass_lineEdit = QtWidgets.QTextEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(210, 310, 181, 31))
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(200, 360, 91, 41))
        self.login_btn.setObjectName("login_btn")
        self.PET = QtWidgets.QLabel(Dialog)
        self.PET.setGeometry(QtCore.QRect(220, 80, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.PET.setFont(font)
        self.PET.setObjectName("PET")
        self.productivity_enhancing_tech = QtWidgets.QLabel(Dialog)
        self.productivity_enhancing_tech.setGeometry(QtCore.QRect(180, 170, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productivity_enhancing_tech.setFont(font)
        self.productivity_enhancing_tech.setObjectName("productivity_enhancing_tech")
        self.login = QtWidgets.QLabel(Dialog)
        self.login.setGeometry(QtCore.QRect(250, 190, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(310, 360, 91, 41))
        self.signup_btn.setObjectName("signup_btn")
        self.signup_btn.clicked.connect(self.signup_clicked)
        self.login_btn.clicked.connect(self.login_clicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME"))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.PET.setText(_translate("Dialog", "PET"))
        self.productivity_enhancing_tech.setText(_translate("Dialog", "PRODUCTIVITY ENHANCING TECHNOLOGY"))
        self.login.setText(_translate("Dialog", "LOGIN"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))

    def signup_clicked(self):
        #print("i am in login signup clicked")
        self.switch_window.emit("create")

    def login_clicked(self):
        #print("i am in login login clicked")
        self.switch_window.emit("prefs")

class Createacct_Dialog(QtWidgets.QWidget):
    switch_window=QtCore.pyqtSignal(str)
    def __init__(self,users):
        QtWidgets.QWidget.__init__(self)
        #print("in init")
        self.users=users
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 559)
        #print("in setup ui")
        self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(240, 230, 181, 31))
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(150, 230, 81, 31))
        self.email_label.setObjectName("email_label")
        self.uname_label = QtWidgets.QLabel(Dialog)
        self.uname_label.setGeometry(QtCore.QRect(150, 180, 81, 31))
        self.uname_label.setObjectName("uname_label")
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(240, 180, 181, 31))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.uname_lineEdit.setText("hello")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(240, 280, 181, 31))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(150, 280, 81, 31))
        self.password_label.setObjectName("password_label")
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(270, 341, 113, 41))
        self.signup_btn.setObjectName("signup_btn")
        #print("before clicked connect")
        self.signup_btn.clicked.connect(self.switch)
        self.PET = QtWidgets.QLabel(Dialog)
        self.PET.setGeometry(QtCore.QRect(250, 0, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.PET.setFont(font)
        self.PET.setObjectName("PET")
        self.productivity_enhancing_tech = QtWidgets.QLabel(Dialog)
        self.productivity_enhancing_tech.setGeometry(QtCore.QRect(200, 80, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productivity_enhancing_tech.setFont(font)
        self.productivity_enhancing_tech.setObjectName("productivity_enhancing_tech")
        self.createacct = QtWidgets.QLabel(Dialog)
        self.createacct.setGeometry(QtCore.QRect(210, 100, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.createacct.setFont(font)
        self.createacct.setObjectName("createacct")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.email_label.setText(_translate("Dialog", "EMAIL "))
        self.uname_label.setText(_translate("Dialog", "USERNAME"))
        self.password_label.setText(_translate("Dialog", "PASSWORD"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))
        self.PET.setText(_translate("Dialog", "PET"))
        self.productivity_enhancing_tech.setText(_translate("Dialog", "PRODUCTIVITY ENHANCING TECHNOLOGY"))
        self.createacct.setText(_translate("Dialog", "CREATE ACCOUNT"))

    def switch(self):
        #print("you clicked me")
        print(self.uname_lineEdit.text())
        #print("past text")
        print(self.email_lineEdit.text())
        #print("past email")
        print(self.password_lineEdit.text())
        #print("past password")
        self.users.add_user(self.uname_lineEdit.text(),self.email_lineEdit.text(),self.password_lineEdit.text())
        #self.users.add_user("fred","email@example.com","pass23")
        self.users.save_to_file("pickle")
        self.switch_window.emit("login")

        
class Preferences_Dialog(QtWidgets.QWidget):
    switch_window=QtCore.pyqtSignal(str)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.preferences = QtWidgets.QLabel(self.centralwidget)
        self.preferences.setGeometry(QtCore.QRect(190, 110, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.preferences.setFont(font)
        self.preferences.setObjectName("preferences")
        self.productivity_enhancing_tech = QtWidgets.QLabel(self.centralwidget)
        self.productivity_enhancing_tech.setGeometry(QtCore.QRect(150, 90, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productivity_enhancing_tech.setFont(font)
        self.productivity_enhancing_tech.setObjectName("productivity_enhancing_tech")
        self.PET = QtWidgets.QLabel(self.centralwidget)
        self.PET.setGeometry(QtCore.QRect(200, 10, 151, 81))
        font = QtGui.QFont()
        #print("first checkpoint in setup ui")
        font.setPointSize(64)
        self.PET.setFont(font)
        self.PET.setObjectName("PET")
        self.chooseapet = QtWidgets.QLabel(self.centralwidget)
        self.chooseapet.setGeometry(QtCore.QRect(210, 170, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chooseapet.setFont(font)
        self.chooseapet.setObjectName("chooseapet")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 181, 121))
        self.label.setStyleSheet("background-image: url(:/newPrefix/PYGKKT.jpg);\n"
"background-image: url(:/newPrefix/PYGKKT happy.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pictures/HappyPython.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 230, 151, 121))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/PYGKKT.jpg);\n"
"background-image: url(:/newPrefix/dog-with-different-emotions happy.jpg);\n"
"background-image: url(:/newPrefix/PYGKKT happy.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Pictures/HappyDog.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(220, 350, 121, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.dogradiobtn = QtWidgets.QRadioButton(self.groupBox)
        self.dogradiobtn.setGeometry(QtCore.QRect(0, 50, 101, 17))
        font = QtGui.QFont()
        #print("second checkpoint in setup ui")
        font.setPointSize(14)
        self.dogradiobtn.setFont(font)
        self.dogradiobtn.setObjectName("dogradiobtn")
        self.pythonradiobtn = QtWidgets.QRadioButton(self.groupBox)
        self.pythonradiobtn.setGeometry(QtCore.QRect(0, 20, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pythonradiobtn.setFont(font)
        self.pythonradiobtn.setObjectName("pythonradiobtn")
        #print("between second and third checkpoint")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(220, 440, 91, 41))
        self.save_btn.setObjectName("save_btn")
        #print("another checkpoint")
        self.save_btn.clicked.connect(self.save_it)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #print("third checkpoint in setup ui")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.preferences.setText(_translate("MainWindow", "PREFERENCES"))
        self.productivity_enhancing_tech.setText(_translate("MainWindow", "PRODUCTIVITY ENHANCING TECHNOLOGY"))
        self.PET.setText(_translate("MainWindow", "PET"))
        self.chooseapet.setText(_translate("MainWindow", "CHOOSE A PET"))
        self.dogradiobtn.setText(_translate("MainWindow", "DOG"))
        self.pythonradiobtn.setText(_translate("MainWindow", "PYTHON"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
    def save_it(self):
        #print("save was pressed")
        if self.pythonradiobtn.isChecked():
            self.switch_window.emit("python")
        else:
            self.switch_window.emit("dog")

class ToDoList(QtWidgets.QWidget):
    switch_window=QtCore.pyqtSignal()
    pythons=["Pictures/AngryPython.jpeg","Pictures/SadPython.jpeg","Pictures/HappyPython.jpeg","Pictures/ThrilledPython.jpeg"]
    dogs=["Pictures/AngryDog.jpg","Pictures/SadDog.jpg","Pictures/HappyDog.jpg","Pictures/ThrilledDog.jpg"]
    def __init__(self,python):
        QtWidgets.QWidget.__init__(self)
        self.python=python
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PET = QtWidgets.QLabel(self.centralwidget)
        self.PET.setGeometry(QtCore.QRect(240, 20, 151, 81))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.PET.setFont(font)
        self.PET.setObjectName("PET")
        self.productivity_enhancing_tech = QtWidgets.QLabel(self.centralwidget)
        self.productivity_enhancing_tech.setGeometry(QtCore.QRect(200, 100, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.productivity_enhancing_tech.setFont(font)
        self.productivity_enhancing_tech.setObjectName("productivity_enhancing_tech")
        self.todolist = QtWidgets.QLabel(self.centralwidget)
        self.todolist.setGeometry(QtCore.QRect(240, 120, 171, 71))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 181, 121))
        self.label.setStyleSheet("background-image: url(:/newPrefix/PYGKKT.jpg);\n"
            "background-image: url(:/newPrefix/PYGKKT happy.jpg);")
        self.label.setText("")
        if self.python:
            self.label.setPixmap(QtGui.QPixmap("Pictures/HappyPython.jpeg"))
        else:
            self.label.setPixmap(QtGui.QPixmap("Pictures/HappyDog.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.todolist.setFont(font)
        self.todolist.setObjectName("todolist")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 190, 331, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 2, 5, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Type To-Do Item")
        self.lineEdit.returnPressed.connect(self.returnPressed)
        self.verticalLayout.addWidget(self.lineEdit)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.setPetEmotion)
        self.verticalLayout.addWidget(self.listWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PET.setText(_translate("MainWindow", "PET"))
        self.productivity_enhancing_tech.setText(_translate("MainWindow", "PRODUCTIVITY ENHANCING TECHNOLOGY"))
        self.todolist.setText(_translate("MainWindow", "TO-DO LIST:"))
        
    def add_todo(self, text):
        item = QtWidgets.QListWidgetItem(text)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.listWidget.addItem(item)

    def returnPressed(self):
        #print("return pressed")
        self.add_todo(self.lineEdit.text())
        self.lineEdit.setText("")
        self.setPetEmotion()

    def getPercentDone(self):
        #print("in getpercentdone")
        numItems=self.listWidget.count()
        numChecked=0
        #print("before loop",numItems)
        for item in range(numItems):
            #print("item=",item)
            if self.listWidget.item(item).checkState()==QtCore.Qt.Checked:
                numChecked+=1
            #print("self.listWidget.item",self.listWidget.item(item))
        return numChecked/numItems
            

    def setPetEmotion(self):
        pctdone=self.getPercentDone()
        #print("percent done",pctdone)
        if self.python:
            #print("its a python")
            if pctdone<=0.25:
                self.label.setPixmap(QtGui.QPixmap(ToDoList.pythons[0]))
            elif 0.25<pctdone<=0.5:
                self.label.setPixmap(QtGui.QPixmap(ToDoList.pythons[1]))
            elif 0.5<pctdone<=0.75:
                self.label.setPixmap(QtGui.QPixmap(ToDoList.pythons[2]))
            elif 0.75<pctdone<=1.0:
                self.label.setPixmap(QtGui.QPixmap(ToDoList.pythons[3]))
        else:
            #print("its a dog")
            if pctdone<=0.25:
                self.label.setPixmap(QtGui.QPixmap(ToDoList.dogs[0]))
            elif 0.25<pctdone<=0.5:
                self.label.setPixmap(QtGui.QPixmap(ToDoList.dogs[1]))
            elif 0.5<pctdone<=0.75:
                self.label.setPixmap(QtGui.QPixmap(ToDoList.dogs[2]))
            elif 0.75<pctdone<=1.0:
                self.label.setPixmap(QtGui.QPixmap(ToDoList.dogs[3]))

        

class Controller:
    def __init__(self):
        self.login_dialog=None
        self.dialog=None
        self.python=None
        self.users=Users()

    def show_login(self):
        #print("in show login")
        self.users.load_from_file("pickle")
        self.login=Login_Dialog(self)
        self.login_dialog=QtWidgets.QDialog()
        self.login.setupUi(self.login_dialog)
        self.login.switch_window.connect(self.show_next)
        self.login_dialog.show()
        if self.dialog:
            self.dialog.close()

    def show_createacct(self):
        #print("in show_createacct")
        self.createacct=Createacct_Dialog(self.users)
        self.dialog=QtWidgets.QDialog()
        #print("before setup ui")
        self.createacct.setupUi(self.dialog)
        self.createacct.switch_window.connect(self.show_next)
        self.dialog.show()
        self.login_dialog.close()

    def show_preferences(self):
        #print("in show preferences")
        self.preferences=Preferences_Dialog()
        #print("before qmainwindow")
        self.prefs_dialog=QtWidgets.QMainWindow()
        #print("before setup ui")
        self.preferences.setupUi(self.prefs_dialog)
        #print("after setup ui")
        self.preferences.switch_window.connect(self.show_next)
        self.prefs_dialog.show()
        self.login_dialog.close()

    def show_todolist(self):
        #print("in show todolist")
        self.todolist=ToDoList(self.python)
        self.todolist_dialog=QtWidgets.QMainWindow()
        self.todolist.setupUi(self.todolist_dialog)
        self.todolist.switch_window.connect(self.show_next)
        self.todolist_dialog.show()
        self.prefs_dialog.close()

    def show_next(self,next):
        #print("in show_next",next)
        if next=="login":
            self.show_login()
        elif next=="create":
            self.show_createacct()
        elif next=="prefs":
            self.show_preferences()
        elif next=="python":
            self.python=True
            self.show_todolist()
        elif next=="dog":
            self.python=False
            self.show_todolist()
        else:
            print("unknown option")

def main():
    app=QtWidgets.QApplication(sys.argv)
    controller=Controller()
    #controller.show_createacct()
    controller.show_login()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

