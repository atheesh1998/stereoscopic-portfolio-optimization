#data analysis and manipulation
import numpy as np
import pandas as pd

#data visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

#statistics and machine learning
from statsmodels.tsa.api import adfuller
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture as GM
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.metrics import confusion_matrix, classification_report
from scipy.spatial.distance import cdist

#importing the Excel file that contains our features data
fundamentals=pd.ExcelFile('SPO_Data.xlsx')

#parsing the Fundamentals sheet from our Excel file of which holds our P/E, EPS, and MarketCap data
features=fundamentals.parse('Fundamentals')

#dropping name column
features.drop('Name',axis=1,inplace=True)

#creating our elbow technique method
def find_k(features):
    #intializing a list to hold costs or errors
    costs=[]
    
    #iterating over possible values for k
    for k in range(1,51):
        model=KMeans(n_clusters=k) 
        model.fit(features)
        costs.append(sum(np.min(cdist(features,model.cluster_centers_,'euclidean'),axis=1)))
    
    #plotting our elbow graph    
    with plt.style.context(['classic','ggplot']):
        plt.figure(figsize=(10,6))
        plt.plot(costs)
        plt.xlabel('Clusters')
        plt.ylabel('Errors')
        plt.title('Finding K')
        plt.show()

#making a copy of our original features dataframe
features_copy=features.copy()

#reindexing our features dataframe
features_copy=features_copy.reindex(index=features_copy['Symbol'],columns=features_copy.columns)

#adding our data back to their respective columns
features_copy['P/E']=features['P/E'].values
features_copy['EPS']=features['EPS'].values
features_copy['MarketCap']=features['MarketCap'].values

