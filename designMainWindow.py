# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)
import graph_resources_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1187, 335)
        mainWindow.setMinimumSize(QSize(1187, 335))
        mainWindow.setMaximumSize(QSize(1445, 680))
        mainWindow.setCursor(QCursor(Qt.ArrowCursor))
        mainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/img/C:/Users/mx/Downloads/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"QWidget{\n"
"background-color: rgb(12, 14, 35);\n"
"color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"")
        mainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        mainWindow.setDocumentMode(False)
        mainWindow.setTabShape(QTabWidget.Rounded)
        self.centralWidget = QWidget(mainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settingsLayout = QGridLayout()
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.physicalFrame = QFrame(self.centralWidget)
        self.physicalFrame.setObjectName(u"physicalFrame")
        self.physicalFrame.setFrameShape(QFrame.Box)
        self.verticalLayout = QVBoxLayout(self.physicalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sizeLabel = QLabel(self.physicalFrame)
        self.sizeLabel.setObjectName(u"sizeLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeLabel.sizePolicy().hasHeightForWidth())
        self.sizeLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(True)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setMouseTracking(False)
        self.sizeLabel.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.sizeLabel.setLayoutDirection(Qt.LeftToRight)
        self.sizeLabel.setAutoFillBackground(False)
        self.sizeLabel.setStyleSheet(u"")
        self.sizeLabel.setFrameShape(QFrame.Box)
        self.sizeLabel.setFrameShadow(QFrame.Plain)
        self.sizeLabel.setLineWidth(1)
        self.sizeLabel.setScaledContents(False)
        self.sizeLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.sizeLabel)

        self.sizeCheckBox = QCheckBox(self.physicalFrame)
        self.sizeCheckBox.setObjectName(u"sizeCheckBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sizeCheckBox.sizePolicy().hasHeightForWidth())
        self.sizeCheckBox.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.sizeCheckBox.setFont(font1)
        self.sizeCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.sizeCheckBox.setTabletTracking(False)
        self.sizeCheckBox.setAutoFillBackground(False)
        self.sizeCheckBox.setStyleSheet(u"\n"
"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
"\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }")
        self.sizeCheckBox.setTristate(False)

        self.verticalLayout.addWidget(self.sizeCheckBox)

        self.upsCheckBox = QCheckBox(self.physicalFrame)
        self.upsCheckBox.setObjectName(u"upsCheckBox")
        sizePolicy1.setHeightForWidth(self.upsCheckBox.sizePolicy().hasHeightForWidth())
        self.upsCheckBox.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setKerning(True)
        self.upsCheckBox.setFont(font2)
        self.upsCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.upsCheckBox.setTabletTracking(False)
        self.upsCheckBox.setAutoFillBackground(False)
        self.upsCheckBox.setStyleSheet(u"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }")
        self.upsCheckBox.setTristate(False)

        self.verticalLayout.addWidget(self.upsCheckBox)

        self.peripheralCheckBox = QCheckBox(self.physicalFrame)
        self.peripheralCheckBox.setObjectName(u"peripheralCheckBox")
        sizePolicy1.setHeightForWidth(self.peripheralCheckBox.sizePolicy().hasHeightForWidth())
        self.peripheralCheckBox.setSizePolicy(sizePolicy1)
        self.peripheralCheckBox.setFont(font1)
        self.peripheralCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.peripheralCheckBox.setTabletTracking(False)
        self.peripheralCheckBox.setAutoFillBackground(False)
        self.peripheralCheckBox.setStyleSheet(u"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }")
        self.peripheralCheckBox.setTristate(False)

        self.verticalLayout.addWidget(self.peripheralCheckBox)


        self.settingsLayout.addWidget(self.physicalFrame, 0, 0, 1, 1)

        self.cpuFrame = QFrame(self.centralWidget)
        self.cpuFrame.setObjectName(u"cpuFrame")
        self.cpuFrame.setFrameShape(QFrame.Box)
        self.verticalLayout_3 = QVBoxLayout(self.cpuFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cpuLabel = QLabel(self.cpuFrame)
        self.cpuLabel.setObjectName(u"cpuLabel")
        sizePolicy.setHeightForWidth(self.cpuLabel.sizePolicy().hasHeightForWidth())
        self.cpuLabel.setSizePolicy(sizePolicy)
        self.cpuLabel.setFont(font)
        self.cpuLabel.setMouseTracking(False)
        self.cpuLabel.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.cpuLabel.setLayoutDirection(Qt.LeftToRight)
        self.cpuLabel.setAutoFillBackground(False)
        self.cpuLabel.setFrameShape(QFrame.Box)
        self.cpuLabel.setFrameShadow(QFrame.Plain)
        self.cpuLabel.setLineWidth(1)
        self.cpuLabel.setScaledContents(False)
        self.cpuLabel.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.cpuLabel)

        self.multithreadRadioButton = QRadioButton(self.cpuFrame)
        self.multithreadRadioButton.setObjectName(u"multithreadRadioButton")
        sizePolicy1.setHeightForWidth(self.multithreadRadioButton.sizePolicy().hasHeightForWidth())
        self.multithreadRadioButton.setSizePolicy(sizePolicy1)
        self.multithreadRadioButton.setFont(font1)
        self.multithreadRadioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.multithreadRadioButton.setAutoFillBackground(False)
        self.multithreadRadioButton.setStyleSheet(u"QRadioButton:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QRadioButton:checked {\n"
"                color: yellow;\n"
"            }\n"
"")
        self.multithreadRadioButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.multithreadRadioButton)

        self.coreRadioButton = QRadioButton(self.cpuFrame)
        self.coreRadioButton.setObjectName(u"coreRadioButton")
        sizePolicy1.setHeightForWidth(self.coreRadioButton.sizePolicy().hasHeightForWidth())
        self.coreRadioButton.setSizePolicy(sizePolicy1)
        self.coreRadioButton.setFont(font1)
        self.coreRadioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.coreRadioButton.setAutoFillBackground(False)
        self.coreRadioButton.setStyleSheet(u"QRadioButton:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QRadioButton:checked {\n"
"                color: yellow;\n"
"            }")

        self.verticalLayout_3.addWidget(self.coreRadioButton)

        self.companyComboBox = QComboBox(self.cpuFrame)
        self.companyComboBox.addItem("")
        self.companyComboBox.addItem("")
        self.companyComboBox.addItem("")
        self.companyComboBox.setObjectName(u"companyComboBox")
        sizePolicy1.setHeightForWidth(self.companyComboBox.sizePolicy().hasHeightForWidth())
        self.companyComboBox.setSizePolicy(sizePolicy1)
        self.companyComboBox.setFont(font1)
        self.companyComboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.companyComboBox.setAutoFillBackground(False)
        self.companyComboBox.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(12, 14, 35);}\n"
"\n"
"QComboBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
"\n"
"")
        self.companyComboBox.setFrame(True)

        self.verticalLayout_3.addWidget(self.companyComboBox)


        self.settingsLayout.addWidget(self.cpuFrame, 0, 1, 1, 1)

        self.graphicsFrame = QFrame(self.centralWidget)
        self.graphicsFrame.setObjectName(u"graphicsFrame")
        self.graphicsFrame.setFrameShape(QFrame.Box)
        self.verticalLayout_4 = QVBoxLayout(self.graphicsFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.graphicsLabel = QLabel(self.graphicsFrame)
        self.graphicsLabel.setObjectName(u"graphicsLabel")
        sizePolicy.setHeightForWidth(self.graphicsLabel.sizePolicy().hasHeightForWidth())
        self.graphicsLabel.setSizePolicy(sizePolicy)
        self.graphicsLabel.setFont(font)
        self.graphicsLabel.setMouseTracking(False)
        self.graphicsLabel.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.graphicsLabel.setLayoutDirection(Qt.LeftToRight)
        self.graphicsLabel.setAutoFillBackground(False)
        self.graphicsLabel.setFrameShape(QFrame.Box)
        self.graphicsLabel.setFrameShadow(QFrame.Plain)
        self.graphicsLabel.setLineWidth(1)
        self.graphicsLabel.setScaledContents(False)
        self.graphicsLabel.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.graphicsLabel)

        self.graphicsComboBox = QComboBox(self.graphicsFrame)
        self.graphicsComboBox.addItem("")
        self.graphicsComboBox.addItem("")
        self.graphicsComboBox.addItem("")
        self.graphicsComboBox.setObjectName(u"graphicsComboBox")
        sizePolicy1.setHeightForWidth(self.graphicsComboBox.sizePolicy().hasHeightForWidth())
        self.graphicsComboBox.setSizePolicy(sizePolicy1)
        self.graphicsComboBox.setFont(font1)
        self.graphicsComboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.graphicsComboBox.setAutoFillBackground(False)
        self.graphicsComboBox.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(12, 14, 35);}\n"
