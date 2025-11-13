from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class form_informasi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = QFile("form_informasi.ui"); f.open(QFile.ReadOnly)
        self.form = QUiLoader().load(f, self); f.close()
        self.crud = my_cruddb()
        self.user_ids=[]
        self.loadUsers()
        self.form.btnSimpan.clicked.connect(self.doSimpan)
        self.form.btnUbah.clicked.connect(self.doUbah)
        self.form.btnHapus.clicked.connect(self.doHapus)
        self.form.btnBersih.clicked.connect(self.doBersih)
        self.form.table.cellClicked.connect(self.klikTabel)
        self.form.editCari.textChanged.connect(self.doCari)
        self.tampilData()

    def loadUsers(self):
        self.form.comboUser.clear(); self.user_ids=[]
        for u in self.crud.listUsers():
            self.user_ids.append(u["id"]); self.form.comboUser.addItem(u["name"])

    def uid(self):
        i=self.form.comboUser.currentIndex()
        return self.user_ids[i] if 0<=i<len(self.user_ids) else None

    def doBersih(self):
        f=self.form
        f.edit_id.clear(); f.edit_judul.clear(); f.edit_isi.clear(); f.edit_berkas.clear(); f.edit_tanggal_publikasi.clear()
        if self.form.comboUser.count()>0: self.form.comboUser.setCurrentIndex(0)
        f.edit_id.setFocus()

    def doSimpan(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","id belum diisi"); return
        self.crud.simpanInformasi(f.edit_id.text(), f.edit_judul.text(), f.edit_isi.toPlainText(), f.edit_berkas.text(), f.edit_tanggal_publikasi.text(), self.uid())
        self.tampilData(); QMessageBox.information(self,"Info","Tersimpan"); self.doBersih()

    def doUbah(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","Pilih data dulu"); return
        self.crud.ubahInformasi(f.edit_id.text(), f.edit_judul.text(), f.edit_isi.toPlainText(), f.edit_berkas.text(), f.edit_tanggal_publikasi.text(), self.uid())
        self.tampilData(); QMessageBox.information(self,"Info","Diubah")

    def doHapus(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","Pilih data dulu"); return
        if QMessageBox.question(self,"Konfirmasi","Hapus data ini?",QMessageBox.Yes|QMessageBox.No)==QMessageBox.No: return
        self.crud.hapusInformasi(f.edit_id.text()); self.tampilData(); self.doBersih()

    def tampilData(self):
        data=self.crud.dataInformasi(); t=self.form.table; t.setRowCount(0)
        for row in data:
            i=t.rowCount(); t.insertRow(i)
            t.setItem(i,0,QTableWidgetItem(str(row.get("id",""))))
            t.setItem(i,1,QTableWidgetItem(str(row.get("judul",""))))
            t.setItem(i,2,QTableWidgetItem(str(row.get("isi",""))))
            t.setItem(i,3,QTableWidgetItem(str(row.get("berkas",""))))
            t.setItem(i,4,QTableWidgetItem(str(row.get("tanggal_publikasi",""))))
            t.setItem(i,5,QTableWidgetItem(str(row.get("created_by",""))))
            t.setItem(i,6,QTableWidgetItem(str(row.get("created_name",""))))

    def doCari(self):
        key=self.form.editCari.text(); data=self.crud.cariInformasi(key); t=self.form.table; t.setRowCount(0)
        for row in data:
            i=t.rowCount(); t.insertRow(i)
            t.setItem(i,0,QTableWidgetItem(str(row.get("id",""))))
            t.setItem(i,1,QTableWidgetItem(str(row.get("judul",""))))
            t.setItem(i,2,QTableWidgetItem(str(row.get("isi",""))))
            t.setItem(i,3,QTableWidgetItem(str(row.get("berkas",""))))
            t.setItem(i,4,QTableWidgetItem(str(row.get("tanggal_publikasi",""))))
            t.setItem(i,5,QTableWidgetItem(str(row.get("created_by",""))))
            t.setItem(i,6,QTableWidgetItem(str(row.get("created_name",""))))

    def klikTabel(self, r, c):
        t=self.form.table; f=self.form
        f.edit_id.setText(t.item(r,0).text() if t.item(r,0) else "")
        f.edit_judul.setText(t.item(r,1).text() if t.item(r,1) else "")
        f.edit_isi.setPlainText(t.item(r,2).text() if t.item(r,2) else "")
        f.edit_berkas.setText(t.item(r,3).text() if t.item(r,3) else "")
        f.edit_tanggal_publikasi.setText(t.item(r,4).text() if t.item(r,4) else "")
        try:
            uid=int(t.item(r,5).text())
            if uid in self.user_ids: self.form.comboUser.setCurrentIndex(self.user_ids.index(uid))
        except: pass
