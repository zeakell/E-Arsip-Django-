from django.db import models
from multiselectfield import MultiSelectField

class Surats(models.Model):
	CATEGORY = (
						('Biasa', 'Biasa'),
						('Segera', 'Segera'),
						('Mendesak','Mendesak'),
						)
	KLASFIK = (
						('Kilat', 'Kilat'),
						('Express', 'Express'),
						('Biasa','Biasa'),
						)
	STATUS = (
						('True', 'True'),
						('False', 'False'),
						)
		

	nomor_surat =  models.CharField(max_length=100,unique=True)
	tanggal_surat = models.DateField()
	kategori = models.CharField(max_length=50, null=False, choices=CATEGORY)
	klasifikasi = models.CharField(max_length=50, null=False, choices=KLASFIK)
	tujuan = models.CharField(max_length=50, null=False)
	pengirim = models.CharField(max_length=100)
	perihal = models.TextField(default = '')
	attachment = models.FileField(upload_to='filesimpan/attachments/')
	st_dispo=models.CharField(default='False',max_length=5,choices=STATUS)
	st_arsip=models.CharField(default='False',max_length=5,choices=STATUS)

	def __str__(self):
			return self.nomor_surat

class TSuratKeluar(models.Model):
	CATEGORY = (
						('Biasa', 'Biasa'),
						('Segera', 'Segera'),
						('Mendesak','Mendesak'),
						)
	KLASFIK = (
						('Umum', 'Umum'),
						('Khusus', 'Khusus'),
						('Kilat','Kilat'),
						)
	STATUS = (
						('True', 'True'),
						('False', 'False'),
						)

	Nomor_surat =  models.CharField(max_length=100,unique=True)
	Tanggal_surat = models.DateField()
	Kategori = models.CharField(max_length=50, null=False, choices=CATEGORY)
	Klasifikasi = models.CharField(max_length=50, null=False, choices=KLASFIK)
	Tujuan = models.CharField(max_length=100)
	Tembusan = models.CharField(max_length=100)
	Perihal = models.TextField(default = 'Default ')
	Attachment = models.FileField(upload_to='filekeluar/attachments/')
	st_arsip=models.CharField(default='False',max_length=5, null=False, choices=STATUS)

	def __str__(self):
			return self.Nomor_surat

class tbl_pejabat(models.Model):

	id_pejabat =   models.CharField(max_length=50, null=False)
	nrp =  models.CharField(max_length=50, null=False)
	id_jabatan = models.CharField(max_length=50)
	nm_pejabat = models.CharField(max_length=50, null=False)
	tmt_jab =  models.CharField(max_length=50, null=False)

	def __str__(self):
			return self.id_pejabat

class Disposisi(models.Model):
	BAGIAN = (
						('KABAGOPSSAN', 'KABAGOPSSAN'),
						('KABAGMINSISSAN', 'KABAGMINSISSAN'),
						('DANSATKOMSAN','DANSATKOMSAN'),
						('DANSATPAMSAN', 'DANSATPAMSAN'),
						('DANSATLIDSAN', 'DANSATLIDSAN'),
						('BATIURMIN','BATIURMIN'),
						)
	DISPOS = (
						('Ump', 'Ump'),
						('Udk', 'Udk'),
						('Udl','Udl'),
						('Siapkan', 'Siapkan'),
						('Arsipkan', 'Arsipkan'),
						('Pelajari','Pelajari'),
						('Ikuti Perkembangannya', 'Ikuti Perkembangannya'),
						('Laporkan Hasilnya', 'Laporkan Hasilnya'),
						('Monitor','Monitor'),
						('Sesuaikan Juk Danpussansiad', 'Sesuaikan Juk Danpussansiad'),
						)

	Nomor_Disposisi = models.CharField(max_length=100,unique=True)
	Nomor_Agenda_tu =  models.CharField(max_length=100)
	Nomor_Surat =  models.CharField(max_length=100,unique=True)
	Diterima = models.CharField(max_length=100)
	Tanggal_Surat = models.DateField()
	Tanggal_Surat_Akhir = models.DateField()
	Bagian = MultiSelectField(null=False, choices=BAGIAN)
	Dispos = MultiSelectField(null=False, choices=DISPOS)
	Perihall = models.TextField(default = '')
	Attachmentt = models.FileField(upload_to='filesimpan/attachments/')
	catatan = models.TextField(default = '', null=True)

def __str__(self):
			return self.Nomor_Disposisi

class tbl_dispo(models.Model):

	id_dispo=models.AutoField(primary_key=True)
	nm_dispo=models.TextField(null=False,max_length=100)

def __str__(self):
			return self.id_dispo

class tmt_bagian(models.Model):

	id_bagian=models.AutoField(primary_key=True)
	nm_bagian=models.TextField(null=False,max_length=100)

def __str__(self):
			return self.id_dispo

class tbl_suratmasuk(models.Model):
	CATEGORY = (
						('Biasa', 'Biasa'),
						('Segera', 'Segera'),
						('Mendesak','Mendesak'),
						)
	KLASFIK = (
						('Kilat', 'Kilat'),
						('Express', 'Express'),
						('Biasa','Biasa'),
						)
	STATUS = (
						('True', 'True'),
						('False', 'False'),
						)
		

	nomor_surat =  models.CharField(max_length=100)
	tanggal_surat = models.DateField()
	kategori = models.CharField(max_length=50, null=False, choices=CATEGORY)
	klasifikasi = models.CharField(max_length=50, null=False, choices=KLASFIK)
	tujuan = models.CharField(max_length=50, null=False)
	pengirim = models.CharField(max_length=100)
	perihal = models.TextField(default = '')
	attachment = models.FileField(upload_to='filesimpan/attachments/')
	st_dispo=models.CharField(default='False',max_length=5, null=False, choices=STATUS)
	st_arsip=models.CharField(default='False',max_length=5, null=False, choices=STATUS)

	def __str__(self):
			return self.nomor_surat
		

class tbl_login(models.Model):

	roles = (
				('Analis','Analis'),
				('Bagum','Bagum'),
				)

	id_login=models.CharField(max_length=100)
	nrp=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	role=models.CharField(max_length=100,choices=roles)

