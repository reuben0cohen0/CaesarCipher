# display window with cipher program on it


# prompt user for input of text


# convert text into cipher and display cipher key


# cipher key/decryption options


# decrypt button to decrypt messages
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QFont
import sys

from PyQt5.QtWidgets import QTextEdit, QSizePolicy

from cipher import gettranslatedmessage


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, Mainwindow):
        Mainwindow.resize(550, 300)
        self.centralwidget = QtWidgets.QWidget(Mainwindow)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)

        # adding pushbutton (Decrypt)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # geometry (left, top, width, height)
        self.pushButton.setGeometry(QtCore.QRect(280, 240, 100, 50))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 221, 20))

        # adding pushbutton2 (Encrypt)
        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(180, 240, 100, 50))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 221, 20))

        # display cipher messages and key
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 500, 250))

        # Keeping main GUI screen initially empty
        self.label.setText("")

        Mainwindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("MainWindow", "Caesar Cipher"))
        Mainwindow.setWindowIcon(QIcon('ciphericon.png'))
        self.setWindowIcon(QIcon('ciphericon.png'))
        # Decrypt
        self.pushButton.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton.clicked.connect(self.takeInputs)
        self.pushButton.setFont(QFont('System', 10))
        # Encrypt
        self.pushbutton.setText(_translate("MainWindow", "Encrypt"))
        self.pushbutton.clicked.connect(self.takeinputs)
        self.pushbutton.setFont(QFont('System', 10))

    def takeinputs(self):
        MAX_KEY_SIZE = 25
        message, done1 = QtWidgets.QInputDialog.getText(
            self, 'Message', 'Enter your Message:')

        key, done2 = QtWidgets.QInputDialog.getInt(
            self, 'Key', 'Enter your Key (1-%s:) ' % MAX_KEY_SIZE, 1, 1, 25)

        if done1 and done2:
            # done1 and done2 = 'message and key'
            # results from done1 and done2, fetch output from cipher.py file
            output = gettranslatedmessage(['e'], message, key)
            self.label.setText('Your cipher and key: \nOriginal Message: ' +
                               str(message) +
                               '\n\nKey: ' + str(key) +
                               '\n\nCiphered Message: ' + str(output))
            self.label.setWordWrap(True)
            self.text = QTextEdit(self)
            self.text.setMinimumSize(50, 50)
            self.text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Show the pushbutton after inputs provided by the user.
            self.pushbutton.show()
            self.pushButton.show()

    def takeInputs(self):
        MAX_KEY_SIZE = 25
        cipher, done3 = QtWidgets.QInputDialog.getText(
            self, 'Cipher', 'Enter your Cipher:')

        keyd, done4 = QtWidgets.QInputDialog.getInt(
            self, 'Key', 'Enter your known Key: (1-%s:) ' % MAX_KEY_SIZE, 1, 1, 25)

        if done3 and done4:
            # done3 and done4 = 'cipher and key'
            # when done3 and done4, fetch decrypted output from cipher.py file
            output = gettranslatedmessage(['d'], cipher, keyd)
            self.label.setText('Here is your cipher and key: \nCipher: ' +
                               str(cipher) +
                               '\n\nKey: ' + str(keyd) +
                               '\n\nDecrypted Message: ' + str(output))
            self.label.setWordWrap(True)
            self.text = QTextEdit(self)
            self.text.setMinimumSize(50, 50)
            self.text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Show the pushbutton after inputs provided by the user.
            self.pushbutton.show()
            self.pushButton.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
