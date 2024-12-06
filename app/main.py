import utils#Este es el modulo que nosotros creamos
import readCSV
import charts
import pandas as pd


def run():
    # data = readCSV.readCSV('./data.csv') #Usando nuestro modulo readCSV para que nos de la data que tiene
    # data = list(filter(lambda continent: continent['Continent'] == 'North America',data))#Filtrado de continentes
    # countries = list(map(lambda country : country['Country/Territory'],data))
    # percentages = list(map(lambda percentage : percentage['World Population Percentage'],data))
    

    data = readCSV.readCSV('./data.csv') #Usando nuestro modulo readCSV para que nos de la data que tiene
    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Africa']
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generatePieChart(countries,percentages)
    
    country = input('Type Country => ')
    print(country)
    result = utils.populationByCountry(data,country)
    if len(result)>0:
        country = result[0]
        labels,values = utils.getPopulation(country)
        charts.generateBarChart(country['Country/Territory'],labels,values)

#Este if nos ayuda a ejecutar el archivo directamente desde la terminal
if __name__ == '__main__':
    run()