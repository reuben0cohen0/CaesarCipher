# display window with cipher program on it


# prompt user for input of text


# convert text into cipher and display cipher key


# cipher key/decryption options


# decrypt button to decrypt messages
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from function import rotate


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.resize(422, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # adding pushbutton (Decrypt)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 140, 93, 30))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 221, 20))

        # adding pushbutton2 (Encrypt)
        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(100, 140, 93, 30))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 90, 221, 20))

        # For displaying confirmation message along with user's info.
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))

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
            self, 'key', 'Enter your Key (1-25:')

        if done1 and done2:
            # Showing confirmation message along
            # with information provided by user.
            self.label.setText('Information stored Successfully\nMessage: '
                               + str(message)
                               + '\nkey: ' + str(key))

            # Hide the pushbutton after inputs provided by the user.
            self.pushButton.hide()

    def takeInputs(self):
        cipher, done3 = QtWidgets.QInputDialog.getText(
            self, 'Cipher', 'Enter your Cipher:')

        keyd, done4 = QtWidgets.QInputDialog.getInt(
            self, 'keyd', 'Enter your known Key:')

        if done3 and done4:
            # Showing confirmation message along
            # with information provided by user.
            self.label.setText('\nCipher: ' + str(cipher)
                               + '\nkeyd: ' + str(keyd))

            # Hide the pushbutton after inputs provided by the user.
            self.pushButton.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
