import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton 
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream 
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image

from sidebar_ui import Ui_MainWindow
import Algo as algo
from PyQt5.QtGui import QTextCursor
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Encryption Algorithms")
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        self.ui.label_7.setHidden(True)
        self.ui.label_24.setHidden(True)
        self.ui.save_ecrypted.setEnabled(False)
        self.ui.encrypt.setEnabled(False)
        self.ui.decrypt.setEnabled(False)
        self.ui.save_decrepted.setEnabled(False)
        self.ui.poly_submit.setEnabled(False)
        self.ui.mono_submit.setEnabled(False)
        




        ## connecting buttons
        self.ui.ceaser_sumit.clicked.connect(self.on_ceaser_sumit_toggled)

        self.ui.mono_generate_key.clicked.connect(self.mono_generate_key)
        self.ui.mono_submit.clicked.connect(self.on_monoalphabetic_submit_toggled)

        self.ui.poly_generate_key.clicked.connect(self.on_polyalphabetic_generate_key_clicked)
        self.ui.poly_submit.clicked.connect(self.on_polyalphabetic_submit_toggled)

        #self.ui.play_submit.clicked.connect(self.on_playfair_generate_key_clicked)
        self.ui.play_submit.clicked.connect(self.on_playfair_submit_toggled)

        self.ui.generate_key.clicked.connect(self.generate_aes_key)
        self.ui.choose_image.clicked.connect(self.choose_image)
        self.ui.encrypt.clicked.connect(self.encrypt_image)
        self.ui.save_ecrypted.clicked.connect(self.save_ecrypted_image)
        self.ui.choose_file.clicked.connect(self.choose_encrypted_image)
        self.ui.decrypt.clicked.connect(self.decrypt_image)
        self.ui.save_decrepted.clicked.connect(self.save_decrypted_image)

    
    

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)


    #ceaser cipher
    def on_ceaser_sumit_toggled(self):
        input = self.ui.ceasar_plain.toPlainText()
        shift = self.ui.ceaser_key.text()
        try:
            shift = int(shift)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning") 
            msg.setText("Please enter int value for the shift value")
            msg.setStandardButtons(QMessageBox.Ok) 
            msg.exec_()
            msg.show()
            return
        

        if (self.ui.enc.isChecked()):
            encrypted = algo.caesar_cipher(input, int(shift))
            self.ui.ceasar_cipher.setPlainText(encrypted)
        elif (self.ui.dec.isChecked()):
            decrypted = algo.caesar_cipher(input, -int(shift))
            self.ui.ceasar_cipher.setPlainText(decrypted)

    #monoalphabetic cipher
    def mono_generate_key(self):
        cipher_key = algo.generate_monoalphabetic_key()
        self.ui.mono_key.setText(cipher_key)
        self.ui.mono_submit.setEnabled(True)

    def on_monoalphabetic_submit_toggled(self):
        cipher_key = self.ui.mono_key.text()

        if (self.ui.enc_2.isChecked()):
            input = self.ui.mono_input.toPlainText()
            encrypted = algo.monoalphabetic_encrypt(input, cipher_key)
            self.ui.mono_output.setPlainText(encrypted)

        elif (self.ui.dec_2.isChecked()):
            input = self.ui.mono_input.toPlainText()
            decrypted = algo.monoalphabetic_decrypt(input, cipher_key)
            self.ui.mono_output.setPlainText(decrypted)

    #polyalphabetic cipher

    def on_polyalphabetic_generate_key_clicked(self):
        self.ui.poly_submit.setEnabled(True)
        keyword = self.ui.poly_keywords.text()
        cipher_key = algo.generate_vigenere_key(keyword, len(self.ui.poly_input.toPlainText()))
        self.ui.poly_key.setText(cipher_key)

    def on_polyalphabetic_submit_toggled(self):
        keyword = self.ui.poly_keywords.text()

        if (self.ui.enc_3.isChecked()):
            input = self.ui.poly_input.toPlainText()
            encrypted = algo.polyalphabetic_encrypt(input, keyword)
            self.ui.poly_output.setPlainText(encrypted)

        elif (self.ui.dec_3.isChecked()):
            input = self.ui.poly_input.toPlainText()
            decrypted = algo.polyalphabetic_decrypt(input, keyword)
            self.ui.poly_output.setPlainText(decrypted)

    #playfair cipher
    def on_playfair_generate_key_clicked(self):
        keyword = self.ui.play_keywords.text()
        keyword = keyword.upper()
        cipher_key = algo.generate_playfair_matrix(keyword)
        self.show_playfair_matrix(cipher_key)

    def show_playfair_matrix(self, key):
        self.ui.play_matrix.clear()
        cursor = self.ui.play_matrix.textCursor()
        cursor.insertTable(5, 5)
        for i in range(5):
            for j in range(5):
                cursor.insertText(" " + key[i][j]+ " ")
                cursor.movePosition(QTextCursor.NextCell)

            
        
    
    def on_playfair_submit_toggled(self):
        self.on_playfair_generate_key_clicked()
        keyword = self.ui.play_keywords.text()
        keyword = keyword.upper()
        if (self.ui.enc_4.isChecked()):
            input = self.ui.play_input.toPlainText()
            input = input.upper()
            input = input.replace(" ","")
            encrypted = algo.playfair_encrypt(input, keyword)
            self.ui.play_output.setPlainText(encrypted)

        elif (self.ui.dec_4.isChecked()):
            input = self.ui.play_input.toPlainText()
            input = input.upper()
            input = input.replace(" ","")
            decrypted = algo.playfair_decrypt(input, keyword)
            self.ui.play_output.setPlainText(decrypted)


    #image cipher
    def generate_aes_key(self):
        self.key = algo.generate_aes_key()
        self.ui.key_display.setPlainText(self.key.hex())

    def choose_image(self):
        fname = QFileDialog.getOpenFileName(QWidget(), 'Open file', './')
        if fname[0]:
            self.image_path = fname[0]
            pixmap = QPixmap(self.image_path)    
            self.ui.original_image.setPixmap(pixmap)
            self.ui.label_7.setScaledContents(True)
            self.ui.encrypt.setEnabled(True)



        
        

    def encrypt_image(self):
        try:
            self.ct, self.iv = algo.encrypt_image(self.image_path, self.key)
            self.ui.label_7.setHidden(False)
            self.ui.save_ecrypted.setEnabled(True)

        except:
            msg = QMessageBox()
            msg.setText("Error : Please generate key and choose image correctly")
            return

    def save_ecrypted_image(self):
        # Get the file name and location to save the file using a file dialog
        file_name, _ = QFileDialog.getSaveFileName(None, 'Save Image', 'icreptedimage.enc','./')
        # If the user selects a file, save the QPixmap object as an image file
        if file_name:
            with open(file_name, 'wb') as f:
                f.write(self.iv)
                f.write(self.ct)


    def choose_encrypted_image(self):
        fname = QFileDialog.getOpenFileName(QWidget(), 'Open file', './')
        if fname[0]:
            self.enc_path = fname[0]
            self.ui.label_6.setText(self.enc_path)
            self.ui.decrypt.setEnabled(True)
            self.ui.save_decrepted.setEnabled(True)



    def decrypt_image(self):
        key = self.ui.key2.toPlainText()
        self.key = bytes.fromhex(key)
        try:
            self.pt = algo.decrypt_image(self.enc_path, self.key)
            self.ui.label_24.setHidden(False)
            with open('temp.jpg', 'wb') as f:
                f.write(self.pt)
            pixmap = QPixmap('temp.jpg')
            self.ui.result_image.setPixmap(pixmap)
            self.ui.label_24.setScaledContents(True)


        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning") 
            msg.setText("Please choose image and generate Key correctly")
            msg.setStandardButtons(QMessageBox.Ok) 
            msg.exec_()
            msg.show()
            return


    def save_decrypted_image(self):
        file_name, _ = QFileDialog.getSaveFileName(None, 'Save Image', 'decreptedimage.jpg','./')
        if file_name:
            with open(file_name, 'wb') as f:
                f.write(self.pt)

    
            
    



    


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # loading style file
    style_file = QFile("style_orange.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())


    window = MainWindow()
    window.show()

    sys.exit(app.exec())



