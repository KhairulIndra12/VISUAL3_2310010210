# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_roles.ui'
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

class Ui_FormRoles(object):
    def setupUi(self, FormRoles):
        if not FormRoles.objectName():
            FormRoles.setObjectName(u"FormRoles")
        FormRoles.resize(860, 580)
        self.formLayoutWidget = QWidget(FormRoles)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 521, 175))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_id = QLabel(self.formLayoutWidget)
        self.lbl_id.setObjectName(u"lbl_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_id)

        self.edit_id = QLineEdit(self.formLayoutWidget)
        self.edit_id.setObjectName(u"edit_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_id)

        self.lbl_nama_role = QLabel(self.formLayoutWidget)
        self.lbl_nama_role.setObjectName(u"lbl_nama_role")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_nama_role)

        self.edit_nama_role = QLineEdit(self.formLayoutWidget)
        self.edit_nama_role.setObjectName(u"edit_nama_role")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.edit_nama_role)

        self.lbl_keterangan = QLabel(self.formLayoutWidget)
        self.lbl_keterangan.setObjectName(u"lbl_keterangan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_keterangan)

        self.edit_keterangan = QLineEdit(self.formLayoutWidget)
        self.edit_keterangan.setObjectName(u"edit_keterangan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.edit_keterangan)

        self.btnSimpan = QPushButton(FormRoles)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(560, 20, 121, 28))
        self.btnUbah = QPushButton(FormRoles)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(560, 55, 121, 28))
        self.btnHapus = QPushButton(FormRoles)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(560, 90, 121, 28))
        self.btnBersih = QPushButton(FormRoles)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(560, 125, 121, 28))
        self.editCari = QLineEdit(FormRoles)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 200, 311, 28))
        self.table = QTableWidget(FormRoles)
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

        self.retranslateUi(FormRoles)

        QMetaObject.connectSlotsByName(FormRoles)
    # setupUi

    def retranslateUi(self, FormRoles):
        FormRoles.setWindowTitle(QCoreApplication.translate("FormRoles", u"Form Roles", None))
        self.lbl_id.setText(QCoreApplication.translate("FormRoles", u"id", None))
        self.lbl_nama_role.setText(QCoreApplication.translate("FormRoles", u"nama_role", None))
        self.lbl_keterangan.setText(QCoreApplication.translate("FormRoles", u"keterangan", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormRoles", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormRoles", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormRoles", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormRoles", u"Bersih", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("FormRoles", u"Cari...", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormRoles", u"id", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormRoles", u"nama_role", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormRoles", u"keterangan", None));
    # retranslateUi

