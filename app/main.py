import utils#Este es el modulo que nosotros creamos
import readCSV
import charts


def run():
    data = readCSV.readCSV('./data.csv') #Usando nuestro modulo readCSV para que nos de la data que tiene
    data = list(filter(lambda continent: continent['Continent'] == 'North America',data))#Filtrado de continentes
    countries = list(map(lambda country : country['Country/Territory'],data))
    percentages = list(map(lambda percentage : percentage['World Population Percentage'],data))
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