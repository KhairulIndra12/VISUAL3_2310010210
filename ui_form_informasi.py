# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_informasi.ui'
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
    QTableWidget, QTableWidgetItem, QTextEdit, QWidget)

class Ui_FormInformasi(object):
    def setupUi(self, FormInformasi):
        if not FormInformasi.objectName():
            FormInformasi.setObjectName(u"FormInformasi")
        FormInformasi.resize(980, 620)
        self.formLayoutWidget = QWidget(FormInformasi)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 621, 260))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_id = QLabel(self.formLayoutWidget)
        self.lbl_id.setObjectName(u"lbl_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_id)

        self.edit_id = QLineEdit(self.formLayoutWidget)
        self.edit_id.setObjectName(u"edit_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_id)

        self.lbl_judul = QLabel(self.formLayoutWidget)
        self.lbl_judul.setObjectName(u"lbl_judul")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_judul)

        self.edit_judul = QLineEdit(self.formLayoutWidget)
        self.edit_judul.setObjectName(u"edit_judul")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.edit_judul)

        self.lbl_isi = QLabel(self.formLayoutWidget)
        self.lbl_isi.setObjectName(u"lbl_isi")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_isi)

        self.edit_isi = QTextEdit(self.formLayoutWidget)
        self.edit_isi.setObjectName(u"edit_isi")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.edit_isi)

        self.lbl_berkas = QLabel(self.formLayoutWidget)
        self.lbl_berkas.setObjectName(u"lbl_berkas")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_berkas)

        self.edit_berkas = QLineEdit(self.formLayoutWidget)
        self.edit_berkas.setObjectName(u"edit_berkas")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.edit_berkas)

        self.lbl_tglpub = QLabel(self.formLayoutWidget)
        self.lbl_tglpub.setObjectName(u"lbl_tglpub")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_tglpub)

        self.edit_tanggal_publikasi = QLineEdit(self.formLayoutWidget)
        self.edit_tanggal_publikasi.setObjectName(u"edit_tanggal_publikasi")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.edit_tanggal_publikasi)

        self.lbl_user = QLabel(self.formLayoutWidget)
        self.lbl_user.setObjectName(u"lbl_user")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lbl_user)

        self.comboUser = QComboBox(self.formLayoutWidget)
        self.comboUser.setObjectName(u"comboUser")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.comboUser)

        self.btnSimpan = QPushButton(FormInformasi)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(660, 20, 121, 28))
        self.btnUbah = QPushButton(FormInformasi)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(660, 55, 121, 28))
        self.btnHapus = QPushButton(FormInformasi)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(660, 90, 121, 28))
        self.btnBersih = QPushButton(FormInformasi)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(660, 125, 121, 28))
        self.editCari = QLineEdit(FormInformasi)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 290, 311, 28))
        self.table = QTableWidget(FormInformasi)
        if (self.table.columnCount() < 7):
            self.table.setColumnCount(7)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 325, 951, 281))
        self.table.setColumnCount(7)
        self.table.setRowCount(0)

        self.retranslateUi(FormInformasi)

        QMetaObject.connectSlotsByName(FormInformasi)
    # setupUi

    def retranslateUi(self, FormInformasi):
        FormInformasi.setWindowTitle(QCoreApplication.translate("FormInformasi", u"Form Informasi", None))
        self.lbl_id.setText(QCoreApplication.translate("FormInformasi", u"id", None))
        self.lbl_judul.setText(QCoreApplication.translate("FormInformasi", u"judul", None))
        self.lbl_isi.setText(QCoreApplication.translate("FormInformasi", u"isi", None))
        self.lbl_berkas.setText(QCoreApplication.translate("FormInformasi", u"berkas", None))
        self.lbl_tglpub.setText(QCoreApplication.translate("FormInformasi", u"tanggal_publikasi", None))
        self.lbl_user.setText(QCoreApplication.translate("FormInformasi", u"created_by", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormInformasi", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormInformasi", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormInformasi", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormInformasi", u"Bersih", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("FormInformasi", u"Cari...", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormInformasi", u"id", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormInformasi", u"judul", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormInformasi", u"isi", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormInformasi", u"berkas", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormInformasi", u"tanggal_publikasi", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormInformasi", u"created_by", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FormInformasi", u"created_name", None));
    # retranslateUi

