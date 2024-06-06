
# define similarity function for n dimensions
# cosine similarity between centers of word clouds

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.lines as mlines
from collections import Counter




def simdim(models, keywords, key, *dims, rangelow=1850, rangehigh=2000, rangestep=10, stand=False):


    # use only terms that exist in all models

    cleankeydict = dict()
    cleankeydict[key] = []
    for dim in dims:
        cleankeydict[dim] = []

    for year, model in models.items():
        if year in range(rangelow, rangehigh, rangestep):
            for term in keywords[key]:
                if term not in model:
                    print('Keyword ', term, ' not available for ', year)
                elif model[term].all() == models[1810]['biology'].all():
                    print('Keyword ', term, ' not available for ', year)
                else:
                    cleankeydict[key].append(term)
            for dim in dims:
                for term in keywords[dim]:
                    if term not in model:
                        print('Keyword ', term, ' not available for ', year)
                    elif model[term].all() == models[1810]['biology'].all():
                        print('Keyword ', term, ' not available for ', year)
                    else:
                        cleankeydict[dim].append(term)

    countskey = Counter(cleankeydict[key])
    cleankeydict[key] = [elem for elem, count in countskey.items() if count == len(range(rangelow, rangehigh, rangestep))]
    print(key, ':', cleankeydict[key])
    for dim in dims:
        countsdim = Counter(cleankeydict[dim])
        cleankeydict[dim] = [elem for elem, count in countsdim.items() if
                             count == len(range(rangelow, rangehigh, rangestep))]
        print(dim, ':', cleankeydict[dim])

    # get raw distances
    if stand == False:

        similarities = pd.DataFrame()

        for dim in dims:
            d = []
            for year, model in models.items():
                if year in range(rangelow, rangehigh, rangestep):
                    d.append(model.n_similarity(cleankeydict[key], cleankeydict[dim]))
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
                    d = model.n_similarity(cleankeydict[key], [term])
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
            dimtable = fulltablestand[fulltablestand.index.isin(cleankeydict[dim])]

            # calculate mean values per year
            similarities[dim] = dimtable.mean()


    # plot the trendline

    x = range(rangelow, rangehigh, rangestep)
    xnew = np.linspace(rangelow, (rangehigh - 10), 100)

    markslist = ['o', 's', 'x']
    marks = iter(markslist)

    fig, ax = plt.subplots()

    for dim in dims:
        y = similarities[dim].tolist()
        fun = interp1d(x, y, kind='cubic')
        ax.plot(xnew, fun(xnew), "-", color='black')
        ax.scatter(x, y, marker=next(marks), color='black')

    # add legend and labels
    if len(dims) == 1:
        legend1 = mlines.Line2D([], [], color='black', marker='o', label=dims[0])
        ax.legend(handles=[legend1], loc='center left', bbox_to_anchor=(1, 0.5))

    if len(dims) == 2:
        legend1 = mlines.Line2D([], [], color='black', marker='o', label=dims[0])
        legend2 = mlines.Line2D([], [], color='black', marker='s', label=dims[1])
        ax.legend(handles=[legend1, legend2], loc='center left', bbox_to_anchor=(1, 0.5))

    if len(dims) == 3:
        legend1 = mlines.Line2D([], [], color='black', marker='o', label=dims[0])
        legend2 = mlines.Line2D([], [], color='black', marker='s', label=dims[1])
        legend3 = mlines.Line2D([], [], color='black', marker='x', label=dims[2])

        ax.legend(handles=[legend1, legend2, legend3], loc='center left', bbox_to_anchor=(1, 0.5))

    if 1800 in models:
        plt.suptitle('Google')
    if 2000 in models:
        plt.suptitle('COHA')
    ax.set_xlabel("Year")
    ax.set_ylabel("Cosine Similarity (std)")
    ax.set_xticks(range(rangelow, rangehigh, 20))
    #plt.tight_layout()

    # show plot
    #plt.show()
    #plt.close()

    return ax









