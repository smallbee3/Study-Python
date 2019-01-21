# XlsxWrite

import xlsxwriter

workbook = xlsxwriter.Workbook('../demo.xlsx')
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 20)
# bold = workbook.add_format({'bold: True'})

worksheet.write('A1', 'Hello')
# worksheet.write('A2', 'World', bold)

worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# worksheet.insert_image('B5', 'logo.png')
workbook.close()
