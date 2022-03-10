import os

from botcity.plugins.excel import BotExcelPlugin

bot_excel = BotExcelPlugin(active_sheet='Sample')
bot_excel.read(os.path.join(os.path.abspath(''), 'FinancialSample.xlsx'))

# bot_excel.add_column(['New Col 1', '0', '1', '2'], 'Sample')  # [col_name, col_rows...]
# bot_excel.add_columns(
#     [
#         ['New Col 2', '00', '11', '22'],
#         ['New Col 3', '00', '11', '22']
#     ], 'Sample')  # [[col_name, col_rows...], ...]

# bot_excel.remove_column(column='a')
# bot_excel.remove_columns(columns=['a', 'b'])

# bot_excel.add_row(['a', 'b', 'c', 'd'], 'Sample')
# bot_excel.add_rows([['a', 'b', 'c', 'd'], ['aa', 'bb', 'cc', 'dd']], 'Sample')

# bot_excel.remove_row(row=6)
# bot_excel.remove_rows(rows=[5, 6])

# print(bot_excel.as_dataframe())
# print(bot_excel.as_list())

# bot_excel.clear()

# bot_excel.clear_range(range_='A5:D7')

# bot_excel.rename_sheet(new_name='Sample', sheet='Sheet')
# bot_excel.create_sheet(sheet='Sheet2')
# bot_excel.remove_sheet(sheet='Sheet2')

# bot_excel.set_cell(column='a', row=1, value='Changed 0', sheet='Sample')
# bot_excel.set_range(values=[['Changed 1', 'Changed 2']], range_='A1:B1', sheet='Sample')

# print(bot_excel.get_cell('a', 2))  # (column_letter, row_num)
# print(bot_excel.get_column(column='a'))  # get column values
# print(bot_excel.get_range(range_='A1:D2'))
# print(bot_excel.get_row(row=1))
# print(bot_excel.list_sheets())

# bot_excel.sort(by_columns=['D'], ascending=True, start_row=2)

bot_excel.write(file_or_path=os.path.join(os.path.abspath(''), 'FinancialSample.xlsx'))