"\n"
"QComboBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.graphicsComboBox)

        self.widescreenCheckBox = QCheckBox(self.graphicsFrame)
        self.widescreenCheckBox.setObjectName(u"widescreenCheckBox")
        sizePolicy1.setHeightForWidth(self.widescreenCheckBox.sizePolicy().hasHeightForWidth())
        self.widescreenCheckBox.setSizePolicy(sizePolicy1)
        self.widescreenCheckBox.setFont(font1)
        self.widescreenCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.widescreenCheckBox.setAutoFillBackground(False)
        self.widescreenCheckBox.setStyleSheet(u"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }")

        self.verticalLayout_4.addWidget(self.widescreenCheckBox)

        self.matrixComboBox = QComboBox(self.graphicsFrame)
        self.matrixComboBox.addItem("")
        self.matrixComboBox.addItem("")
        self.matrixComboBox.addItem("")
        self.matrixComboBox.setObjectName(u"matrixComboBox")
        sizePolicy1.setHeightForWidth(self.matrixComboBox.sizePolicy().hasHeightForWidth())
        self.matrixComboBox.setSizePolicy(sizePolicy1)
        self.matrixComboBox.setFont(font1)
        self.matrixComboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.matrixComboBox.setAutoFillBackground(False)
        self.matrixComboBox.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(12, 14, 35);}\n"
