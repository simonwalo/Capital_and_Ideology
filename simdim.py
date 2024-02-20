
# debug: title of graph should inlude key name

# define similarity function for n dimensions
# cosine similarity between centers of word clouds

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import random
import matplotlib.lines as mlines




def simdim(models, keywords, key, *dims, rangelow=1850, rangehigh=2000, rangestep=10, stand=False):


    # check if all terms exist in all models
    for year, model in models.items():
        if year in range(rangelow, rangehigh, rangestep):
            for term in keywords[key]:
                if model[term].all() == models[1810]['biology'].all():
                    print('Keyword ', term, ' not available for ', year)
                    return
            for dim in dims:
                for term in keywords[dim]:
                    if model[term].all() == models[1810]['biology'].all():
                        print('Keyword ', term, ' not available for ', year)
                        return


    # get raw distances
    if stand == False:

        similarities = pd.DataFrame()

        for dim in dims:
            d = []
            for year, model in models.items():
                if year in range(rangelow, rangehigh, rangestep):
                    d.append(model.n_similarity(keywords[key], keywords[dim]))
            similarities[dim] = d

    # get standardized distances
    if stand == True:

        # get similarity between anchor and all words per year

        similarities = pd.DataFrame()

        fulltable = pd.DataFrame()

        for year, model in models.items():
            if year in range(rangelow, rangehigh, rangestep):
                allkeys = list(model.key_to_index.keys())
                templist = []

                for term in allkeys:
                    d = model.n_similarity(keywords[key], [term])
                    templist.append(d)

                data = pd.DataFrame()
                data.index = allkeys
                data[year] = templist

                fulltable = fulltable.merge(data, left_index=True, right_index=True, how='right')

        # standardize dataframe
        fulltablestand = (fulltable - fulltable.mean()) / fulltable.std()

        # calculate mean distance for each dim
        for dim in dims:
            # only keep values for relevant keys
            dimtable = fulltablestand[fulltablestand.index.isin(keywords[dim])]

            # calculate mean values per year
            similarities[dim] = dimtable.mean()


    # plot the trendline

    x = range(rangelow, rangehigh, rangestep)
    xnew = np.linspace(rangelow, (rangehigh - 10), 100)

    markslist = ['o', 's']
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







