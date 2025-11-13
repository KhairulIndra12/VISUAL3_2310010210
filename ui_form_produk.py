# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_produk.ui'
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

class Ui_FormProduk(object):
    def setupUi(self, FormProduk):
        if not FormProduk.objectName():
            FormProduk.setObjectName(u"FormProduk")
        FormProduk.resize(1000, 640)
        self.formLayoutWidget = QWidget(FormProduk)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 681, 270))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_id = QLabel(self.formLayoutWidget)
        self.lbl_id.setObjectName(u"lbl_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lbl_id)

        self.edit_id = QLineEdit(self.formLayoutWidget)
        self.edit_id.setObjectName(u"edit_id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.edit_id)

        self.lbl_jenis = QLabel(self.formLayoutWidget)
        self.lbl_jenis.setObjectName(u"lbl_jenis")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lbl_jenis)

        self.comboJenis = QComboBox(self.formLayoutWidget)
        self.comboJenis.setObjectName(u"comboJenis")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboJenis)

        self.lbl_nomor = QLabel(self.formLayoutWidget)
        self.lbl_nomor.setObjectName(u"lbl_nomor")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lbl_nomor)

        self.edit_nomor = QLineEdit(self.formLayoutWidget)
        self.edit_nomor.setObjectName(u"edit_nomor")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.edit_nomor)

        self.lbl_tahun = QLabel(self.formLayoutWidget)
        self.lbl_tahun.setObjectName(u"lbl_tahun")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lbl_tahun)

        self.edit_tahun = QLineEdit(self.formLayoutWidget)
        self.edit_tahun.setObjectName(u"edit_tahun")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.edit_tahun)

        self.lbl_tentang = QLabel(self.formLayoutWidget)
        self.lbl_tentang.setObjectName(u"lbl_tentang")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lbl_tentang)

        self.edit_tentang = QLineEdit(self.formLayoutWidget)
        self.edit_tentang.setObjectName(u"edit_tentang")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.edit_tentang)

        self.lbl_tgl_tetap = QLabel(self.formLayoutWidget)
        self.lbl_tgl_tetap.setObjectName(u"lbl_tgl_tetap")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lbl_tgl_tetap)

        self.edit_tgl_tetap = QLineEdit(self.formLayoutWidget)
        self.edit_tgl_tetap.setObjectName(u"edit_tgl_tetap")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.edit_tgl_tetap)

        self.lbl_tgl_undang = QLabel(self.formLayoutWidget)
        self.lbl_tgl_undang.setObjectName(u"lbl_tgl_undang")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lbl_tgl_undang)

        self.edit_tgl_undang = QLineEdit(self.formLayoutWidget)
        self.edit_tgl_undang.setObjectName(u"edit_tgl_undang")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.edit_tgl_undang)

        self.lbl_berkas = QLabel(self.formLayoutWidget)
        self.lbl_berkas.setObjectName(u"lbl_berkas")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lbl_berkas)

        self.edit_berkas = QLineEdit(self.formLayoutWidget)
        self.edit_berkas.setObjectName(u"edit_berkas")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.edit_berkas)

        self.lbl_status = QLabel(self.formLayoutWidget)
        self.lbl_status.setObjectName(u"lbl_status")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lbl_status)

        self.comboStatus = QComboBox(self.formLayoutWidget)
        self.comboStatus.setObjectName(u"comboStatus")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.comboStatus)

        self.lbl_user = QLabel(self.formLayoutWidget)
        self.lbl_user.setObjectName(u"lbl_user")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.lbl_user)

        self.comboUser = QComboBox(self.formLayoutWidget)
        self.comboUser.setObjectName(u"comboUser")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.comboUser)

        self.btnSimpan = QPushButton(FormProduk)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(720, 20, 121, 28))
        self.btnUbah = QPushButton(FormProduk)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(720, 55, 121, 28))
        self.btnHapus = QPushButton(FormProduk)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(720, 90, 121, 28))
        self.btnBersih = QPushButton(FormProduk)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(720, 125, 121, 28))
        self.editCari = QLineEdit(FormProduk)
        self.editCari.setObjectName(u"editCari")
        self.editCari.setGeometry(QRect(10, 300, 311, 28))
        self.table = QTableWidget(FormProduk)
        if (self.table.columnCount() < 12):
            self.table.setColumnCount(12)
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
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(10, 335, 971, 281))
        self.table.setColumnCount(12)
        self.table.setRowCount(0)

        self.retranslateUi(FormProduk)

        QMetaObject.connectSlotsByName(FormProduk)
    # setupUi

    def retranslateUi(self, FormProduk):
        FormProduk.setWindowTitle(QCoreApplication.translate("FormProduk", u"Form Produk Hukum", None))
        self.lbl_id.setText(QCoreApplication.translate("FormProduk", u"id", None))
        self.lbl_jenis.setText(QCoreApplication.translate("FormProduk", u"jenis", None))
        self.lbl_nomor.setText(QCoreApplication.translate("FormProduk", u"nomor", None))
        self.lbl_tahun.setText(QCoreApplication.translate("FormProduk", u"tahun", None))
        self.lbl_tentang.setText(QCoreApplication.translate("FormProduk", u"tentang", None))
        self.lbl_tgl_tetap.setText(QCoreApplication.translate("FormProduk", u"tanggal_penetapan", None))
        self.lbl_tgl_undang.setText(QCoreApplication.translate("FormProduk", u"tanggal_pengundangan", None))
        self.lbl_berkas.setText(QCoreApplication.translate("FormProduk", u"berkas", None))
        self.lbl_status.setText(QCoreApplication.translate("FormProduk", u"status", None))
        self.lbl_user.setText(QCoreApplication.translate("FormProduk", u"created_by", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormProduk", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("FormProduk", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("FormProduk", u"Hapus", None))
        self.btnBersih.setText(QCoreApplication.translate("FormProduk", u"Bersih", None))
        self.editCari.setPlaceholderText(QCoreApplication.translate("FormProduk", u"Cari...", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormProduk", u"id", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormProduk", u"jenis_kode", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormProduk", u"jenis_nama", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormProduk", u"nomor", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormProduk", u"tahun", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormProduk", u"tentang", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FormProduk", u"tanggal_penetapan", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("FormProduk", u"tanggal_pengundangan", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("FormProduk", u"berkas", None));
        ___qtablewidgetitem9 = self.table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("FormProduk", u"status", None));
        ___qtablewidgetitem10 = self.table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("FormProduk", u"created_by", None));
        ___qtablewidgetitem11 = self.table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("FormProduk", u"created_name", None));
    # retranslateUi