"\n"
"QComboBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.matrixComboBox)


        self.settingsLayout.addWidget(self.graphicsFrame, 0, 2, 1, 1)

        self.soundFrame = QFrame(self.centralWidget)
        self.soundFrame.setObjectName(u"soundFrame")
        self.soundFrame.setFrameShape(QFrame.Box)
        self.verticalLayout_6 = QVBoxLayout(self.soundFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.soundLabel = QLabel(self.soundFrame)
        self.soundLabel.setObjectName(u"soundLabel")
        sizePolicy.setHeightForWidth(self.soundLabel.sizePolicy().hasHeightForWidth())
        self.soundLabel.setSizePolicy(sizePolicy)
        self.soundLabel.setFont(font)
        self.soundLabel.setMouseTracking(False)
        self.soundLabel.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.soundLabel.setLayoutDirection(Qt.LeftToRight)
        self.soundLabel.setAutoFillBackground(False)
        self.soundLabel.setFrameShape(QFrame.Box)
        self.soundLabel.setFrameShadow(QFrame.Plain)
        self.soundLabel.setLineWidth(1)
        self.soundLabel.setScaledContents(False)
        self.soundLabel.setWordWrap(True)
        self.soundLabel.setMargin(5)

        self.verticalLayout_6.addWidget(self.soundLabel)

        self.soundComboBox = QComboBox(self.soundFrame)
        self.soundComboBox.addItem("")
        self.soundComboBox.addItem("")
        self.soundComboBox.addItem("")
        self.soundComboBox.addItem("")
        self.soundComboBox.setObjectName(u"soundComboBox")
        sizePolicy1.setHeightForWidth(self.soundComboBox.sizePolicy().hasHeightForWidth())
        self.soundComboBox.setSizePolicy(sizePolicy1)
        self.soundComboBox.setFont(font1)
        self.soundComboBox.setAutoFillBackground(False)
        self.soundComboBox.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(12, 14, 35);}\n"
