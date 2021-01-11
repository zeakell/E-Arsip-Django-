from django.contrib import admin
from dapur.models import Surats
from dapur.models import TSuratKeluar
from dapur.models import tbl_pejabat
from dapur.models import tbl_dispo
from dapur.models import Disposisi
from dapur.models import tbl_login

# Register your models here.
#admin.site.register(Students)

admin.site.register(Surats)
admin.site.register(TSuratKeluar)
admin.site.register(tbl_pejabat)
admin.site.register(Disposisi)
admin.site.register(tbl_dispo)
admin.site.register(tbl_login)
