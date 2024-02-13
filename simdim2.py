#### WHAT IS THIS??? ####


# debug: title of graph should inlude key name

# define similarity function for n dimensions
# average of cosine similarities between all word combinations from different lists

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import random




def simdim2(models, keywords, key, *dims, rangelow=1850, rangehigh=2000, rangestep=10, ci=95, bootstrap=1000):

    medians = pd.DataFrame()
    lower_cis = pd.DataFrame()
    upper_cis = pd.DataFrame()

    for dim in dims:
        data = pd.DataFrame(index=range(len(range(rangelow, rangehigh, rangestep))), columns=range(bootstrap))

        for i in range(bootstrap):

            sample1 = keywords[key]  # random.choices(keywords['work'], k=len(keywords['work']))
            sample2 = random.choices(keywords[dim], k=len(keywords[dim]))

            d = []
            for year, model in models.items():
                if year in range(rangelow, rangehigh, rangestep):
                    temp = []
                    for word1 in sample1:
                        for word2 in sample2:
                            temp.append(model.n_similarity([word1], [word2]))
                    d.append(sum(temp) / len(temp))
            d = np.asarray(d)
            data[i] = d

        # get medians
        temp = []
        for i in range(len(range(rangelow, rangehigh, rangestep))):
            sample = data.iloc[i]
            temp.append(sample.median())
        medians[dim] = temp

        # get 95% intervals
        alpha = 100 - ci

        # get lowers CIs
        temp = []
        for i in range(len(range(rangelow, rangehigh, rangestep))):
            sample = data.iloc[i]
            temp.append(np.percentile(sample, alpha / 2))
        lower_cis[dim] = temp

        # get upper CIs
        temp = []
        for i in range(len(range(rangelow, rangehigh, rangestep))):
            sample = data.iloc[i]
            temp.append(np.percentile(sample, 100 - alpha / 2))
        upper_cis[dim] = temp

    # the trendline

    x = range(rangelow, rangehigh, rangestep)
    xnew = np.linspace(rangelow, (rangehigh - 10), 100)

    n = len(dims)
    colors = iter(cm.rainbow(np.linspace(0, 1, n)))

    for dim in dims:
        y = medians[dim].tolist()
        fun = interp1d(x, y, kind='cubic')

        low = lower_cis[dim].tolist()
        fun_low = interp1d(x, low, kind='cubic')

        high = upper_cis[dim].tolist()
        fun_high = interp1d(x, high, kind='cubic')

        color = next(colors)
        plt.plot(xnew, fun(xnew), "-", color=color, label=dim)
        plt.plot(x, y, 'o', color=color)
        plt.fill_between(xnew, fun_low(xnew), fun_high(xnew), alpha=0.2)

    # show plot
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel("Year")
    plt.ylabel("Cosine Similarity")
    plt.xticks(range(1850, 2000, 20))
    plt.tight_layout()
    plt.show()
    plt.close()









