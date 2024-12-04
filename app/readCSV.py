import csv

def readCSV(path):
    with open(path,'r') as csvFile:
        reader = csv.reader(csvFile,delimiter=',')#reader es un iterable
        header = next(reader)
        data=[]
        for row in reader:
            iterable = zip(header,row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
   data = readCSV('./app/data.csv')
   print(data[0])

#Para resolver este desafío, debes utilizar el archivo data.csv que contiene los datos de los gastos de una empresa. 
#El archivo tiene dos columnas: el nombre del área y el total de gastos del año.

#Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. 
#Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, 
#puedes calcular el total de gastos implementando la lógica que consideres necesaria.

# import csv
# import functools

# def read_csv(path):
#    with open(path, 'r',) as csvFile:
#       reader = csv.reader(csvFile,delimiter=',')#reader es un iterable
#       data=[] #Creando lista donde pondremos los nuevos valores
#       for row in reader: #por casa fila de reader 
#          data.append(int(row[1]))#agregamos los datoss que esten en la posicion 1 a nuestra lista #data
#    total = functools.reduce(lambda x , y: x+y, data) #Sumamos cada uno de esos datos
#    return total

# response = read_csv('./data.csv')
# print(response)
