# -*- coding: utf-8 -*-
"""Q5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oxt-LMFmM_GHaQQknGU8dhxCTS9-Hr5W
"""

def fetch_dbscan_data():
  db_pts = []
  neighbors = []
  url = 'http://www.ccs.neu.edu/home/vip/teach/DMcourse/2_cluster_EM_mixt/HW2/dbscan.csv'
  data = pd.read_csv(url)
  for i in range(data.shape[0]):
    db_pts.append([data['pt'][i],data['x'][i],data['y'][i]])
    neighbors.append([data['pt'][i],data['num_neighbors'][i],data['neighbors'][i]])
  return db_pts, neighbors

def expandcluster(data,visited_pts,neighbor_pts,neighbor_points,clusters,index,min_pts):
  for point in neighbor_points:
    if point not in visited_pts:
      visited_pts.append(point)
      if neighbor_pts[point[0]][1]>=min_pts:
        neighbor_points_add = []
        Points = neighbor_pts[point[0]][2].split(",")
        for i in Points:
          neighbor_points_add.append(data[int(i)])
        neighbor_points += neighbor_points_add
    x= False
    for cluster in clusters:
      if point in cluster:
        x = True
    if x== False:
      clusters[index].append(point)

def dbscan(data,neighbor_pts, min_pts):
  visited_pts=[]
  clusters=[]
  index = 0
  noise_pts = []
  for data_item in data:
    if data_item not in visited_pts:
      if neighbor_pts[data_item[0]][1]>=min_pts:
        visited_pts.append(data_item)
        neighbor_points=[]
        Points = neighbor_pts[data_item[0]][2].split(",")
        for i in Points:
          neighbor_points.append(data[int(i)])
        clusters.append([])
        clusters[index].append(data_item)
        expandcluster(data,visited_pts,neighbor_pts,neighbor_points,clusters,index,min_pts)
        index +=1
      else:
        noise_pts.append(data_item)
  for data_item in noise_pts:
    clusters.append([])
    clusters[index].append(data_item)
  return clusters


def plot_clusters(clusters):

  for cluster in clusters:
    plt.scatter([point[1] for point in cluster], [float(point[2]) for point in cluster])
  plt.show

dataset,neighbors = fetch_dbscan_data()
clusters= dbscan(dataset,neighbors,3)
print(clusters)
plot_clusters(clusters)