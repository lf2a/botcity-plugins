from botcity.plugins.csv import BotCSVPlugin

bot_csv = BotCSVPlugin()

# open csv
bot_csv.read('sample.csv')

# set separator character
bot_csv.set_separator(separator=',')  # default ','

# get csv header
csv_header = bot_csv.header
print(csv_header)

# add row style 1
bot_csv.add_row({'col1': '11', 'col2': '22', 'col3': '33'})

# add row style 2
bot_csv.add_row(['x', 'y', 'z'])

# add rows style
bot_csv.add_rows([{'col1': '11', 'col2': '22', 'col3': '33'}, {'col1': '11', 'col2': '22', 'col3': '33'}])

# remove row by row index
bot_csv.remove_row(row=2)

# remove row by row index
bot_csv.remove_rows(rows=[1, 2])

# remove column by column name
bot_csv.remove_column(columns='col1')

# sort rows by column name
bot_csv.sort(by_columns=['col2'], ascending=False)

# save csv
bot_csv.write('sample.csv')

# csv to matrix
print(bot_csv.as_list())

# csv to dict
print(bot_csv.as_dict())

# csv to pandas dataframe
print(bot_csv.as_dataframe())
