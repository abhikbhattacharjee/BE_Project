
import pylab as plt
import numpy as np



fn = "C:\\Project\heatmap1.txt"
with open(fn, "r") as f:
    labels = f.readline().rstrip("\n").split()[1:]
data = np.loadtxt(fn, skiprows=1, converters={0:lambda x: 0})
data[data > 1] = 1
data[data == 0] =1.100
plot_data = np.ma.masked_equal(data[:,1:], 0)   
plt.subplots_adjust(left=0.1, bottom=0.15, right=0.99, top=0.95)
plt.imshow(plot_data,cmap= "inferno", interpolation="nearest", aspect = "auto")
#mpl.rcParams['lines.color'] = 'r'
plt.xticks(range(len(labels)), labels, rotation=90, va="top", ha="center")
plt.colorbar()

plt.rcParams["figure.figsize"] = (80,70)
plt.show()
