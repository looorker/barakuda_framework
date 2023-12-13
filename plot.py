import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3),(1, 4),(1, 5),(1, 6),(1, 7),(1, 8)])
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.title('Сеть ')
plt.style.use('seaborn-v0_8-poster')
plt.plasma()
var = plt.colormaps()

plt.show()