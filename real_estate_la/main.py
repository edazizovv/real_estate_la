#


#
import pandas
import seaborn
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.cluster import KMeans, AgglomerativeClustering
from matplotlib import pyplot

#


#
d = './data/extended.csv'
data = pandas.read_csv(d)


def get_size_house(x):
    if ' м²' in x:
        ix = x.index(' м²')
        xx = x[:ix]
        if ' ' in xx:
            gx = xx.rindex(' ')
            xxx = xx[gx+1:]
            return xxx
        else:
            return 'NA'
    else:
        return 'NA'


def get_size_land(x):
    if ' сот.' in x:
        ix = x.index(' сот.')
        xx = x[:ix]
        if ' ' in xx:
            gx = xx.rindex(' ')
            xxx = xx[gx+1:]
            return xxx
        else:
            return 'NA'
    elif ' га' in x:
        ix = x.index(' га')
        xx = x[:ix]
        if ' ' in xx:
            gx = xx.rindex(' ')
            xxx = xx[gx+1:]
            return xxx + '00'
        else:
            return 'NA'
    else:
        return 'NA'


data['size_house'] = data['Название'].apply(func=get_size_house).str.replace(',', '.').astype(dtype=float)
data['size_land'] = data['Название'].apply(func=get_size_land).str.replace(',', '.').astype(dtype=float)
data['price'] = data['Цена'].astype(dtype=float)

data = data[data['size_land'] <= 50]

binner = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile')

data['price_binned'] = binner.fit_transform(X=data[['price']]).flatten()


def get_price_labels(x):
    return '{0} -- {1}'.format(binner.bin_edges_[0][int(x)], binner.bin_edges_[0][int(x)+1])


# n_clus = 4
n_clus = 6
# clusterer = KMeans(n_clusters=n_clus)
# clusterer = HDBSCAN
clusterer = AgglomerativeClustering(n_clusters=n_clus, metric='euclidean', linkage='ward')
na_mask = data['l1l2'] == 'NA NA'
data.loc[~na_mask, 'clus'] = clusterer.fit_predict(X=data.loc[~na_mask, ['l1', 'l2']].dropna().values).flatten()
data.loc[na_mask, 'clus'] = -1


data['price_binned_labels'] = data['price_binned'].apply(func=get_price_labels)

# prices vs home & land size
"""
plot_by = 'price_binned_labels'
seaborn.scatterplot(
    data=data, x="size_house", y="size_land", hue=plot_by, size=plot_by,
    palette=seaborn.color_palette("viridis", len(binner.bin_edges_[0])),
    sizes=(20, 200), legend="full"
)

pyplot.scatter(271.8, 8.92, color='r')
"""

plot_by = 'price_binned_labels'
seaborn.scatterplot(
    data=data, x="size_house", y="size_land", hue='clus', size=plot_by,
    sizes=(20, 200), legend="full"
)

pyplot.scatter(271.8, 8.92, color='r')

# prices vs longitude & latitude
"""
plot_by = 'price_binned_labels'
seaborn.scatterplot(
    data=data, x="l1", y="l2", hue=plot_by, size=plot_by,
    palette=seaborn.color_palette("viridis", len(binner.bin_edges_[0])),
    sizes=(20, 200), legend="full"
)

pyplot.scatter(48.275769, 42.073634, color='r')
"""
"""
plot_by = 'price_binned_labels'
seaborn.scatterplot(
    data=data, x="l1", y="l2", hue='clus', size=plot_by,
    sizes=(20, 200), legend="full"
)

pyplot.scatter(48.275769, 42.073634, color='r')
"""