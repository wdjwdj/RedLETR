#Code Snippet 2: Unlocking XLSX workbooks and worksheets using Python win32com.client library

import win32com.client as win32
import glob
excel = win32.gencache.EnsureDispatch('Excel.Application')
ws_pass = 'some_password'
glob_base_path = 'C:\CONVERTED\*\*.xlsx'
excel_files_to_process = glob.glob(glob_base_path)
for xlsx_file in excel_files_to_process:
      print xlsx_file
      wb = excel.Workbooks.Open( xlsx_file)
      for ws in wb.Worksheets:
          print 'Unprotecting Worksheet:',ws.Name
          ws.Unprotect(ncv.ws_pass)
      wb.Unprotect(ncv.ws_pass)
      excel.ActiveWorkbook.Close(SaveChanges=1)

