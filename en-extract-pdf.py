import camelot


tables = camelot.read_pdf('tabela_jogos.pdf', pages='1')
print(tables)

tables.export('game.csv', f='csv', compress=True)
tables[0].to_csv('game1.csv')