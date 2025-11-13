from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class form_users(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = QFile("form_users.ui"); f.open(QFile.ReadOnly)
        self.form = QUiLoader().load(f, self); f.close()
        self.crud = my_cruddb()
        self.role_ids=[]
        self.loadRole()
        self.form.btnSimpan.clicked.connect(self.doSimpan)
        self.form.btnUbah.clicked.connect(self.doUbah)
        self.form.btnHapus.clicked.connect(self.doHapus)
        self.form.btnBersih.clicked.connect(self.doBersih)
        self.form.table.cellClicked.connect(self.klikTabel)
        self.form.editCari.textChanged.connect(self.doCari)
        self.tampilData()

    def loadRole(self):
        self.form.comboRole.clear(); self.role_ids=[]
        for r in self.crud.listRoles():
            self.role_ids.append(r["id"]); self.form.comboRole.addItem(r["nama_role"])

    def roleId(self):
        i=self.form.comboRole.currentIndex()
        return self.role_ids[i] if 0<=i<len(self.role_ids) else None

    def doBersih(self):
        f=self.form; f.edit_id.clear(); f.edit_name.clear(); f.edit_email.clear(); f.edit_password.clear()
        if self.form.comboRole.count()>0: self.form.comboRole.setCurrentIndex(0)
        f.edit_id.setFocus()

    def doSimpan(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","id belum diisi"); return
        self.crud.simpanUser(f.edit_id.text(), f.edit_name.text(), f.edit_email.text(), f.edit_password.text(), self.roleId())
        self.tampilData(); QMessageBox.information(self,"Info","Tersimpan"); self.doBersih()

    def doUbah(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","Pilih data dulu"); return
        self.crud.ubahUser(f.edit_id.text(), f.edit_name.text(), f.edit_email.text(), f.edit_password.text(), self.roleId())
        self.tampilData(); QMessageBox.information(self,"Info","Diubah")

    def doHapus(self):
        f=self.form
        if not f.edit_id.text().strip(): QMessageBox.information(self,"Info","Pilih data dulu"); return
        if QMessageBox.question(self,"Konfirmasi","Hapus data ini?",QMessageBox.Yes|QMessageBox.No)==QMessageBox.No: return
        self.crud.hapusUser(f.edit_id.text()); self.tampilData(); self.doBersih()

    def tampilData(self):
        data=self.crud.dataUser(); t=self.form.table; t.setRowCount(0)
        for row in data:
            i=t.rowCount(); t.insertRow(i)
            t.setItem(i,0,QTableWidgetItem(str(row.get("id",""))))
            t.setItem(i,1,QTableWidgetItem(str(row.get("name",""))))
            t.setItem(i,2,QTableWidgetItem(str(row.get("email",""))))
            t.setItem(i,3,QTableWidgetItem(str(row.get("password",""))))
            t.setItem(i,4,QTableWidgetItem(str(row.get("role_id",""))))

    def doCari(self):
        key=self.form.editCari.text(); data=self.crud.cariUser(key); t=self.form.table; t.setRowCount(0)
        for row in data:
            i=t.rowCount(); t.insertRow(i)
            t.setItem(i,0,QTableWidgetItem(str(row.get("id",""))))
            t.setItem(i,1,QTableWidgetItem(str(row.get("name",""))))
            t.setItem(i,2,QTableWidgetItem(str(row.get("email",""))))
            t.setItem(i,3,QTableWidgetItem(str(row.get("password",""))))
            t.setItem(i,4,QTableWidgetItem(str(row.get("role_id",""))))

    def klikTabel(self, r, c):
        t=self.form.table; f=self.form
        f.edit_id.setText(t.item(r,0).text() if t.item(r,0) else "")
        f.edit_name.setText(t.item(r,1).text() if t.item(r,1) else "")
        f.edit_email.setText(t.item(r,2).text() if t.item(r,2) else "")
        f.edit_password.setText(t.item(r,3).text() if t.item(r,3) else "")
        try:
            rid=int(t.item(r,4).text())
            if rid in self.role_ids: self.form.comboRole.setCurrentIndex(self.role_ids.index(rid))
        except: pass
