# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_users.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_FormUsers(object):
    def setupUi(self, FormUsers):
        if not FormUsers.objectName():
            FormUsers.setObjectName(u"FormUsers")
        FormUsers.resize(860, 580)
        self.formLayoutWidget = QWidget(FormUsers)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 521, 220))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_id = QLabel(self.formLayoutWidget)
        self.lbl_id.setObjectName(u"lbl_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_id)

        self.edit_id = QLineEdit(self.formLayoutWidget)
        self.edit_id.setObjectName(u"edit_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_id)

        self.lbl_name = QLabel(self.formLayoutWidget)
        self.lbl_name.setObjectName(u"lbl_name")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_name)

        self.edit_name = QLineEdit(self.formLayoutWidget)
        self.edit_name.setObjectName(u"edit_name")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.edit_name)

        self.lbl_email = QLabel(self.formLayoutWidget)
        self.lbl_email.setObjectName(u"lbl_email")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_email)

        self.edit_email = QLineEdit(self.formLayoutWidget)
        self.edit_email.setObjectName(u"edit_email")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.edit_email)

        self.lbl_password = QLabel(self.formLayoutWidget)
        self.lbl_password.setObjectName(u"lbl_password")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_password)

        self.edit_password = QLineEdit(self.formLayoutWidget)
        self.edit_password.setObjectName(u"edit_password")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.edit_password)

        self.lbl_role = QLabel(self.formLayoutWidget)
        self.lbl_role.setObjectName(u"lbl_role")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_role)

        self.comboRole = QComboBox(self.formLayoutWidget)
        self.comboRole.setObjectName(u"comboRole")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboRole)

        self.btnSimpan = QPushButton(FormUsers)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(560, 20, 121, 28))
        self.btnUbah = QPushButton(FormUsers)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(560, 55, 121, 28))
        self.btnHapus = QPushButton(FormUsers)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(560, 90, 121, 28))
        self.btnBersih = QPushButton(FormUsers)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(560, 125, 121, 28))
        self.editCari = QLineEdit(FormUsers)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 250, 311, 28))
        self.table = QTableWidget(FormUsers)
        if (self.table.columnCount() < 5):
            self.table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 285, 831, 281))
        self.table.setRowCount(0)
        self.table.setColumnCount(5)

        self.retranslateUi(FormUsers)

        QMetaObject.connectSlotsByName(FormUsers)
    # setupUi

    def retranslateUi(self, FormUsers):
        FormUsers.setWindowTitle(QCoreApplication.translate("FormUsers", u"Form Users", None))
        self.lbl_id.setText(QCoreApplication.translate("FormUsers", u"id", None))
        self.lbl_name.setText(QCoreApplication.translate("FormUsers", u"<html><head/><body><p>nama</p></body></html>", None))
        self.lbl_email.setText(QCoreApplication.translate("FormUsers", u"email", None))
        self.lbl_password.setText(QCoreApplication.translate("FormUsers", u"password", None))
        self.lbl_role.setText(QCoreApplication.translate("FormUsers", u"role", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormUsers", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormUsers", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormUsers", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormUsers", u"Bersih", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("FormUsers", u"Cari...", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormUsers", u"id", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormUsers", u"name", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormUsers", u"email", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormUsers", u"password", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormUsers", u"role_id", None));
    # retranslateUi