"\n"
"QComboBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.soundComboBox)

        self.soundcardCheckBox = QCheckBox(self.soundFrame)
        self.soundcardCheckBox.setObjectName(u"soundcardCheckBox")
        sizePolicy1.setHeightForWidth(self.soundcardCheckBox.sizePolicy().hasHeightForWidth())
        self.soundcardCheckBox.setSizePolicy(sizePolicy1)
        self.soundcardCheckBox.setFont(font1)
        self.soundcardCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.soundcardCheckBox.setAutoFillBackground(False)
        self.soundcardCheckBox.setStyleSheet(u"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }")

        self.verticalLayout_6.addWidget(self.soundcardCheckBox)

        self.webcamCheckBox = QCheckBox(self.soundFrame)
        self.webcamCheckBox.setObjectName(u"webcamCheckBox")
        sizePolicy1.setHeightForWidth(self.webcamCheckBox.sizePolicy().hasHeightForWidth())
        self.webcamCheckBox.setSizePolicy(sizePolicy1)
        self.webcamCheckBox.setFont(font1)
        self.webcamCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.webcamCheckBox.setAutoFillBackground(False)
        self.webcamCheckBox.setStyleSheet(u"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }")

        self.verticalLayout_6.addWidget(self.webcamCheckBox)


        self.settingsLayout.addWidget(self.soundFrame, 0, 3, 1, 1)

        self.netDataFrame = QFrame(self.centralWidget)
        self.netDataFrame.setObjectName(u"netDataFrame")
        self.netDataFrame.setFrameShape(QFrame.Box)
        self.verticalLayout_7 = QVBoxLayout(self.netDataFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.netDataLabel = QLabel(self.netDataFrame)
        self.netDataLabel.setObjectName(u"netDataLabel")
        sizePolicy.setHeightForWidth(self.netDataLabel.sizePolicy().hasHeightForWidth())
        self.netDataLabel.setSizePolicy(sizePolicy)
        self.netDataLabel.setFont(font)
        self.netDataLabel.setMouseTracking(False)
        self.netDataLabel.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.netDataLabel.setLayoutDirection(Qt.LeftToRight)
        self.netDataLabel.setAutoFillBackground(False)
        self.netDataLabel.setFrameShape(QFrame.Box)
        self.netDataLabel.setFrameShadow(QFrame.Plain)
        self.netDataLabel.setLineWidth(1)
        self.netDataLabel.setScaledContents(False)
        self.netDataLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.netDataLabel)

        self.wirelessCheckBox = QCheckBox(self.netDataFrame)
        self.wirelessCheckBox.setObjectName(u"wirelessCheckBox")
        sizePolicy1.setHeightForWidth(self.wirelessCheckBox.sizePolicy().hasHeightForWidth())
        self.wirelessCheckBox.setSizePolicy(sizePolicy1)
        self.wirelessCheckBox.setFont(font1)
        self.wirelessCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.wirelessCheckBox.setAutoFillBackground(False)
        self.wirelessCheckBox.setStyleSheet(u"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }")

        self.verticalLayout_7.addWidget(self.wirelessCheckBox)

        self.opticCheckBox = QCheckBox(self.netDataFrame)
        self.opticCheckBox.setObjectName(u"opticCheckBox")
        sizePolicy1.setHeightForWidth(self.opticCheckBox.sizePolicy().hasHeightForWidth())
        self.opticCheckBox.setSizePolicy(sizePolicy1)
        self.opticCheckBox.setFont(font1)
        self.opticCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.opticCheckBox.setAutoFillBackground(False)
        self.opticCheckBox.setStyleSheet(u"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }\n"
"")

        self.verticalLayout_7.addWidget(self.opticCheckBox)

        self.dataCheckBox = QCheckBox(self.netDataFrame)
        self.dataCheckBox.setObjectName(u"dataCheckBox")
        sizePolicy1.setHeightForWidth(self.dataCheckBox.sizePolicy().hasHeightForWidth())
        self.dataCheckBox.setSizePolicy(sizePolicy1)
        self.dataCheckBox.setFont(font1)
        self.dataCheckBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.dataCheckBox.setAutoFillBackground(False)
        self.dataCheckBox.setStyleSheet(u"QCheckBox:hover {\n"
"	color: #8bdbff;\n"
"}\n"
" QCheckBox:checked {\n"
"                color: yellow;\n"
"            }")

        self.verticalLayout_7.addWidget(self.dataCheckBox)


        self.settingsLayout.addWidget(self.netDataFrame, 0, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.settingsLayout)

        self.algorithmLayout = QHBoxLayout()
        self.algorithmLayout.setObjectName(u"algorithmLayout")
        self.modeFrame = QFrame(self.centralWidget)
        self.modeFrame.setObjectName(u"modeFrame")
        self.modeFrame.setMaximumSize(QSize(400, 16777215))
        self.modeFrame.setFrameShape(QFrame.Box)
        self.verticalLayout_1 = QVBoxLayout(self.modeFrame)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.modeLabel = QLabel(self.modeFrame)
        self.modeLabel.setObjectName(u"modeLabel")
        sizePolicy.setHeightForWidth(self.modeLabel.sizePolicy().hasHeightForWidth())
        self.modeLabel.setSizePolicy(sizePolicy)
        self.modeLabel.setFont(font1)
        self.modeLabel.setLayoutDirection(Qt.LeftToRight)
        self.modeLabel.setAutoFillBackground(False)
        self.modeLabel.setFrameShape(QFrame.Box)
        self.modeLabel.setAlignment(Qt.AlignCenter)
        self.modeLabel.setWordWrap(True)

        self.verticalLayout_1.addWidget(self.modeLabel)

        self.modeComboBox = QComboBox(self.modeFrame)
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.addItem("")
        self.modeComboBox.setObjectName(u"modeComboBox")
        sizePolicy1.setHeightForWidth(self.modeComboBox.sizePolicy().hasHeightForWidth())
        self.modeComboBox.setSizePolicy(sizePolicy1)
        self.modeComboBox.setFont(font1)
        self.modeComboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.modeComboBox.setAutoFillBackground(False)
        self.modeComboBox.setStyleSheet(u"QComboBox {\n"
"background-color: rgb(12, 14, 35);\n"
"}\n"
"\n"
"\n"
"QComboBox:hover {\n"
"	color: #8bdbff;\n"
"}")

        self.verticalLayout_1.addWidget(self.modeComboBox)

        self.algorithmButton = QPushButton(self.modeFrame)
        self.algorithmButton.setObjectName(u"algorithmButton")
        sizePolicy1.setHeightForWidth(self.algorithmButton.sizePolicy().hasHeightForWidth())
        self.algorithmButton.setSizePolicy(sizePolicy1)
        self.algorithmButton.setFont(font1)
        self.algorithmButton.setCursor(QCursor(Qt.OpenHandCursor))
        self.algorithmButton.setMouseTracking(False)
        self.algorithmButton.setAutoFillBackground(False)
        self.algorithmButton.setStyleSheet(u"QPushButton:hover {\n"
"	color: #8bdbff;\n"
"}\n"
"QPushButton {\n"
"	border: 1px solid white;\n"
"	}\n"
"\n"
"")

        self.verticalLayout_1.addWidget(self.algorithmButton)


        self.algorithmLayout.addWidget(self.modeFrame)

        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setFont(font1)
        self.progressBar.setValue(0)
        self.progressBar.setInvertedAppearance(False)

        self.algorithmLayout.addWidget(self.progressBar)


        self.verticalLayout_2.addLayout(self.algorithmLayout)

        mainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"PC Assembly", None))
        self.sizeLabel.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0418\u041c\u041e\u0413\u0418 \u0414\u041e \u0413\u0415\u041e\u041c\u0415\u0422\u0420\u0406\u0407 \u0422\u0410 \u041f\u0415\u0420\u0418\u0424\u0415\u0420\u0406\u0407 \u041f\u041a", None))
        self.sizeCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u041c\u0430\u043b\u0456 \u0440\u043e\u0437\u043c\u0456\u0440\u0438 \u043a\u043e\u0440\u043f\u0443\u0441\u0443 \u041f\u041a", None))
        self.upsCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0411\u0435\u0437\u043f\u0435\u0440\u0435\u0431\u0456\u0439\u043d\u0430 \u0440\u043e\u0431\u043e\u0442\u0430", None))
        self.peripheralCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0411\u0435\u0437\u0434\u0440\u043e\u0442\u043e\u0432\u0430 \u043f\u0435\u0440\u0438\u0444\u0435\u0440\u0456\u044f", None))
        self.cpuLabel.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0418\u041c\u041e\u0413\u0418 \u0414\u041e \u0421\u041f\u0415\u0426\u0418\u0424\u0406\u041a\u0410\u0426\u0406\u0419 \u041f\u0410\u0420\u0410\u041c\u0415\u0422\u0420\u0406\u0412 \u041f\u0420\u041e\u0426\u0415\u0421\u041e\u0420\u0423", None))
        self.multithreadRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u041c\u0443\u043b\u044c\u0442\u0438\u043f\u043e\u0442\u043e\u0447\u043d\u0456\u0441\u0442\u044c", None))
        self.coreRadioButton.setText(QCoreApplication.translate("mainWindow", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c \u043d\u0430 \u044f\u0434\u0440\u043e", None))
        self.companyComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"AMD/Intel", None))
        self.companyComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"Intel", None))
        self.companyComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"AMD", None))

        self.graphicsLabel.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0418\u041c\u041e\u0413\u0418 \u0414\u041e \u0421\u041f\u0415\u0426\u0418\u0424\u0406\u041a\u0410\u0426\u0406\u0419 \u0413\u0420\u0410\u0424\u0406\u0427\u041d\u041e\u0413\u041e \u041e\u0411\u041b\u0410\u0414\u041d\u0410\u041d\u041d\u042f", None))
        self.graphicsComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"\u0413\u0440\u0430\u0444\u0456\u043a\u0430 \u0456\u043d\u0442\u0435\u0433\u0440\u043e\u0432\u0430\u043d\u0430", None))
        self.graphicsComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u0413\u0440\u0430\u0444\u0456\u043a\u0430 \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u043d\u0430", None))
        self.graphicsComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"\u0406\u043d\u0442\u0435\u0433\u0440\u043e\u0432\u0430\u043d\u0430 + \u0434\u0438\u0441\u043a\u0440\u0435\u0442\u043d\u0430", None))

        self.widescreenCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0428\u0438\u0440\u043e\u043a\u043e\u0444\u043e\u0440\u043c\u0430\u0442\u043d\u0438\u0439 \u0435\u043a\u0440\u0430\u043d", None))
        self.matrixComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0448\u0432\u0438\u0434\u043a\u043e\u0441\u0442\u0456 \u0456 \u044f\u043a\u043e\u0441\u0442\u0456", None))
        self.matrixComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u0428\u0432\u0438\u0434\u043a\u0456\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0456 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f", None))
        self.matrixComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"\u042f\u043a\u0456\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0456 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f", None))

        self.soundLabel.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0418\u041c\u041e\u0413\u0418 \u0414\u041e \u0421\u041f\u0415\u0426\u0418\u0424\u0406\u041a\u0410\u0426\u0406\u0419 \u0417\u0412\u0423\u041a\u041e\u0412\u041e\u0413\u041e \u041e\u0411\u041b\u0410\u0414\u041d\u0410\u041d\u041d\u042f", None))
        self.soundComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"\u0417\u0432\u0438\u0447\u0430\u0439\u043d\u0456 \u0434\u0438\u043d\u0430\u043c\u0456\u043a\u0438", None))
        self.soundComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u041d\u0430\u0432\u0443\u0448\u043d\u0438\u043a\u0438", None))
        self.soundComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"\u0413\u0430\u0440\u043d\u0456\u0442\u0443\u0440\u0430", None))
        self.soundComboBox.setItemText(3, QCoreApplication.translate("mainWindow", u"\u0413\u0430\u0440\u043d\u0456\u0442\u0443\u0440\u0430 + \u0434\u0438\u043d\u0430\u043c\u0456\u043a\u0438", None))

        self.soundcardCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0420\u043e\u0431\u043e\u0442\u0430 \u0437\u0456 \u0437\u0432\u0443\u043a\u043e\u0432\u0438\u043c\u0438 \u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
        self.webcamCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u041d\u0435\u043e\u0431\u0445\u0456\u0434\u043d\u0456\u0441\u0442\u044c \u0432\u0456\u0434\u0435\u043e\u043a\u0430\u043c\u0435\u0440\u0438", None))
        self.netDataLabel.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0418\u041c\u041e\u0413\u0418 \u0414\u041e \u041d\u0410\u041a\u041e\u041f\u0418\u0427\u0423\u0412\u0410\u0427\u0406\u0412 \u0414\u0410\u041d\u0418\u0425 \u0422\u0410 \u041c\u0415\u0420\u0415\u0416\u0406", None))
        self.wirelessCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0411\u0435\u0437\u0434\u0440\u043e\u0442\u043e\u0432\u0430 \u043c\u0435\u0440\u0435\u0436\u0430", None))
        self.opticCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0420\u043e\u0431\u043e\u0442\u0430 \u0437 CD/DVD", None))
        self.dataCheckBox.setText(QCoreApplication.translate("mainWindow", u"\u0412\u0435\u043b\u0438\u043a\u0438\u0439 \u043e\u0431\u0441\u044f\u0433 \u043f\u0430\u043c'\u044f\u0442\u0456", None))
        self.modeLabel.setText(QCoreApplication.translate("mainWindow", u"\u0420\u0415\u0416\u0418\u041c \u0420\u041e\u0411\u041e\u0422\u0418 \u0410\u041b\u0413\u041e\u0420\u0418\u0422\u041c\u0423 \u041f\u0406\u0414\u0411\u041e\u0420\u0423", None))
        self.modeComboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430 \u0435\u043a\u043e\u043d\u043e\u043c\u0456\u044f \u043a\u043e\u0448\u0442\u0456\u0432 ", None))
        self.modeComboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0456 \u0442\u0430 \u0446\u0456\u043d\u0438", None))
        self.modeComboBox.setItemText(2, QCoreApplication.translate("mainWindow", u"\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0438\u0432\u043d\u0456\u0441\u0442\u044c", None))

        self.algorithmButton.setText(QCoreApplication.translate("mainWindow", u"\u0420\u043e\u0437\u043f\u043e\u0447\u0430\u0442\u0438 \u0440\u043e\u0437\u0440\u0430\u0445\u0443\u043d\u043e\u043a", None))
    # retranslateUi

