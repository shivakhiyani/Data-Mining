# -*- coding: utf-8 -*-
"""Q6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zzKSjSwltZlpnU7GzS1U5RKarlzKpD79
"""

import matplotlib.pyplot as plt
import pandas as pd
from numpy import sqrt

def fetch_moons_data():
  moons=[]
  url = 'http://www.ccs.neu.edu/home/vip/teach/DMcourse/2_cluster_EM_mixt/HW2/moons.csv'
  data = pd.read_csv(url)
  for i in range(data.shape[0]):
    moons.append([i,data['Xmoons_X1'][i],data['Xmoons_X2'][i]])
  return moons

def fetch_blobs_data():
  blobs=[]
  url = 'http://www.ccs.neu.edu/home/vip/teach/DMcourse/2_cluster_EM_mixt/HW2/blobs.csv'
  data = pd.read_csv(url)
  for i in range(data.shape[0]):
    blobs.append([i,data['Xblobs_X1'][i],data['Xblobs_X2'][i]])
  return blobs

def fetch_circle_data():
  circle=[]
  url = 'http://www.ccs.neu.edu/home/vip/teach/DMcourse/2_cluster_EM_mixt/HW2/circle.csv'
  data = pd.read_csv(url)
  for i in range(data.shape[0]):
    circle.append([i,data['Xcircle_X1'][i],data['Xcircle_X2'][i]])
  return circle

def find_neighbors(data, data_item,eps):
  neighbor_pts = []
  for point in data:
    if sqrt((data_item[1] - point[1])**2 +(data_item[2]-point[2])**2)<eps:
      neighbor_pts.append(point)
  return neighbor_pts

def cluster_formation(data,visited_pts,neighbor_pts,clusters,eps,index,min_pts):
  for point in neighbor_pts:
    if point not in visited_pts:
      neighbor_pts_add = find_neighbors(data,point,eps)
      visited_pts.append(point)
      if len(neighbor_pts_add)>=min_pts:
        neighbor_pts += neighbor_pts_add
    x= False
    for cluster in clusters:
      if point in cluster:
        x = True
    if x== False:
      clusters[index].append(point)

def dbscan(data,eps, min_pts):
  visited_pts=[]
  clusters=[]
  index = 0
  noise_pts = []
  for data_item in data:
    if data_item not in visited_pts:
      neighbor_pts = find_neighbors(data,data_item,eps)
      if len(neighbor_pts)>=min_pts:
        visited_pts.append(data_item)
        clusters.append([])
        clusters[index].append(data_item)
        cluster_formation(data,visited_pts,neighbor_pts,clusters,eps,index,min_pts)
        index +=1
      else:
        noise_pts.append(data_item)

  return clusters


def plot_clusters(clusters):

  for cluster in clusters:
    plt.scatter([point[1] for point in cluster], [point[2] for point in cluster])
  plt.show

# print(clusters)

dataset = fetch_circle_data()
clusters = dbscan(dataset,0.2,15)
plot_clusters(clusters)

dataset = fetch_blobs_data()
clusters = dbscan(dataset,0.15,15)
plot_clusters(clusters)

dataset = fetch_moons_data()
clusters = dbscan(dataset,0.2,10)
plot_clusters(clusters)