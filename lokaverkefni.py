import matplotlib.pyplot as plt
import numpy as np

# x ** 2
# 2x
# function to generate coordinates
def
def create_plot(ptype):

    # setting the x-axis vaues
    x = np.arange(-2, 2, 1)
    # setting the y-axis values
    if ptype == 'linear':
        y = x
    elif ptype == 'quadratic':
        y = x ** 2
    elif ptype == 'cubic':
        y = x ** 3
    elif ptype == 'diffrun':
        y = np.diff(x ** 2)
    return (x, y)




# setting a style to use
plt.style.use('fivethirtyeight')

# create a figure
fig = plt.figure()

# define subplots and their positions in figure


plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)

# plotting points on each subplot

x, y = create_plot('diffrun')
print("Þetta eru x gildi",x)
print("Þetta eru y gildi",y)
plt4.plot(y, color='k')
plt4.set_title('$y_1 = x^1$')
plt1.plot(x, color='k')
plt1.set_title('$y_1 = x^1$')






# adjusting space between subplots
fig.subplots_adjust(hspace=.5, wspace=0.5)

# function to show the plot
plt.show()



