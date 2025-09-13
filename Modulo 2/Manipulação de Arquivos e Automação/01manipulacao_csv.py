import csv # importtamos o csv

with open('lista_de_compras.tsv','w', newline='', encoding='utf-8') as csvFile:
          csvWriter = csv.writer(csvFile,delimiter='\t',lineterminator='\n') # a função para a construção de arquivo

          csvWriter.writerow(['maçãs','bananas','morangos']) # escrevendo as linhas 
          csvWriter.writerow(['leite','iorgute','queijo'])
          csvWriter.writerow(['sabão','detergente','esponja'])