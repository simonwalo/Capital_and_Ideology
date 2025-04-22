#%% import packages

from functions.simdim import simdim
from gensim.models import KeyedVectors
import matplotlib.pyplot as plt

#%% load data

google = {
    1800: KeyedVectors.load('./data/Google/vectors1800.kv'),
    1810: KeyedVectors.load('./data/Google/vectors1810.kv'),
    1820: KeyedVectors.load('./data/Google/vectors1820.kv'),
    1830: KeyedVectors.load('./data/Google/vectors1830.kv'),
    1840: KeyedVectors.load('./data/Google/vectors1840.kv'),
    1850: KeyedVectors.load('./data/Google/vectors1850.kv'),
    1860: KeyedVectors.load('./data/Google/vectors1860.kv'),
    1870: KeyedVectors.load('./data/Google/vectors1870.kv'),
    1880: KeyedVectors.load('./data/Google/vectors1880.kv'),
    1890: KeyedVectors.load('./data/Google/vectors1890.kv'),
    1900: KeyedVectors.load('./data/Google/vectors1900.kv'),
    1910: KeyedVectors.load('./data/Google/vectors1910.kv'),
    1920: KeyedVectors.load('./data/Google/vectors1920.kv'),
    1930: KeyedVectors.load('./data/Google/vectors1930.kv'),
    1940: KeyedVectors.load('./data/Google/vectors1940.kv'),
    1950: KeyedVectors.load('./data/Google/vectors1950.kv'),
    1960: KeyedVectors.load('./data/Google/vectors1960.kv'),
    1970: KeyedVectors.load('./data/Google/vectors1970.kv'),
    1980: KeyedVectors.load('./data/Google/vectors1980.kv'),
    1990: KeyedVectors.load('./data/Google/vectors1990.kv')
}


coha = {
    1810: KeyedVectors.load('./data/COHA/vectors1810.kv'),
    1820: KeyedVectors.load('./data/COHA/vectors1820.kv'),
    1830: KeyedVectors.load('./data/COHA/vectors1830.kv'),
    1840: KeyedVectors.load('./data/COHA/vectors1840.kv'),
    1850: KeyedVectors.load('./data/COHA/vectors1850.kv'),
    1860: KeyedVectors.load('./data/COHA/vectors1860.kv'),
    1870: KeyedVectors.load('./data/COHA/vectors1870.kv'),
    1880: KeyedVectors.load('./data/COHA/vectors1880.kv'),
    1890: KeyedVectors.load('./data/COHA/vectors1890.kv'),
    1900: KeyedVectors.load('./data/COHA/vectors1900.kv'),
    1910: KeyedVectors.load('./data/COHA/vectors1910.kv'),
    1920: KeyedVectors.load('./data/COHA/vectors1920.kv'),
    1930: KeyedVectors.load('./data/COHA/vectors1930.kv'),
    1940: KeyedVectors.load('./data/COHA/vectors1940.kv'),
    1950: KeyedVectors.load('./data/COHA/vectors1950.kv'),
    1960: KeyedVectors.load('./data/COHA/vectors1960.kv'),
    1970: KeyedVectors.load('./data/COHA/vectors1970.kv'),
    1980: KeyedVectors.load('./data/COHA/vectors1980.kv'),
    1990: KeyedVectors.load('./data/COHA/vectors1990.kv'),
    2000: KeyedVectors.load('./data/COHA/vectors2000.kv')

}

