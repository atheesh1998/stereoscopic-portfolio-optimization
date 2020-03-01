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
from scipy.stats import linregress

#importing the Excel file that contains our features data
fundamentals=pd.ExcelFile('SPO_Data.xlsx')

#parsing the Fundamentals sheet from our Excel file of which holds our P/E, EPS, and MarketCap data
features=fundamentals.parse('Fundamentals')

#dropping name column
features=features.drop('Name', axis=1, inplace=True)

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

#dropping symbol column
features_copy=features_copy.drop('Symbol', axis=1, inplace=True)

#finding K using elbow graph
find_k(features_copy.fillna(0))

#initialzing K-Means algorithm
kmeans = KMeans(n_clusters=15, random_state=101)
#fitting kmeans to our features data
kmeans.fit(features_copy.fillna(0))
#getting cluster labels
features_copy['Cluster'] = kmeans.labels_

#creating dataframe to hold data
clusters_df = pd.DataFrame()
#grouping our data by cluster for clusters with atleast 2 stocks in it.
clusters_df = pd.concat(i for clusters_df, i in features_copy.groupby(features_copy['Cluster']) if len(i) > 1)

#creating method to identify each possible pair

def create_pairs(symbolList):
    #creating a list to hold each possible pair
    pairs = []
    #initializing placeholders for the symbols in each pair
    x = 0
    y = 0
    for count, symbol in enumerate(symbolList):
        for nextCount, nextSymbol in enumerate(symbolList):
            x = symbol
            y = nextSymbol
            if x != y:
                pairs.append([x, y])

    return pairs


#creating list of symbols from cluster 0
symbol_list_0 = ['ADBE', 'AET', 'AIG', 'ANTM', 'AMAT']
#list of lists of pairs
all_pairs = create_pairs(symbol_list_0)

#initializing our stock variables
adbe = pd.read_csv('ADBE_5min.csv')
aet = pd.read_csv('AET_5min.csv')
aig = pd.read_csv('AIG_5min.csv')
antm = pd.read_csv('ANTM_5min.csv')
amat = pd.read_csv('AMAT_5min.csv')







