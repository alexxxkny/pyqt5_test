# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keypad_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Keypad(object):
    def setupUi(self, Keypad):
        Keypad.setObjectName("Keypad")
        Keypad.resize(362, 555)
        Keypad.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Keypad.setPalette(palette)
        self.verticalLayout = QtWidgets.QVBoxLayout(Keypad)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Keypad)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.title.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.digit_frame = QtWidgets.QFrame(Keypad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.digit_frame.sizePolicy().hasHeightForWidth())
        self.digit_frame.setSizePolicy(sizePolicy)
        self.digit_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.digit_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.digit_frame.setObjectName("digit_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.digit_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.digit_1 = QtWidgets.QLineEdit(self.digit_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit_1.sizePolicy().hasHeightForWidth())
        self.digit_1.setSizePolicy(sizePolicy)
        self.digit_1.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.digit_1.setFont(font)
        self.digit_1.setMaxLength(1)
        self.digit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.digit_1.setObjectName("digit_1")
        self.horizontalLayout.addWidget(self.digit_1)
        self.digit_2 = QtWidgets.QLineEdit(self.digit_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit_2.sizePolicy().hasHeightForWidth())
        self.digit_2.setSizePolicy(sizePolicy)
        self.digit_2.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.digit_2.setFont(font)
        self.digit_2.setMaxLength(1)
        self.digit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.digit_2.setObjectName("digit_2")
        self.horizontalLayout.addWidget(self.digit_2)
        self.digit_3 = QtWidgets.QLineEdit(self.digit_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit_3.sizePolicy().hasHeightForWidth())
        self.digit_3.setSizePolicy(sizePolicy)
        self.digit_3.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.digit_3.setFont(font)
        self.digit_3.setMaxLength(1)
        self.digit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.digit_3.setObjectName("digit_3")
        self.horizontalLayout.addWidget(self.digit_3)
        self.digit_4 = QtWidgets.QLineEdit(self.digit_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.digit_4.sizePolicy().hasHeightForWidth())
        self.digit_4.setSizePolicy(sizePolicy)
        self.digit_4.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.digit_4.setFont(font)
        self.digit_4.setMaxLength(1)
        self.digit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.digit_4.setObjectName("digit_4")
        self.horizontalLayout.addWidget(self.digit_4)
        self.verticalLayout.addWidget(self.digit_frame)
        self.btn_frame = QtWidgets.QFrame(Keypad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.btn_frame.sizePolicy().hasHeightForWidth())
        self.btn_frame.setSizePolicy(sizePolicy)
        self.btn_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.btn_frame.setLineWidth(6)
        self.btn_frame.setObjectName("btn_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.btn_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_7 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 2, 0, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 2, 1, 1, 1)
        self.btn_star = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_star.sizePolicy().hasHeightForWidth())
        self.btn_star.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_star.setFont(font)
        self.btn_star.setObjectName("btn_star")
        self.gridLayout.addWidget(self.btn_star, 3, 0, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 0, 2, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)
        self.btn_hash = QtWidgets.QPushButton(self.btn_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_hash.sizePolicy().hasHeightForWidth())
        self.btn_hash.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_hash.setFont(font)
        self.btn_hash.setObjectName("btn_hash")
        self.gridLayout.addWidget(self.btn_hash, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.btn_frame)

        self.retranslateUi(Keypad)
        self.btn_star.clicked.connect(self.digit_1.clear)
        self.btn_star.clicked.connect(self.digit_2.clear)
        self.btn_star.clicked.connect(self.digit_3.clear)
        self.btn_star.clicked.connect(self.digit_4.clear)
        QtCore.QMetaObject.connectSlotsByName(Keypad)

    def retranslateUi(self, Keypad):
        _translate = QtCore.QCoreApplication.translate
        Keypad.setWindowTitle(_translate("Keypad", "Keypad"))
        self.title.setText(_translate("Keypad", "Enter a passcode"))
        self.btn_7.setText(_translate("Keypad", "7"))
        self.btn_9.setText(_translate("Keypad", "9"))
        self.btn_8.setText(_translate("Keypad", "8"))
        self.btn_star.setText(_translate("Keypad", "*"))
        self.btn_0.setText(_translate("Keypad", "0"))
        self.btn_5.setText(_translate("Keypad", "5"))
        self.btn_6.setText(_translate("Keypad", "6"))
        self.btn_2.setText(_translate("Keypad", "2"))
        self.btn_4.setText(_translate("Keypad", "4"))
        self.btn_3.setText(_translate("Keypad", "3"))
        self.btn_1.setText(_translate("Keypad", "1"))
        self.btn_hash.setText(_translate("Keypad", "#"))
