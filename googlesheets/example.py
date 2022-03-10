import os

from botcity.plugins.googlesheets import BotGoogleSheetsPlugin

# spreadsheet_id = ''
# bot_sheets = BotGoogleSheetsPlugin('credentials.json', spreadsheet_id)

# bot_sheets.add_column(column=['A', '1', '2', '3'])  # [column_name, column_rows...]
# bot_sheets.remove_column(column='D', sheet='Página1')

# [[column_name, column_rows...], ...]
# bot_sheets.add_columns(columns=[['B', '1', '2', '3'], ['C', '1', '2', '3']], sheet='Página1')
# bot_sheets.remove_columns(columns=['C', 'D'], sheet='Página1')

# bot_sheets.add_row(row=['1', '2', '3', '4'], sheet='Página1')  # [column_value...]
# bot_sheets.remove_row(row=4, sheet='Página1')

# [[column_value...], ...]
# bot_sheets.add_rows(rows=[['1', '2', '3', '4'], ['11', '22', '33', '44']], sheet='Página1')
# bot_sheets.remove_rows(rows=[4, 5], sheet='Página1')

# print(bot_sheets.as_list(sheet='Página1'))

# bot_sheets.clear(sheet='Página1')

# bot_sheets.clear_range(range_='A4:D4')

# bot_sheets.create_sheet(sheet='Página22')
# bot_sheets.remove_sheet(sheet='Página22')

# print(bot_sheets.get_cell(column='A', row=1, sheet='Página1'))
# print(bot_sheets.get_column(column='A', sheet='Página1'))
# print(bot_sheets.get_range(range_='A1:B3'))
# print(bot_sheets.get_row(row=1, sheet='Página1'))
# print(bot_sheets.list_sheets())

# bot_sheets.set_cell(column='A', row=2, value='High2', sheet='Página1')
# bot_sheets.set_range(values=[['High3', '1682000']], range_='A2:B2', sheet='Página1')

# bot_sheets.sort(by_columns=['C'], ascending=True, start_row=2, sheet='Página1')

# bot_sheets2 = BotGoogleSheetsPlugin.new_spreadsheet('credentials.json', 'test_new_spreadsheet')
# print(bot_sheets2.get_spreadsheet_id())
# print(bot_sheets2.get_spreadsheet_link())
