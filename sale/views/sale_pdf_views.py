from django.http import HttpResponse
from django.views.generic import View
from sale.models import Sale
from utility.render_to_pdf import generate_pdf


class ViewSalePDF(View):
	def get(self, request, *args, **kwargs):
		sales = Sale.objects.all().order_by('-id')
		pdf = generate_pdf('sales/pdf/sales_pdf.html', {'sales': sales})
		return HttpResponse(pdf, content_type='application/pdf')