googlefiction = {
    1800: KeyedVectors.load('./data/Google fiction/vectors1800.kv'),
    1810: KeyedVectors.load('./data/Google fiction/vectors1810.kv'),
    1820: KeyedVectors.load('./data/Google fiction/vectors1820.kv'),
    1830: KeyedVectors.load('./data/Google fiction/vectors1830.kv'),
    1840: KeyedVectors.load('./data/Google fiction/vectors1840.kv'),
    1850: KeyedVectors.load('./data/Google fiction/vectors1850.kv'),
    1860: KeyedVectors.load('./data/Google fiction/vectors1860.kv'),
    1870: KeyedVectors.load('./data/Google fiction/vectors1870.kv'),
    1880: KeyedVectors.load('./data/Google fiction/vectors1880.kv'),
    1890: KeyedVectors.load('./data/Google fiction/vectors1890.kv'),
    1900: KeyedVectors.load('./data/Google fiction/vectors1900.kv'),
    1910: KeyedVectors.load('./data/Google fiction/vectors1910.kv'),
    1920: KeyedVectors.load('./data/Google fiction/vectors1920.kv'),
    1930: KeyedVectors.load('./data/Google fiction/vectors1930.kv'),
    1940: KeyedVectors.load('./data/Google fiction/vectors1940.kv'),
    1950: KeyedVectors.load('./data/Google fiction/vectors1950.kv'),
    1960: KeyedVectors.load('./data/Google fiction/vectors1960.kv'),
    1970: KeyedVectors.load('./data/Google fiction/vectors1970.kv'),
    1980: KeyedVectors.load('./data/Google fiction/vectors1980.kv'),
    1990: KeyedVectors.load('./data/Google fiction/vectors1990.kv')
}

keywords = dict()


#%% (Neo-)Liberalism


keywords['econ'] = [
    "economy", "economic",
    "invest", "investment",
    "business", "businesses",
    "enterprise", "enterprises",
    "trade", "trades", "trading",
    "commerce", "commercial",
    "manufacture", "manufactures",
    "industry", "industries",
    "market", "markets",
    'corporation', 'corporations',
    'production'
]


keywords['Regulation'] = [
    "regulate", "regulated", "regulation", "regulations", "regulating",
    "intervene", "intervening", "intervention", "interventions",
    "restrict", "restriction", "restrictions", "restricting", "restricted",
    "prohibit", "prohibition", "prohibitions", "prohibiting", "prohibited",
    "control", "controlled", "controlling"
]

keywords['Liberalism'] = [
    "liberal", "liberalism",
    'liberty', "liberties",
    "free", "freedom",
    "unfettered",
    "faire", "laissez",
    "liberalize", "liberalization",
    'deregulate', 'deregulation', "deregulated",
    "open"
]


simdim.simdim(google, "Google", keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=False)
simdim.simdim(coha, "COHA", keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=False)



ax1 = simdim.simdim(google, keywords, "Google", 'econ', 'Liberalism', 'Regulation',
                    rangelow=1850, stand=True, display=False)
ax2 = simdim.simdim(coha, "COHA", keywords, 'econ', 'Liberalism', 'Regulation',
                    rangelow=1850, stand=True, display=False)

fig, (new_ax1, new_ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

line1 = ax1.get_lines()[0]  # Get the first line from ax1
new_ax1.plot(line1.get_xdata(), line1.get_ydata(), label='Liberalism', color='C0')
offsets1 = ax1.collections[0].get_offsets()
new_ax1.scatter(offsets1[:, 0], offsets1[:, 1], color='C0', marker="o")

line2 = ax1.get_lines()[1]  # Get the second line from ax1
new_ax1.plot(line2.get_xdata(), line2.get_ydata(), label='Regulation', color='C1')
offsets2 = ax1.collections[1].get_offsets()
new_ax1.scatter(offsets2[:, 0], offsets2[:, 1], color='C1', marker="D")

new_ax1.set_title('Google')
new_ax1.set_ylabel("Cosine Similarity (std)")
new_ax1.set_xticks(range(1850, 2000, 20))

line3 = ax2.get_lines()[0]  # Get the first line from ax2
new_ax2.plot(line3.get_xdata(), line3.get_ydata(), label='Liberalism', color='C0')
offsets3 = ax2.collections[0].get_offsets()
new_ax2.scatter(offsets3[:, 0], offsets3[:, 1], color='C0', marker="o")


line4 = ax2.get_lines()[1]  # Get the second line from ax2
new_ax2.plot(line4.get_xdata(), line4.get_ydata(), label='Regulation', color='C1')
offsets4 = ax2.collections[1].get_offsets()
new_ax2.scatter(offsets4[:, 0], offsets4[:, 1], color='C1', marker="D")

new_ax2.set_title('COHA')
new_ax2.set_xticks(range(1850, 2000, 20))
new_ax2.yaxis.set_tick_params(labelleft=True)

handles, labels = new_ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=2)

