import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
fruits=pd.read_table('fruit_data_with_colors.txt');
#fruits.info()
fruits.head(2)
#X=fruits[['mass','width','height','color_score']]
#Y=fruits['fruit_label']
#X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=0)
#from matplotlib import cm
#cmap = cm.get_cmap('gnuplot')

#scatter = pd.plotting.scatter_matrix(X_train, c = Y_train, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(12,12),cmap=cmap)
from mpl_toolkits.mplot3d import Axes3D
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c = Y_train, marker = 'o', s=100)
#ax.set_xlabel('width')
#ax.set_xlabel('height')
#ax.set_xlabel('color_score')
#plt.show()
