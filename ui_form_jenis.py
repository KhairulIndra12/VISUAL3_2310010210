# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_jenis.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_FormJenis(object):
    def setupUi(self, FormJenis):
        if not FormJenis.objectName():
            FormJenis.setObjectName(u"FormJenis")
        FormJenis.resize(860, 580)
        self.formLayoutWidget = QWidget(FormJenis)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 521, 175))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_kode = QLabel(self.formLayoutWidget)
        self.lbl_kode.setObjectName(u"lbl_kode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_kode)

        self.edit_kode = QLineEdit(self.formLayoutWidget)
        self.edit_kode.setObjectName(u"edit_kode")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_kode)

        self.lbl_nama = QLabel(self.formLayoutWidget)
        self.lbl_nama.setObjectName(u"lbl_nama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_nama)

        self.edit_nama = QLineEdit(self.formLayoutWidget)
        self.edit_nama.setObjectName(u"edit_nama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.edit_nama)

        self.lbl_keterangan = QLabel(self.formLayoutWidget)
        self.lbl_keterangan.setObjectName(u"lbl_keterangan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_keterangan)

        self.edit_keterangan = QLineEdit(self.formLayoutWidget)
        self.edit_keterangan.setObjectName(u"edit_keterangan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.edit_keterangan)

        self.btnSimpan = QPushButton(FormJenis)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(560, 20, 121, 28))
        self.btnUbah = QPushButton(FormJenis)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(560, 55, 121, 28))
        self.btnHapus = QPushButton(FormJenis)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(560, 90, 121, 28))
        self.btnBersih = QPushButton(FormJenis)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(560, 125, 121, 28))
        self.editCari = QLineEdit(FormJenis)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 200, 311, 28))
        self.table = QTableWidget(FormJenis)
        if (self.table.columnCount() < 3):
            self.table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 235, 831, 331))
        self.table.setColumnCount(3)
        self.table.setRowCount(0)

        self.retranslateUi(FormJenis)

        QMetaObject.connectSlotsByName(FormJenis)
    # setupUi

    def retranslateUi(self, FormJenis):
        FormJenis.setWindowTitle(QCoreApplication.translate("FormJenis", u"Form Jenis", None))
        self.lbl_kode.setText(QCoreApplication.translate("FormJenis", u"kode", None))
        self.lbl_nama.setText(QCoreApplication.translate("FormJenis", u"nama", None))
        self.lbl_keterangan.setText(QCoreApplication.translate("FormJenis", u"keterangan", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormJenis", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormJenis", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormJenis", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormJenis", u"Bersih", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("FormJenis", u"Cari...", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormJenis", u"kode", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormJenis", u"nama", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormJenis", u"keterangan", None));
    # retranslateUi

