# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 640)
        self.actionFormJenis = QAction(MainWindow)
        self.actionFormJenis.setObjectName(u"actionFormJenis")
        self.actionFormRoles = QAction(MainWindow)
        self.actionFormRoles.setObjectName(u"actionFormRoles")
        self.actionFormUsers = QAction(MainWindow)
        self.actionFormUsers.setObjectName(u"actionFormUsers")
        self.actionFormInformasi = QAction(MainWindow)
        self.actionFormInformasi.setObjectName(u"actionFormInformasi")
        self.actionFormProduk = QAction(MainWindow)
        self.actionFormProduk.setObjectName(u"actionFormProduk")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menuMaster = QMenu(self.menubar)
        self.menuMaster.setObjectName(u"menuMaster")
        self.menuTransaksi = QMenu(self.menubar)
        self.menuTransaksi.setObjectName(u"menuTransaksi")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMaster.menuAction())
        self.menubar.addAction(self.menuTransaksi.menuAction())
        self.menuMaster.addAction(self.actionFormJenis)
        self.menuMaster.addAction(self.actionFormRoles)
        self.menuMaster.addAction(self.actionFormUsers)
        self.menuTransaksi.addAction(self.actionFormInformasi)
        self.menuTransaksi.addAction(self.actionFormProduk)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aplikasi DB Hukum", None))
        self.actionFormJenis.setText(QCoreApplication.translate("MainWindow", u"Form Jenis", None))
        self.actionFormRoles.setText(QCoreApplication.translate("MainWindow", u"Form Roles", None))
        self.actionFormUsers.setText(QCoreApplication.translate("MainWindow", u"Form Users", None))
        self.actionFormInformasi.setText(QCoreApplication.translate("MainWindow", u"Form Informasi", None))
        self.actionFormProduk.setText(QCoreApplication.translate("MainWindow", u"Form Produk", None))
        self.menuMaster.setTitle(QCoreApplication.translate("MainWindow", u"Master", None))
        self.menuTransaksi.setTitle(QCoreApplication.translate("MainWindow", u"Transaksi", None))
    # retranslateUi