plt.savefig('./figures/neoliberalism.eps', format='eps')

plt.show()

#add legend symbols manually!

#extra: google books fiction
simdim.simdim(googlefiction, "Google Fiction", keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=True)
plt.savefig('./figures/neoliberalism_googlefiction.eps', format='eps')
plt.show()


#%% Meritocracy


keywords['Work'] = [
    "work", "works", "worked", "working",
    "job", "jobs",
    "career", "careers",
    "employment", "employed",
    "labor", "labors", 'labour', 'labours',
]

keywords['rich'] = [
    "wealth", "wealthy",
    "rich", "riches",
    "affluence", "affluent",
    "opulent", "opulence",
    'luxury', 'luxurious',
    'prosperity', 'prosperous'
]

keywords['poor'] = [
    "poor", 'poorer', 'poorest',
    "poverty", "impoverished",
    'indigent', 'necessitous',
    "destitute", "needy"
]

keywords['Affluence'] = keywords['rich'] + keywords['poor']


keywords['Inheritance'] = [
    'inherit', 'inherited', 'inheritance', 'heir', 'heirs',
    'inheritor', 'inheritors', 'hereditary', 'heritage',
    'family', 'families',
    'father', 'fathers',
    'mother', 'mothers',
    'son', 'sons', 'daughter', 'daughters',
    'descendent', 'descendents',
    'ancestor', 'ancestors'
]



simdim.simdim(google, "Googke", keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=False)
simdim.simdim(coha, "Google", keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=False)

ax1 = simdim.simdim(google, "Google", keywords, 'Affluence', 'merit', 'Inheritance',
                    rangelow=1850, stand=True, display=False)
ax2 = simdim.simdim(coha, "COHA", keywords, 'Affluence',  'merit', 'Inheritance',
                    rangelow=1850, stand=True, display=False)


fig, (new_ax1, new_ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

line1 = ax1.get_lines()[0]  # Get the first line from ax1
new_ax1.plot(line1.get_xdata(), line1.get_ydata(), label='Work', color='C0')
offsets1 = ax1.collections[0].get_offsets()
new_ax1.scatter(offsets1[:, 0], offsets1[:, 1], color='C0', marker="o")

line2 = ax1.get_lines()[1]  # Get the second line from ax1
new_ax1.plot(line2.get_xdata(), line2.get_ydata(), label='Inheritance', color='C1')
offsets2 = ax1.collections[1].get_offsets()
new_ax1.scatter(offsets2[:, 0], offsets2[:, 1], color='C1', marker="D")

new_ax1.set_title('Google')
new_ax1.set_ylabel("Cosine Similarity (std)")
new_ax1.set_xticks(range(1850, 2000, 20))

line3 = ax2.get_lines()[0]  # Get the first line from ax2
new_ax2.plot(line3.get_xdata(), line3.get_ydata(), label='Work', color='C0')
offsets3 = ax2.collections[0].get_offsets()
new_ax2.scatter(offsets3[:, 0], offsets3[:, 1], color='C0', marker="o")


line4 = ax2.get_lines()[1]  # Get the second line from ax2
new_ax2.plot(line4.get_xdata(), line4.get_ydata(), label='Inheritance', color='C1')
offsets4 = ax2.collections[1].get_offsets()
new_ax2.scatter(offsets4[:, 0], offsets4[:, 1], color='C1', marker="D")

new_ax2.set_title('COHA')
new_ax2.set_xticks(range(1850, 2000, 20))
new_ax2.yaxis.set_tick_params(labelleft=True)

handles, labels = new_ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=2)

