 __author__ = 'dagutman'
"""This will check an XLSX file and unprotect the worksheets"""

### Useful links for background
#http://support.microsoft.com/kb/161245
#http://pythonexcels.com/python-excel-mini-cookbook/

import glob
import sys
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')

glob_base_path = 'C:\CONVERTED\*\*.xlsx'   ### this is the path where the protected XLSX files are stored
ncv.ws_pass = 'NOTEBOOKPASS'  ### This is the password for worksheets/cells that are locked


excel_files_to_process = glob.glob(glob_base_path)

for xlsx_file in excel_files_to_process:
        print xlsx_file
        wb = excel.Workbooks.Open( xlsx_file)
        for ws in wb.Worksheets:
            print ws.Name
            ws.Unprotect(ncv.ws_pass)
        wb.Unprotect(ncv.ws_pass)
        excel.ActiveWorkbook.Close(SaveChanges=1)
        excel.Application.Quit()



