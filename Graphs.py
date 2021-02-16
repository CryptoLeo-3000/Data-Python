import matplotlib
import pandas

data = pandas.read_csv("Processed_U.S._Crude_Oil.csv")

data.plot(x = 'Months', y = 'U.S. Crude Oil ', figsize =(12, 8), color = 'green')
matplotlib.pyplot.xlabel("Dates")
matplotlib.pyplot.ylabel("Productions")
matplotlib.pyplot.title("U.S. Crude Oil Production")
matplotlib.pyplot.show()