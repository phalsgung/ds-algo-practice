import matplotlib.pyplot as plt

Clusters = ["Cluster 1", "Cluster 2", "Cluster 3"]
TotalFeatures = [5, 8, 10]
NewFeatures = [1, 2, 4]
OldFeatures = [4, 6, 6]

plt.xlabel("Clusters")
plt.ylabel("Features")

plt.bar(Clusters,OldFeatures, color='r')
plt.bar(Clusters, NewFeatures, bottom=OldFeatures, color='b')

plt.legend(["Old Features", "New Features"])
plt.show()