import matplotlib.pyplot as plt

def generatePieChart():
    labels=['A','B','C']
    values = [100,200,300]

    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()