# This Python file uses the following encoding: utf-8
import mysql.connector

class my_cruddb:
    def __init__(self):
        # Sesuaikan kredensial ini jika perlu
        self.conn = mysql.connector.connect(
            host='localhost', user='root', password='', database='db_hukum'
        )

    # ===== Jenis =====
    def simpanJenis(self, kode, nama, keterangan):
        c=self.conn.cursor(); c.execute(
            "INSERT INTO jenis (kode,nama,keterangan) VALUES (%s,%s,%s)",
            (kode,nama,keterangan)); self.conn.commit(); c.close()
    def ubahJenis(self, kode, nama, keterangan):
        c=self.conn.cursor(); c.execute(
            "UPDATE jenis SET nama=%s,keterangan=%s WHERE kode=%s",
            (nama,keterangan,kode)); self.conn.commit(); c.close()
    def hapusJenis(self, kode):
        c=self.conn.cursor(); c.execute("DELETE FROM jenis WHERE kode=%s",(kode,)); self.conn.commit(); c.close()
    def dataJenis(self):
        c=self.conn.cursor(dictionary=True); c.execute("SELECT kode,nama,keterangan FROM jenis ORDER BY kode")
        r=c.fetchall(); c.close(); return r
    def cariJenis(self, key):
        like=f"%{key}%"; c=self.conn.cursor(dictionary=True)
        c.execute("SELECT kode,nama,keterangan FROM jenis WHERE kode LIKE %s OR nama LIKE %s",(like,like))
        r=c.fetchall(); c.close(); return r

    # ===== Roles =====
    def simpanRole(self, id_role, nama_role, keterangan):
        c=self.conn.cursor(); c.execute(
            "INSERT INTO roles (id,nama_role,keterangan) VALUES (%s,%s,%s)",
            (id_role,nama_role,keterangan)); self.conn.commit(); c.close()
    def ubahRole(self, id_role, nama_role, keterangan):
        c=self.conn.cursor(); c.execute(
            "UPDATE roles SET nama_role=%s,keterangan=%s WHERE id=%s",
            (nama_role,keterangan,id_role)); self.conn.commit(); c.close()
    def hapusRole(self, id_role):
        c=self.conn.cursor(); c.execute("DELETE FROM roles WHERE id=%s",(id_role,)); self.conn.commit(); c.close()
    def dataRole(self):
        c=self.conn.cursor(dictionary=True); c.execute("SELECT id,nama_role,keterangan FROM roles ORDER BY id")
        r=c.fetchall(); c.close(); return r
    def cariRole(self, key):
        like=f"%{key}%"; c=self.conn.cursor(dictionary=True)
        c.execute("SELECT id,nama_role,keterangan FROM roles WHERE CAST(id AS CHAR) LIKE %s OR nama_role LIKE %s",(like,like))
        r=c.fetchall(); c.close(); return r

    # ===== Users =====
    def simpanUser(self, id_user, name, email, password, role_id):
        c=self.conn.cursor(); c.execute(
            "INSERT INTO users (id,name,email,password,role_id) VALUES (%s,%s,%s,%s,%s)",
            (id_user,name,email,password,role_id)); self.conn.commit(); c.close()
    def ubahUser(self, id_user, name, email, password, role_id):
        c=self.conn.cursor(); c.execute(
            "UPDATE users SET name=%s,email=%s,password=%s,role_id=%s WHERE id=%s",
            (name,email,password,role_id,id_user)); self.conn.commit(); c.close()
    def hapusUser(self, id_user):
        c=self.conn.cursor(); c.execute("DELETE FROM users WHERE id=%s",(id_user,)); self.conn.commit(); c.close()
    def dataUser(self):
        c=self.conn.cursor(dictionary=True); c.execute("SELECT id,name,email,password,role_id FROM users ORDER BY id")
        r=c.fetchall(); c.close(); return r
    def cariUser(self, key):
        like=f"%{key}%"; c=self.conn.cursor(dictionary=True)
        c.execute("SELECT id,name,email,password,role_id FROM users WHERE CAST(id AS CHAR) LIKE %s OR name LIKE %s OR email LIKE %s",
                  (like,like,like))
        r=c.fetchall(); c.close(); return r

    # ===== Informasi =====
    def simpanInformasi(self, id_info, judul, isi, berkas, tanggal_publikasi, created_by):
        c=self.conn.cursor(); c.execute(
            "INSERT INTO informasi (id,judul,isi,berkas,tanggal_publikasi,created_by) VALUES (%s,%s,%s,%s,%s,%s)",
            (id_info,judul,isi,berkas,tanggal_publikasi,created_by)); self.conn.commit(); c.close()
    def ubahInformasi(self, id_info, judul, isi, berkas, tanggal_publikasi, created_by):
        c=self.conn.cursor(); c.execute(
            "UPDATE informasi SET judul=%s,isi=%s,berkas=%s,tanggal_publikasi=%s,created_by=%s WHERE id=%s",
            (judul,isi,berkas,tanggal_publikasi,created_by,id_info)); self.conn.commit(); c.close()
    def hapusInformasi(self, id_info):
        c=self.conn.cursor(); c.execute("DELETE FROM informasi WHERE id=%s",(id_info,)); self.conn.commit(); c.close()
    def dataInformasi(self):
        c=self.conn.cursor(dictionary=True); c.execute(
            "SELECT i.id,i.judul,i.isi,i.berkas,i.tanggal_publikasi,i.created_by,u.name AS created_name "
            "FROM informasi i LEFT JOIN users u ON u.id=i.created_by ORDER BY i.id")
        r=c.fetchall(); c.close(); return r
    def cariInformasi(self, key):
        like=f"%{key}%"; c=self.conn.cursor(dictionary=True)
        c.execute(
            "SELECT i.id,i.judul,i.isi,i.berkas,i.tanggal_publikasi,i.created_by,u.name AS created_name "
            "FROM informasi i LEFT JOIN users u ON u.id=i.created_by WHERE i.judul LIKE %s OR i.isi LIKE %s",
            (like,like))
        r=c.fetchall(); c.close(); return r

    # ===== Produk =====
    def simpanProduk(self, id_produk, jenis_kode, nomor, tahun, tentang, tanggal_penetapan, tanggal_pengundangan, berkas, status, created_by):
        c=self.conn.cursor(); c.execute(
            "INSERT INTO produk (id,jenis_kode,nomor,tahun,tentang,tanggal_penetapan,tanggal_pengundangan,berkas,status,created_by) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (id_produk,jenis_kode,nomor,tahun,tentang,tanggal_penetapan,tanggal_pengundangan,berkas,status,created_by)); self.conn.commit(); c.close()
    def ubahProduk(self, id_produk, jenis_kode, nomor, tahun, tentang, tanggal_penetapan, tanggal_pengundangan, berkas, status, created_by):
        c=self.conn.cursor(); c.execute(
            "UPDATE produk SET jenis_kode=%s,nomor=%s,tahun=%s,tentang=%s,tanggal_penetapan=%s,tanggal_pengundangan=%s,berkas=%s,status=%s,created_by=%s WHERE id=%s",
            (jenis_kode,nomor,tahun,tentang,tanggal_penetapan,tanggal_pengundangan,berkas,status,created_by,id_produk)); self.conn.commit(); c.close()
    def hapusProduk(self, id_produk):
        c=self.conn.cursor(); c.execute("DELETE FROM produk WHERE id=%s",(id_produk,)); self.conn.commit(); c.close()
    def dataProduk(self):
        c=self.conn.cursor(dictionary=True); c.execute(
            "SELECT p.id,p.jenis_kode,j.nama AS jenis_nama,p.nomor,p.tahun,p.tentang,p.tanggal_penetapan,p.tanggal_pengundangan,p.berkas,p.status,p.created_by,u.name AS created_name "
            "FROM produk p LEFT JOIN jenis j ON j.kode=p.jenis_kode LEFT JOIN users u ON u.id=p.created_by ORDER BY p.id")
        r=c.fetchall(); c.close(); return r
    def cariProduk(self, key):
        like=f"%{key}%"; c=self.conn.cursor(dictionary=True)
        c.execute(
            "SELECT p.id,p.jenis_kode,j.nama AS jenis_nama,p.nomor,p.tahun,p.tentang,p.tanggal_penetapan,p.tanggal_pengundangan,p.berkas,p.status,p.created_by,u.name AS created_name "
            "FROM produk p LEFT JOIN jenis j ON j.kode=p.jenis_kode LEFT JOIN users u ON u.id=p.created_by "
            "WHERE p.nomor LIKE %s OR p.tentang LIKE %s",
            (like,like))
        r=c.fetchall(); c.close(); return r

    # ===== List FK =====
    def listUsers(self):
        c=self.conn.cursor(dictionary=True); c.execute("SELECT id,name FROM users ORDER BY name")
        r=c.fetchall(); c.close(); return r
    def listRoles(self):
        c=self.conn.cursor(dictionary=True); c.execute("SELECT id,nama_role FROM roles ORDER BY id")
        r=c.fetchall(); c.close(); return r
    def listJenis(self):
        c=self.conn.cursor(dictionary=True); c.execute("SELECT kode,nama FROM jenis ORDER BY nama")
        r=c.fetchall(); c.close(); return r
