from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,1.5,3,5,3.5,4.5])
y = np.array([1,2,4,7,5,5])

#plt.plot()
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('Dataset')
plt.scatter(x, y)
plt.show()

#plt.plot()
X = np.array(list(zip(x, y)))
colors = ['b', 'g']
markers = ['o', 'v']

# KMeans algorithm
kmeans_model = KMeans(n_clusters=2).fit(X)

#plt.plot()
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(x[i], y[i], color=colors[l], marker=markers[l],ls='None')
    plt.xlim([0, 10])
    plt.ylim([0, 10])

plt.show()