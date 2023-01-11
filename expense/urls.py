from django.urls import path

from expense.views.add_expense_views import CreateExpense
from expense.views.add_type_views import CreateType
from expense.views.delete_expense_views import DeleteExpense
from expense.views.download_expense_pdf import DownloadExpensePDF
from expense.views.expense_pdf_views import ViewExpensePDF
from expense.views.export_expense_csv_views import DownloadExpenseCSV
from expense.views.export_expense_excle_views import DownloadExpenseEXCLE
from expense.views.manage_expense_views import ExpenseType, ManageExpense
from expense.views.update_expense_type_views import UpdateType
from expense.views.update_expense_views import UpdateExpense

urlpatterns = [
    path('list', ManageExpense.as_view(), name='expense_list'),
    path('add/', CreateExpense.as_view(), name='add_expense'),
    path('update/<int:pk>', UpdateExpense.as_view(), name='update_expense'),
    path('delete/<int:pk>', DeleteExpense.as_view(), name='delete_expense'),

    path('type/add/', CreateType.as_view(), name='add_type'),
    path('type/list/', ExpenseType.as_view(), name='expense_type_list'),
    path('update/type/<int:pk>', UpdateType.as_view(), name='update_expense_type'),

    # File management
    path('export/csv/', DownloadExpenseCSV.as_view(), name='download_expense_csv'),
    path('export/excle/', DownloadExpenseEXCLE.as_view(), name='download_expense_excle'),
    path('pdf/', ViewExpensePDF.as_view(), name='view_expense_pdf'),
    path('pdf/download/', DownloadExpensePDF.as_view(), name="pdf_expense_download")
]
