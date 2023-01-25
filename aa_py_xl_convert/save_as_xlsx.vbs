' This is supposed to be temporary, until we can find a way to read `.xlsb` files directly without Windows or Excel.

Set fso = CreateObject("Scripting.FileSystemObject")
Set xl = CreateObject("Excel.Application")

xl.EnableEvents = False
xl.DisplayAlerts = False
xl.Visible = False
xl.ScreenUpdating = False
xl.UserControl = False
xl.Interactive = False

' Get args
inputPath = fso.GetAbsolutePathName(WScript.Arguments(0))
outputPath = fso.GetAbsolutePathName(WScript.Arguments(1))

' Open Excel Workbook
Set wb = xl.Workbooks.Open(inputPath)

wb.SaveAs outputPath, 51  ' 51 = xlOpenXMLWorkbook xlsx
wb.Close
xl.Quit
