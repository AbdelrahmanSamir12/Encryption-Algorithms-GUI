# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.ceasar_cipher = QtWidgets.QTextEdit(self.page)
        self.ceasar_cipher.setGeometry(QtCore.QRect(50, 410, 731, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ceasar_cipher.setFont(font)
        self.ceasar_cipher.setObjectName("ceasar_cipher")
        self.ceasar_plain = QtWidgets.QTextEdit(self.page)
        self.ceasar_plain.setGeometry(QtCore.QRect(50, 70, 721, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ceasar_plain.setFont(font)
        self.ceasar_plain.setObjectName("ceasar_plain")
        self.ceaser_key = QtWidgets.QLineEdit(self.page)
        self.ceaser_key.setGeometry(QtCore.QRect(90, 250, 681, 31))
        self.ceaser_key.setObjectName("ceaser_key")
        self.ceaser_sumit = QtWidgets.QPushButton(self.page)
        self.ceaser_sumit.setGeometry(QtCore.QRect(50, 340, 721, 41))
        self.ceaser_sumit.setObjectName("ceaser_sumit")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(50, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(50, 255, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(50, 390, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.enc = QtWidgets.QRadioButton(self.page)
        self.enc.setGeometry(QtCore.QRect(60, 310, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enc.setFont(font)
        self.enc.setObjectName("enc")
        self.dec = QtWidgets.QRadioButton(self.page)
        self.dec.setGeometry(QtCore.QRect(160, 310, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dec.setFont(font)
        self.dec.setObjectName("dec")
        self.label_11 = QtWidgets.QLabel(self.page)
        self.label_11.setGeometry(QtCore.QRect(350, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.mono_key = QtWidgets.QLineEdit(self.page_2)
        self.mono_key.setGeometry(QtCore.QRect(80, 240, 551, 31))
        self.mono_key.setReadOnly(False)
        self.mono_key.setObjectName("mono_key")
        self.mono_submit = QtWidgets.QPushButton(self.page_2)
        self.mono_submit.setGeometry(QtCore.QRect(40, 330, 721, 41))
        self.mono_submit.setObjectName("mono_submit")
        self.enc_2 = QtWidgets.QRadioButton(self.page_2)
        self.enc_2.setGeometry(QtCore.QRect(50, 300, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enc_2.setFont(font)
        self.enc_2.setObjectName("enc_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dec_2 = QtWidgets.QRadioButton(self.page_2)
        self.dec_2.setGeometry(QtCore.QRect(150, 300, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dec_2.setFont(font)
        self.dec_2.setObjectName("dec_2")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(40, 380, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.mono_input = QtWidgets.QTextEdit(self.page_2)
        self.mono_input.setGeometry(QtCore.QRect(40, 60, 721, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mono_input.setFont(font)
        self.mono_input.setObjectName("mono_input")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(40, 245, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.mono_output = QtWidgets.QTextEdit(self.page_2)
        self.mono_output.setGeometry(QtCore.QRect(40, 400, 731, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mono_output.setFont(font)
        self.mono_output.setObjectName("mono_output")
        self.mono_generate_key = QtWidgets.QPushButton(self.page_2)
        self.mono_generate_key.setGeometry(QtCore.QRect(640, 240, 121, 31))
        self.mono_generate_key.setObjectName("mono_generate_key")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(320, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(310, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(30, 380, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_3)
        self.label_14.setGeometry(QtCore.QRect(30, 30, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setGeometry(QtCore.QRect(30, 270, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.enc_3 = QtWidgets.QRadioButton(self.page_3)
        self.enc_3.setGeometry(QtCore.QRect(40, 300, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enc_3.setFont(font)
        self.enc_3.setObjectName("enc_3")
        self.poly_input = QtWidgets.QTextEdit(self.page_3)
        self.poly_input.setGeometry(QtCore.QRect(30, 60, 721, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.poly_input.setFont(font)
        self.poly_input.setObjectName("poly_input")
        self.dec_3 = QtWidgets.QRadioButton(self.page_3)
        self.dec_3.setGeometry(QtCore.QRect(140, 300, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dec_3.setFont(font)
        self.dec_3.setObjectName("dec_3")
        self.poly_generate_key = QtWidgets.QPushButton(self.page_3)
        self.poly_generate_key.setGeometry(QtCore.QRect(630, 265, 121, 31))
        self.poly_generate_key.setObjectName("poly_generate_key")
        self.poly_output = QtWidgets.QTextEdit(self.page_3)
        self.poly_output.setGeometry(QtCore.QRect(30, 400, 731, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.poly_output.setFont(font)
        self.poly_output.setObjectName("poly_output")
        self.poly_key = QtWidgets.QLineEdit(self.page_3)
        self.poly_key.setGeometry(QtCore.QRect(130, 265, 491, 31))
        self.poly_key.setReadOnly(True)
        self.poly_key.setObjectName("poly_key")
        self.poly_submit = QtWidgets.QPushButton(self.page_3)
        self.poly_submit.setGeometry(QtCore.QRect(30, 330, 721, 41))
        self.poly_submit.setObjectName("poly_submit")
        self.poly_keywords = QtWidgets.QLineEdit(self.page_3)
        self.poly_keywords.setGeometry(QtCore.QRect(130, 230, 491, 31))
        self.poly_keywords.setReadOnly(False)
        self.poly_keywords.setObjectName("poly_keywords")
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setGeometry(QtCore.QRect(30, 230, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_17 = QtWidgets.QLabel(self.page_4)
        self.label_17.setGeometry(QtCore.QRect(40, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.play_input = QtWidgets.QTextEdit(self.page_4)
        self.play_input.setGeometry(QtCore.QRect(40, 70, 721, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.play_input.setFont(font)
        self.play_input.setObjectName("play_input")
        self.dec_4 = QtWidgets.QRadioButton(self.page_4)
        self.dec_4.setGeometry(QtCore.QRect(150, 320, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dec_4.setFont(font)
        self.dec_4.setObjectName("dec_4")
        self.play_output = QtWidgets.QTextEdit(self.page_4)
        self.play_output.setGeometry(QtCore.QRect(40, 410, 731, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.play_output.setFont(font)
        self.play_output.setObjectName("play_output")
        self.enc_4 = QtWidgets.QRadioButton(self.page_4)
        self.enc_4.setGeometry(QtCore.QRect(50, 320, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.enc_4.setFont(font)
        self.enc_4.setObjectName("enc_4")
        self.play_keywords = QtWidgets.QLineEdit(self.page_4)
        self.play_keywords.setGeometry(QtCore.QRect(120, 240, 411, 31))
        self.play_keywords.setReadOnly(False)
        self.play_keywords.setObjectName("play_keywords")
        self.label_18 = QtWidgets.QLabel(self.page_4)
        self.label_18.setGeometry(QtCore.QRect(350, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page_4)
        self.label_19.setGeometry(QtCore.QRect(40, 390, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.page_4)
        self.label_21.setGeometry(QtCore.QRect(30, 240, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.play_submit = QtWidgets.QPushButton(self.page_4)
        self.play_submit.setGeometry(QtCore.QRect(40, 350, 721, 41))
        self.play_submit.setObjectName("play_submit")
        self.label_22 = QtWidgets.QLabel(self.page_4)
        self.label_22.setGeometry(QtCore.QRect(550, 250, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.play_matrix = QtWidgets.QTextEdit(self.page_4)
        self.play_matrix.setGeometry(QtCore.QRect(650, 240, 104, 101))
        self.play_matrix.setReadOnly(True)
        self.play_matrix.setObjectName("play_matrix")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_8 = QtWidgets.QLabel(self.page_5)
        self.label_8.setGeometry(QtCore.QRect(210, 10, 411, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.choose_image = QtWidgets.QPushButton(self.page_5)
        self.choose_image.setGeometry(QtCore.QRect(30, 380, 301, 31))
        self.choose_image.setObjectName("choose_image")
        self.save_ecrypted = QtWidgets.QPushButton(self.page_5)
        self.save_ecrypted.setGeometry(QtCore.QRect(30, 550, 301, 31))
        self.save_ecrypted.setObjectName("save_ecrypted")
        self.original_image = QtWidgets.QLabel(self.page_5)
        self.original_image.setGeometry(QtCore.QRect(30, 80, 301, 291))
        self.original_image.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.original_image.setFrameShape(QtWidgets.QFrame.Box)
        self.original_image.setAlignment(QtCore.Qt.AlignCenter)
        self.original_image.setObjectName("original_image")
        self.generate_key = QtWidgets.QPushButton(self.page_5)
        self.generate_key.setGeometry(QtCore.QRect(250, 420, 81, 41))
        self.generate_key.setObjectName("generate_key")
        self.encrypt = QtWidgets.QPushButton(self.page_5)
        self.encrypt.setGeometry(QtCore.QRect(30, 480, 301, 31))
        self.encrypt.setObjectName("encrypt")
        self.label_7 = QtWidgets.QLabel(self.page_5)
        self.label_7.setGeometry(QtCore.QRect(100, 520, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.choose_file = QtWidgets.QPushButton(self.page_5)
        self.choose_file.setGeometry(QtCore.QRect(470, 80, 301, 31))
        self.choose_file.setObjectName("choose_file")
        self.label_20 = QtWidgets.QLabel(self.page_5)
        self.label_20.setGeometry(QtCore.QRect(480, 150, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.decrypt = QtWidgets.QPushButton(self.page_5)
        self.decrypt.setGeometry(QtCore.QRect(470, 190, 301, 31))
        self.decrypt.setObjectName("decrypt")
        self.result_image = QtWidgets.QLabel(self.page_5)
        self.result_image.setGeometry(QtCore.QRect(470, 240, 301, 291))
        self.result_image.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_image.setFrameShape(QtWidgets.QFrame.Box)
        self.result_image.setAlignment(QtCore.Qt.AlignCenter)
        self.result_image.setObjectName("result_image")
        self.save_decrepted = QtWidgets.QPushButton(self.page_5)
        self.save_decrepted.setGeometry(QtCore.QRect(470, 550, 301, 31))
        self.save_decrepted.setObjectName("save_decrepted")
        self.label_24 = QtWidgets.QLabel(self.page_5)
        self.label_24.setGeometry(QtCore.QRect(530, 220, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.page_5)
        self.label_25.setGeometry(QtCore.QRect(30, 50, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.page_5)
        self.label_26.setGeometry(QtCore.QRect(470, 50, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.key_display = QtWidgets.QPlainTextEdit(self.page_5)
        self.key_display.setGeometry(QtCore.QRect(30, 420, 211, 41))
        self.key_display.setObjectName("key_display")
        self.key2 = QtWidgets.QPlainTextEdit(self.page_5)
        self.key2.setGeometry(QtCore.QRect(540, 150, 231, 31))
        self.key2.setObjectName("key2")
        self.label_6 = QtWidgets.QLabel(self.page_5)
        self.label_6.setGeometry(QtCore.QRect(470, 120, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 1, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.home_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.dashborad_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.dashborad_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.dashborad_btn_2.setCheckable(True)
        self.dashborad_btn_2.setAutoExclusive(True)
        self.dashborad_btn_2.setObjectName("dashborad_btn_2")
        self.verticalLayout_2.addWidget(self.dashborad_btn_2)
        self.orders_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.orders_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.orders_btn_2.setCheckable(True)
        self.orders_btn_2.setAutoExclusive(True)
        self.orders_btn_2.setObjectName("orders_btn_2")
        self.verticalLayout_2.addWidget(self.orders_btn_2)
        self.products_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.products_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.products_btn_2.setCheckable(True)
        self.products_btn_2.setAutoExclusive(True)
        self.products_btn_2.setObjectName("products_btn_2")
        self.verticalLayout_2.addWidget(self.products_btn_2)
        self.customers_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.customers_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.customers_btn_2.setCheckable(True)
        self.customers_btn_2.setAutoExclusive(True)
        self.customers_btn_2.setObjectName("customers_btn_2")
        self.verticalLayout_2.addWidget(self.customers_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_2.setIcon(icon)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ceaser_sumit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Input Text"))
        self.label_2.setText(_translate("MainWindow", "Shift"))
        self.label_3.setText(_translate("MainWindow", "Output Text"))
        self.enc.setText(_translate("MainWindow", "Encrypt"))
        self.dec.setText(_translate("MainWindow", "Decrypt"))
        self.label_11.setText(_translate("MainWindow", "Ceasar Chiper"))
        self.mono_submit.setText(_translate("MainWindow", "Submit"))
        self.enc_2.setText(_translate("MainWindow", "Encrypt"))
        self.label_4.setText(_translate("MainWindow", "Input Text"))
        self.dec_2.setText(_translate("MainWindow", "Decrypt"))
        self.label_9.setText(_translate("MainWindow", "Output Text"))
        self.label_10.setText(_translate("MainWindow", "Key"))
        self.mono_generate_key.setText(_translate("MainWindow", "Generate Key"))
        self.label_5.setText(_translate("MainWindow", "Monoalphabetic cipher"))
        self.label_12.setText(_translate("MainWindow", "Polyalphabetic cipher"))
        self.label_13.setText(_translate("MainWindow", "Output Text"))
        self.label_14.setText(_translate("MainWindow", "Input Text"))
        self.label_15.setText(_translate("MainWindow", "Key"))
        self.enc_3.setText(_translate("MainWindow", "Encrypt"))
        self.dec_3.setText(_translate("MainWindow", "Decrypt"))
        self.poly_generate_key.setText(_translate("MainWindow", "Generate Key"))
        self.poly_submit.setText(_translate("MainWindow", "Submit"))
        self.label_16.setText(_translate("MainWindow", " key words"))
        self.label_17.setText(_translate("MainWindow", "Input Text"))
        self.dec_4.setText(_translate("MainWindow", "Decrypt"))
        self.enc_4.setText(_translate("MainWindow", "Encrypt"))
        self.label_18.setText(_translate("MainWindow", "PlayFair cipher"))
        self.label_19.setText(_translate("MainWindow", "Output Text"))
        self.label_21.setText(_translate("MainWindow", " key words"))
        self.play_submit.setText(_translate("MainWindow", "Submit"))
        self.label_22.setText(_translate("MainWindow", " Key Matrix"))
        self.label_8.setText(_translate("MainWindow", "Image Encryption using AES"))
        self.choose_image.setText(_translate("MainWindow", "Choose Image"))
        self.save_ecrypted.setText(_translate("MainWindow", "Save File"))
        self.original_image.setText(_translate("MainWindow", "ChooseImage"))
        self.generate_key.setText(_translate("MainWindow", "Generate Key"))
        self.encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.label_7.setText(_translate("MainWindow", "Image Encrypted Successfully!"))
        self.choose_file.setText(_translate("MainWindow", "Choose Increpted Image"))
        self.label_20.setText(_translate("MainWindow", "Key"))
        self.decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.result_image.setText(_translate("MainWindow", "ChooseImage"))
        self.save_decrepted.setText(_translate("MainWindow", "Save Image"))
        self.label_24.setText(_translate("MainWindow", "Image Decrypted Successfully!"))
        self.label_25.setText(_translate("MainWindow", "Encrypt"))
        self.label_26.setText(_translate("MainWindow", "Decrypt"))
        self.logo_label_3.setText(_translate("MainWindow", "Sidebar"))
        self.home_btn_2.setText(_translate("MainWindow", "Ceasar Chiper"))
        self.dashborad_btn_2.setText(_translate("MainWindow", "Monoalphabetic cipher"))
        self.orders_btn_2.setText(_translate("MainWindow", "Polyalphabetic cipher"))
        self.products_btn_2.setText(_translate("MainWindow", "Playfair cipher"))
        self.customers_btn_2.setText(_translate("MainWindow", "Image cipher"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))

