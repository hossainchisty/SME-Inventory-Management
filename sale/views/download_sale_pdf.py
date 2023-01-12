from datetime import date

from django.http import HttpResponse
from django.views.generic import View
from sale.models import Sale
from utility.render_to_pdf import generate_pdf


class DownloadSalePDF(View):
    '''
    Automaticly downloads to PDF file.
    '''
    def get(self, request, *args, **kwargs):
        sales = Sale.objects.all().order_by('-id')
        pdf = generate_pdf('sales/pdf/sales_pdf.html', {'sales': sales})
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Sales-Data-%s.pdf" % date.today()
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response
