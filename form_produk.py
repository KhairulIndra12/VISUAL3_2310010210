from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class form_produk(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = QFile("form_produk.ui"); f.open(QFile.ReadOnly)
        self.form = QUiLoader().load(f, self); f.close()
        self.crud = my_cruddb()
        self.jenis_kodes=[]; self.user_ids=[]
        self.loadFK()
        self.form.btnSimpan.clicked.connect(self.doSimpan)
        self.form.btnUbah.clicked.connect(self.doUbah)
        self.form.btnHapus.clicked.connect(self.doHapus)
        self.form.btnBersih.clicked.connect(self.doBersih)
        self.form.table.cellClicked.connect(self.klikTabel)
        self.form.editCari.textChanged.connect(self.doCari)
        self.tampilData()

    def loadFK(self):
        self.form.comboJenis.clear(); self.jenis_kodes=[]
        for j in self.crud.listJenis():
            self.jenis_kodes.append(j["kode"]); self.form.comboJenis.addItem(j["nama"])
        self.form.comboUser.clear(); self.user_ids=[]
        for u in self.crud.listUsers():
            self.user_ids.append(u["id"]); self.form.comboUser.addItem(u["name"])
        self.form.comboStatus.clear(); self.form.comboStatus.addItems(["berlaku","tidak_berlaku"])

    def jenisKode(self):
        i=self.form.comboJenis.currentIndex()
        return self.jenis_kodes[i] if 0<=i<len(self.jenis_kodes) else None

    def userId(self):
        i=self.form.comboUser.currentIndex()
        return self.user_ids[i] if 0<=i<len(self.user_ids) else None

    def doBersih(self):
        f=self.form
        f.edit_id.clear(); f.edit_nomor.clear(); f.edit_tahun.clear(); f.edit_tentang.clear()
        f.edit_tgl_tetap.clear(); f.edit_tgl_undang.clear(); f.edit_berkas.clear()
        if self.form.comboJenis.count()>0: self.form.comboJenis.setCurrentIndex(0)
        if self.form.comboUser.count()>0: self.form.comboUser.setCurrentIndex(0)
        self.form.comboStatus.setCurrentIndex(0); f.edit_id.setFocus()

    def doSimpan(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","id belum diisi"); return
        self.crud.simpanProduk(
            f.edit_id.text(), self.jenisKode(), f.edit_nomor.text(), f.edit_tahun.text(), f.edit_tentang.text(),
            f.edit_tgl_tetap.text(), f.edit_tgl_undang.text(), f.edit_berkas.text(),
            self.form.comboStatus.currentText(), self.userId()
        )
        self.tampilData(); QMessageBox.information(self,"Info","Tersimpan"); self.doBersih()

    def doUbah(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","Pilih data dulu"); return
        self.crud.ubahProduk(
            f.edit_id.text(), self.jenisKode(), f.edit_nomor.text(), f.edit_tahun.text(), f.edit_tentang.text(),
            f.edit_tgl_tetap.text(), f.edit_tgl_undang.text(), f.edit_berkas.text(),
            self.form.comboStatus.currentText(), self.userId()
        )
        self.tampilData(); QMessageBox.information(self,"Info","Diubah")

    def doHapus(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","Pilih data dulu"); return
        if QMessageBox.question(self,"Konfirmasi","Hapus data ini?",QMessageBox.Yes|QMessageBox.No)==QMessageBox.No: return
        self.crud.hapusProduk(f.edit_id.text()); self.tampilData(); self.doBersih()

    def tampilData(self):
        data=self.crud.dataProduk(); t=self.form.table; t.setRowCount(0)
        for row in data:
            i=t.rowCount(); t.insertRow(i)
            t.setItem(i,0,QTableWidgetItem(str(row.get("id",""))))
            t.setItem(i,1,QTableWidgetItem(str(row.get("jenis_kode",""))))
            t.setItem(i,2,QTableWidgetItem(str(row.get("jenis_nama",""))))
            t.setItem(i,3,QTableWidgetItem(str(row.get("nomor",""))))
            t.setItem(i,4,QTableWidgetItem(str(row.get("tahun",""))))
            t.setItem(i,5,QTableWidgetItem(str(row.get("tentang",""))))
            t.setItem(i,6,QTableWidgetItem(str(row.get("tanggal_penetapan",""))))
            t.setItem(i,7,QTableWidgetItem(str(row.get("tanggal_pengundangan",""))))
            t.setItem(i,8,QTableWidgetItem(str(row.get("berkas",""))))
            t.setItem(i,9,QTableWidgetItem(str(row.get("status",""))))
            t.setItem(i,10,QTableWidgetItem(str(row.get("created_by",""))))
            t.setItem(i,11,QTableWidgetItem(str(row.get("created_name",""))))

    def doCari(self):
        key=self.form.editCari.text(); data=self.crud.cariProduk(key); t=self.form.table; t.setRowCount(0)
        for row in data:
            i=t.rowCount(); t.insertRow(i)
            t.setItem(i,0,QTableWidgetItem(str(row.get("id",""))))
            t.setItem(i,1,QTableWidgetItem(str(row.get("jenis_kode",""))))
            t.setItem(i,2,QTableWidgetItem(str(row.get("jenis_nama",""))))
            t.setItem(i,3,QTableWidgetItem(str(row.get("nomor",""))))
            t.setItem(i,4,QTableWidgetItem(str(row.get("tahun",""))))
            t.setItem(i,5,QTableWidgetItem(str(row.get("tentang",""))))
            t.setItem(i,6,QTableWidgetItem(str(row.get("tanggal_penetapan",""))))
            t.setItem(i,7,QTableWidgetItem(str(row.get("tanggal_pengundangan",""))))
            t.setItem(i,8,QTableWidgetItem(str(row.get("berkas",""))))
            t.setItem(i,9,QTableWidgetItem(str(row.get("status",""))))
            t.setItem(i,10,QTableWidgetItem(str(row.get("created_by",""))))
            t.setItem(i,11,QTableWidgetItem(str(row.get("created_name",""))))

    def klikTabel(self, r, c):
        t=self.form.table; f=self.form
        f.edit_id.setText(t.item(r,0).text() if t.item(r,0) else "")
        jk=t.item(r,1).text() if t.item(r,1) else ""
        if jk in self.jenis_kodes: self.form.comboJenis.setCurrentIndex(self.jenis_kodes.index(jk))
        f.edit_nomor.setText(t.item(r,3).text() if t.item(r,3) else "")
        f.edit_tahun.setText(t.item(r,4).text() if t.item(r,4) else "")
        f.edit_tentang.setText(t.item(r,5).text() if t.item(r,5) else "")
        f.edit_tgl_tetap.setText(t.item(r,6).text() if t.item(r,6) else "")
        f.edit_tgl_undang.setText(t.item(r,7).text() if t.item(r,7) else "")
        f.edit_berkas.setText(t.item(r,8).text() if t.item(r,8) else "")
        st=t.item(r,9).text() if t.item(r,9) else "berlaku"
        idx=self.form.comboStatus.findText(st)
        if idx>=0: self.form.comboStatus.setCurrentIndex(idx)
        try:
            uid=int(t.item(r,10).text())
            if uid in self.user_ids: self.form.comboUser.setCurrentIndex(self.user_ids.index(uid))
        except: pass