plt.savefig('meritocracy.eps', format='eps')

plt.show()

#add legend symbols manually!


#extra: google books fiction
simdim.simdim(googlefiction, keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=True)
plt.savefig('./figures/meritocracy_googlefiction.eps', format='eps')
plt.show()


#%% Intrinsic vs. Extrinsic Work Motivation


keywords['work'] = [
    "work", "works", "worked", "working",
    "job", "jobs",
    "career", "careers",
    "employment", "employed",
    "labor", "labors", 'labour', 'labours'
]

keywords['Extrinsic'] = [
    "earn", "earning", "earnings",
    "money",
    "wage", "wages",
    "salary", 'salaries',
    "income", 'incomes',
    "remuneration",
    "pay", 'pays', 'paying', 'payment',
    'compensation', 'compensations'
]


keywords['Intrinsic'] = [
    "interesting", "interest", "interested",
    "fulfilling", "fulfill", "fulfilled",
    "stimulate", "stimulating", "stimulation",
    "satisfy", "satisfying", "satisfied", 'satisfaction',
    "expression", "express", "expressive",
    'meaning', 'meaningful'
]


simdim.simdim(google, "Google", keywords, 'work', 'alienation', 'Intrinsic', rangelow=1850, stand=False)
simdim.simdim(coha, "COHA", keywords, 'work', 'alienation', 'Intrinsic', rangelow=1850, stand=False)


ax1 = simdim.simdim(google, "Google", keywords, 'work', 'alienation', 'Intrinsic',
                    rangelow=1850, stand=True, display=False)
ax2 = simdim.simdim(coha, "COHA", keywords, 'work', 'alienation', 'Intrinsic',
                    rangelow=1850, stand=True, display=False)

fig, (new_ax1, new_ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

line1 = ax1.get_lines()[0]  # Get the first line from ax1
new_ax1.plot(line1.get_xdata(), line1.get_ydata(), label='Extrinsic', color='C0')
offsets1 = ax1.collections[0].get_offsets()
new_ax1.scatter(offsets1[:, 0], offsets1[:, 1], color='C0', marker="o")

line2 = ax1.get_lines()[1]  # Get the second line from ax1
new_ax1.plot(line2.get_xdata(), line2.get_ydata(), label='Intrinsic', color='C1')
offsets2 = ax1.collections[1].get_offsets()
new_ax1.scatter(offsets2[:, 0], offsets2[:, 1], color='C1', marker="D")

new_ax1.set_title('Google')
new_ax1.set_ylabel("Cosine Similarity (std)")
new_ax1.set_xticks(range(1850, 2000, 20))

line3 = ax2.get_lines()[0]  # Get the first line from ax2
new_ax2.plot(line3.get_xdata(), line3.get_ydata(), label='Extrinsic', color='C0')
offsets3 = ax2.collections[0].get_offsets()
new_ax2.scatter(offsets3[:, 0], offsets3[:, 1], color='C0', marker="o")


line4 = ax2.get_lines()[1]  # Get the second line from ax2
new_ax2.plot(line4.get_xdata(), line4.get_ydata(), label='Intrinsic', color='C1')
offsets4 = ax2.collections[1].get_offsets()
new_ax2.scatter(offsets4[:, 0], offsets4[:, 1], color='C1', marker="D")

new_ax2.set_title('COHA')
new_ax2.set_xticks(range(1850, 2000, 20))
new_ax2.yaxis.set_tick_params(labelleft=True)

handles, labels = new_ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=2)

plt.savefig('figure 3.eps', format='eps')

plt.show()

#add legend symbols manually!

#extra: google books fiction
simdim.simdim(googlefiction, keywords, 'work', 'Extrinsic', 'Intrinsic', rangelow=1850, stand=True)
plt.savefig('./figures/meaningofwork_googlefiction.eps', format='eps')
plt.show()
