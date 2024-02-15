### this function plots the cosine similarity between an anchor and different dimensions ###
### it is similar to the original simdim function but includes the following changes:
# - removed option for CIs (because meaningless)
# - plot can include one, two or three dimensions

# to do:
# - relative measures of similarity instead of absolute ones (see review)
# - check first if all terms exist in all embeddings




import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.lines as mlines


# basics


#get similarity between anchor and all words per year

fulltable = pd.DataFrame()

for year, model in models_all.items():
    if year in range(1850, 2000, 10):
        allkeys = list(model.key_to_index.keys())
        templist = []

        for key in allkeys:
            d = model.n_similarity(keywords['work'], [key])
            templist.append(d)

        data = pd.DataFrame()
        data.index = allkeys
        data[year] = templist

        fulltable = fulltable.merge(data, left_index=True, right_index=True, how='right')

#standardize dataframe
fulltablestand = (fulltable-fulltable.mean())/fulltable.std()

# only keep values for relevant keys
fulltablestand = fulltablestand[fulltablestand.index.isin(keywords['Morality'])]

# calculate mean values per year
mean_values = fulltablestand.mean()
mean_values
















# function

def simdimnew(models, keywords, key, *dims, rangelow=1850, rangehigh=2000, rangestep=10):

    similarities = pd.DataFrame()

    for dim in dims:
        d = []
        for year, model in models.items():
            if year in range(rangelow, rangehigh, rangestep):
                d.append(model.n_similarity(keywords[key], keywords[dim]))
        similarities[dim] = d


    # plot the trendline

    x = range(rangelow, rangehigh, rangestep)
    xnew = np.linspace(rangelow, (rangehigh - 10), 100)

    n = len(dims)
    markslist = ['o', 's', 'x']
    marks = iter(markslist)

    for dim in dims:
        y = similarities[dim].tolist()
        fun = interp1d(x, y, kind='cubic')
        plt.plot(xnew, fun(xnew), "-", x, y, next(marks), color='black')


    # add legend and labels
    if len(dims) == 1:
        legend1 = mlines.Line2D([], [], color='black', marker='o', label=dims[0])
        plt.legend(handles=[legend1], loc='center left', bbox_to_anchor=(1, 0.5))

    if len(dims) == 2:
        legend1 = mlines.Line2D([], [], color='black', marker='o', label=dims[0])
        legend2 = mlines.Line2D([], [], color='black', marker='s', label=dims[1])
        plt.legend(handles=[legend1, legend2], loc='center left', bbox_to_anchor=(1, 0.5))

    if len(dims) == 3:
        legend1 = mlines.Line2D([], [], color='black', marker='o', label=dims[0])
        legend2 = mlines.Line2D([], [], color='black', marker='s', label=dims[1])
        legend3 = mlines.Line2D([], [], color='black', marker='x', label=dims[2])

        plt.legend(handles=[legend1, legend2, legend3], loc='center left', bbox_to_anchor=(1, 0.5))

    plt.xlabel("Year")
    plt.ylabel("Cosine Similarity")
    plt.xticks(range(rangelow, rangehigh, 20))
    plt.tight_layout()

    # show plot
    plt.show()
    plt.close()










