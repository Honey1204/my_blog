from django.contrib import admin
from visulaizer.models import FormDetails
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class FormDetailsAdmin(admin.ModelAdmin):
	list_display = ['Unit','Date','Blowroom','Waste_Collection','Carding',
					'Comber_Drawing','Speed_Frame','Pre_Total','Spg_DB1','Spg_DB2','Spg_DB3',
					'Spg_DB4','Spg_Total','Autoconner','Post_spinning_total','Pre_HMD','Spg1_HMD','Spg2_HMD','Post_Spg_HMD','Total',
						'Compressor','Lighting','Total_Units','Production','UKG','s40s_con_pro','s40s_Con_Ukg','s40s_Compac_con_pr',
							's40s_Compac_con_ukg']
	search_fields = ['Date','Unit']


admin.site.register(FormDetails,FormDetailsAdmin)
