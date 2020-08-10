# display window with cipher program on it


# prompt user for input of text


# convert text into cipher and display cipher key


# cipher key/decryption options


# decrypt button to decrypt messages
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import sys

from cipher import gettranslatedmessage
from function import rotate


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.resize(550, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # adding pushbutton (Decrypt)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 120, 100, 50))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 221, 20))

        # adding pushbutton2 (Encrypt)
        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(180, 120, 100, 50))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 221, 20))

        # display cipher messages and key
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 540, 80))

        # Keeping the text of label empty initially.
        self.label.setText("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caesar Cipher"))
        # Decrypt
        self.pushButton.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton.clicked.connect(self.takeInputs)
        # Encrypt
        self.pushbutton.setText(_translate("MainWindow", "Encrypt"))
        self.pushbutton.clicked.connect(self.takeinputs)

    def takeinputs(self):
        message, done1 = QtWidgets.QInputDialog.getText(
            self, 'Message', 'Enter your Message:')

        key, done2 = QtWidgets.QInputDialog.getInt(
            self, 'key', 'Enter your Key (1-25:)')

        if done1 and done2:
            # Showing confirmation message along
            # with information provided by user.
            output = gettranslatedmessage(['e'], message, key)
            self.label.setText('Here is your cipher and key: \nOriginal Message: '
                               + str(message)
                               + '\nKey: ' + str(key)
                               + '\nCiphered Message: ' + str(output))

            # Show the pushbutton after inputs provided by the user.
            self.pushbutton.show()
            self.pushButton.show()

    def takeInputs(self):
        cipher, done3 = QtWidgets.QInputDialog.getText(
            self, 'Cipher', 'Enter your Cipher:')

        keyd, done4 = QtWidgets.QInputDialog.getInt(
            self, 'keyd', 'Enter your known Key:')

        if done3 and done4:
            # Showing confirmation message along
            # with information provided by user.
            output = gettranslatedmessage(['d'], cipher, keyd)
            self.label.setText('Here is your cipher and key: \nCipher: '
                               + str(cipher)
                               + '\nKey: ' + str(keyd)
                               + '\nDecrypted Message: ' + str(output))

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
