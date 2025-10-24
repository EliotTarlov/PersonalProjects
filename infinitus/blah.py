from copy import deepcopy
import random
import networkx as nx
if False:
    flights = [["New York","Chicago",100],["Chicago","Denver",100],["Denver","New York",100],["Chicago","Los Angeles",600],["Denver","Los Angeles",200], ["New York","Los Angeles",900]]

    src = "New York"
    dst = "Los Angeles" 

    k = 1

    cities=set()
    for i in flights:
        cities.add(i[0])
        cities.add(i[1])

    flightsDict=dict()

    for city in cities:
        flightsDict[city]=list()
    for source, destination, cost in flights:
        flightsDict[source].append((destination, cost))


#randomized unit test
cities=list(range(20))
flightsDict={i:list() for i in cities}
for city in cities:
    destinations=(random.sample(cities[:city]+cities[city+1:],random.randint(0,len(cities)-1)))
    for i in destinations:
        flightsDict[city].append((i,random.randint(0,1000)))
src=14
dst=1

G=nx.Graph()
edge_list=list()
for i in flightsDict.keys():
    for j in flightsDict[i]:
        edge_list.append((i,j))
G.add_edges_from(edge_list)
nx.draw(G)

k=2
costToEachCity={city:float("inf") for city in cities}
costToEachCity[src]=0

#at a given number of hops, find the optimal cost to each city
for _ in range(k+1): 
    newCosts=deepcopy(costToEachCity)
    for source in flightsDict.keys():
        if costToEachCity[source] != float("inf"):
            for destination, cost in flightsDict[source]:
                #if cost is less than our current best, set it to the new one
                newCosts[destination]=min(costToEachCity[source]+cost, newCosts [destination])
    costToEachCity=newCosts
print(costToEachCity)

print(costToEachCity[dst])
