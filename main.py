#%% import packages

import semchange
import simdim
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

keywords = dict()

#%%  most similar terms by decade

for x, y in google.items():
    print(x)
    print(y.most_similar("gdp"))


#%% visualize semantic change over time (PCA with keyword as passive projection)

semchange.semchange(google, "work", rangelow=1810, rangehigh=2000, rangestep=60, export=False)



#%% (Neo-)Liberalism


keywords['econ'] = [
    "profit", "profitable", "cost", "benefit", "sell", "revenue", "gain",
    "loss", "capital", "invest", "economic", "price", "business", "money", "trade",
    "pay", "paid"
]

keywords['econ'] = [
    "economy", "invest", "economic", "business", "money", "trade"
]


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
    "regulate", "regulated", "regulation", "regulations", #sinkt
    "intervene", "intervention", "interventions", #steigt
    "govern", "government", "governments", #steigt
    "restrict", "restriction", "restrictions", #sinkt
    "prohibit", "prohibition", #sinkt
    "control", "controlled" #sinkt
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

#discarded:

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['Liberalism']))




simdim.simdim(google, keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=False)



ax1 = simdim.simdim(google, keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=True)
ax2 = simdim.simdim(coha, keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=True)

fig, (new_ax1, new_ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

line1 = ax1.get_lines()[0]  # Get the first line from ax1
new_ax1.plot(line1.get_xdata(), line1.get_ydata(), label='Liberalism', color='C0')
offsets1 = ax1.collections[0].get_offsets()
new_ax1.scatter(offsets1[:, 0], offsets1[:, 1], color='C0')

line2 = ax1.get_lines()[1]  # Get the second line from ax1
new_ax1.plot(line2.get_xdata(), line2.get_ydata(), label='Regulation', color='C1')
offsets2 = ax1.collections[1].get_offsets()
new_ax1.scatter(offsets2[:, 0], offsets2[:, 1], color='C1')

new_ax1.set_title('Google')
new_ax1.set_ylabel("Cosine Similarity (std)")
new_ax1.set_xticks(range(1850, 2000, 20))

line3 = ax2.get_lines()[0]  # Get the first line from ax2
new_ax2.plot(line3.get_xdata(), line3.get_ydata(), label='Liberalism', color='C0')
offsets3 = ax2.collections[0].get_offsets()
new_ax2.scatter(offsets3[:, 0], offsets3[:, 1], color='C0')


line4 = ax2.get_lines()[1]  # Get the second line from ax2
new_ax2.plot(line4.get_xdata(), line4.get_ydata(), label='Regulation', color='C1')
offsets4 = ax2.collections[1].get_offsets()
new_ax2.scatter(offsets4[:, 0], offsets4[:, 1], color='C1')

new_ax2.set_title('COHA')
new_ax2.set_xticks(range(1850, 2000, 20))
new_ax2.yaxis.set_tick_params(labelleft=True)

handles, labels = new_ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=2)

plt.show()





#%% Meritocracy


keywords['Work'] = [
    "work", "works", "worked", "working",
    "job", "jobs",
    "career", "careers",
    "employment", "employed",
    "labor", "labors", 'labour', 'labours'
]

# discarded:
#"profession", "professions", "professional",
#"occupation", "occupations",

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


keywords['merit'] = [
    'merit', 'merits', 'merited', # nimmt ab, coha zu
    'deserve', 'deserved', 'deserves', 'deserving', # nimmt zu
    'just', 'justice', 'justly', #nimmt zu
    "effort", # nimmt leicht zu
    'perform', 'performance', # leichte zunahme, coha abnahme
    'reward', 'rewards', 'rewarded' #google abnahme, coha zunahme
    'accomplish', 'accomplishment',  # leichte zunahme, coha zunahme
    'achieve', 'achievement', # konstant, coha abnahme
]
#discarded:
# 'fair', 'fairness' (polysemy)
#
# 'talent', 'talents',  # zunahme, coha abnahme
# 'skill', 'skills',  # konstant, coha abnahme
# 'able', 'ability', 'abilities'  # konstant, coha abnahme
#


keywords['luck'] = [
    'luck', 'lucky', 'unlucky'
    'chance', 'chances',
    'fortunate', 'unfortunate'
]

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



keywords['luckinherit'] = keywords['luck'] + keywords['inherit']

# find related terms
for year, model in google.items():
    print(year, model.most_similar(positive=keywords['Inheritance']))

for year, model in google.items():
    print(year, model.most_similar(positive=['Inheritance']))


simdim.simdim(google, keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=False)

ax1 = simdim.simdim(google, keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=True)
ax2 = simdim.simdim(coha, keywords, 'Affluence',  'Work', 'Inheritance', rangelow=1850, stand=True)


fig, (new_ax1, new_ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

line1 = ax1.get_lines()[0]  # Get the first line from ax1
new_ax1.plot(line1.get_xdata(), line1.get_ydata(), label='Work', color='C0')
offsets1 = ax1.collections[0].get_offsets()
new_ax1.scatter(offsets1[:, 0], offsets1[:, 1], color='C0')

line2 = ax1.get_lines()[1]  # Get the second line from ax1
new_ax1.plot(line2.get_xdata(), line2.get_ydata(), label='Inheritance', color='C1')
offsets2 = ax1.collections[1].get_offsets()
new_ax1.scatter(offsets2[:, 0], offsets2[:, 1], color='C1')

new_ax1.set_title('Google')
new_ax1.set_ylabel("Cosine Similarity (std)")
new_ax1.set_xticks(range(1850, 2000, 20))

line3 = ax2.get_lines()[0]  # Get the first line from ax2
new_ax2.plot(line3.get_xdata(), line3.get_ydata(), label='Work', color='C0')
offsets3 = ax2.collections[0].get_offsets()
new_ax2.scatter(offsets3[:, 0], offsets3[:, 1], color='C0')


line4 = ax2.get_lines()[1]  # Get the second line from ax2
new_ax2.plot(line4.get_xdata(), line4.get_ydata(), label='Inheritance', color='C1')
offsets4 = ax2.collections[1].get_offsets()
new_ax2.scatter(offsets4[:, 0], offsets4[:, 1], color='C1')

new_ax2.set_title('COHA')
new_ax2.set_xticks(range(1850, 2000, 20))
new_ax2.yaxis.set_tick_params(labelleft=True)

handles, labels = new_ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=2)

plt.show()







#%% Intrinsic vs. Extrinsic Work Motivation


keywords['work'] = [
    "work", "works", "worked", "working",
    "job", "jobs",
    "career", "careers",
    "employment", "employed",
    "labor", "labors", 'labour', 'labours'
]

#discarded:
# "profession", "professions", "professional",
#     "occupation", "occupations",

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

# temp discard:
#"meaningless"
 #   "useful", "useless",
#    "boring", "bore", "bored"

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['work']))

for  year, model in coha.items():
    print(year, model.most_similar(positive=['wage', 'salary']))

simdim.simdim(google, keywords, 'work', 'Extrinsic', 'Intrinsic', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'work', 'Extrinsic', 'Intrinsic', rangelow=1850, stand=False)

ax1 = simdim.simdim(google, keywords, 'work', 'Extrinsic', 'Intrinsic', rangelow=1850, stand=True)
ax2 = simdim.simdim(coha, keywords, 'work', 'Extrinsic', 'Intrinsic', rangelow=1850, stand=True)

fig, (new_ax1, new_ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

line1 = ax1.get_lines()[0]  # Get the first line from ax1
new_ax1.plot(line1.get_xdata(), line1.get_ydata(), label='Extrinsic', color='C0')
offsets1 = ax1.collections[0].get_offsets()
new_ax1.scatter(offsets1[:, 0], offsets1[:, 1], color='C0')

line2 = ax1.get_lines()[1]  # Get the second line from ax1
new_ax1.plot(line2.get_xdata(), line2.get_ydata(), label='Intrinsic', color='C1')
offsets2 = ax1.collections[1].get_offsets()
new_ax1.scatter(offsets2[:, 0], offsets2[:, 1], color='C1')

new_ax1.set_title('Google')
new_ax1.set_ylabel("Cosine Similarity (std)")
new_ax1.set_xticks(range(1850, 2000, 20))

line3 = ax2.get_lines()[0]  # Get the first line from ax2
new_ax2.plot(line3.get_xdata(), line3.get_ydata(), label='Extrinsic', color='C0')
offsets3 = ax2.collections[0].get_offsets()
new_ax2.scatter(offsets3[:, 0], offsets3[:, 1], color='C0')


line4 = ax2.get_lines()[1]  # Get the second line from ax2
new_ax2.plot(line4.get_xdata(), line4.get_ydata(), label='Intrinsic', color='C1')
offsets4 = ax2.collections[1].get_offsets()
new_ax2.scatter(offsets4[:, 0], offsets4[:, 1], color='C1')

new_ax2.set_title('COHA')
new_ax2.set_xticks(range(1850, 2000, 20))
new_ax2.yaxis.set_tick_params(labelleft=True)

handles, labels = new_ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', ncol=2)

plt.show()
















#%% Economization

### Economic code ###
keywords['Economic code'] = [
    "profit", "profitable", "cost", "benefit", "sell", "revenue", "gain",
    "loss", "capital", "invest", 'economy', "economic", "price", "business", "money", "trade",
    "pay", "paid", "market", 'markets'
]
#discarded: "maximize", "asset"


### Politics ###

#Political system
keywords['Politics'] = [
    "politics", "political", "policy", "legislative", "legislation", "government", "state"
]

#Political code
keywords['Political code'] = [
    "power", "rule", "influence", "law", "laws", "authority", "sovereign", "control", "command"
]


simdim.simdim(google, keywords, 'Politics', 'Political code', 'Economic code', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'Politics', 'Political code', 'Economic code', rangelow=1850, stand=False)

ax1 = simdim.simdim(google, keywords, 'Politics', 'Political code', 'Economic code', rangelow=1850, stand=True)
ax2 = simdim.simdim(coha, keywords, 'Politics', 'Political code', 'Economic code', rangelow=1850, stand=True)

fig = plt.figure(figsize=(13, 20), layout='constrained')
(subfig1, subfig2, subfig3, subfig4) = fig.subfigures(4, 1) # create 4x1 subfigures
(new_ax1, new_ax2) = subfig1.subplots(1, 2, sharey=True)
(new_ax3, new_ax4) = subfig2.subplots(1, 2, sharey=True)
(new_ax5, new_ax6) = subfig3.subplots(1, 2, sharey=True)
(new_ax7, new_ax8) = subfig4.subplots(1, 2, sharey=True)


line1 = ax1.get_lines()[0]  # Get the first line from ax1
new_ax1.plot(line1.get_xdata(), line1.get_ydata(), label='Internal code', color='C0')
offsets1 = ax1.collections[0].get_offsets()
new_ax1.scatter(offsets1[:, 0], offsets1[:, 1], color='C0')

line2 = ax1.get_lines()[1]  # Get the second line from ax1
new_ax1.plot(line2.get_xdata(), line2.get_ydata(), label='Economic code', color='C1')
offsets2 = ax1.collections[1].get_offsets()
new_ax1.scatter(offsets2[:, 0], offsets2[:, 1], color='C1')

new_ax1.set_title('Google')
new_ax1.set_ylabel("Cosine Similarity (std)")
new_ax1.set_xticks(range(1850, 2000, 20))

line3 = ax2.get_lines()[0]  # Get the first line from ax2
new_ax2.plot(line3.get_xdata(), line3.get_ydata(), color='C0')
offsets3 = ax2.collections[0].get_offsets()
new_ax2.scatter(offsets3[:, 0], offsets3[:, 1], color='C0')


line4 = ax2.get_lines()[1]  # Get the second line from ax2
new_ax2.plot(line4.get_xdata(), line4.get_ydata(), color='C1')
offsets4 = ax2.collections[1].get_offsets()
new_ax2.scatter(offsets4[:, 0], offsets4[:, 1], color='C1')

new_ax2.set_title('COHA')
new_ax2.set_xticks(range(1850, 2000, 20))
new_ax2.yaxis.set_tick_params(labelleft=True)



### education ###

#educational system
keywords['Education'] = [
    "education", "educate",
    "school", 'schools',
    "teach", 'teaching', 'teacher', 'teacher',
    "university", 'universities',
    'college', 'colleges',
    'gymnasium',
    'student', 'students'
]

#educational code
keywords['Educational code'] = [
    "study", "learn", "development", "develop", "skill", "critical", "thinking", "think", "growth", "empower"
]
#discarded because of data: "skills"
# discarded because of theory: "equal", "equality", "dignity", "curious", "curiosity", "stimulate", "stimulating"



# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['Education']))

simdim.simdim(google, keywords, 'Education', 'Educational code', 'Economic code', rangelow=1850)
simdim.simdim(coha, keywords, 'Education', 'Educational code', 'Economic code', rangelow=1850)

ax3 = simdim.simdim(google, keywords, 'Education', 'Educational code', 'Economic code', rangelow=1850, stand=True)
ax4 = simdim.simdim(coha, keywords, 'Education', 'Educational code', 'Economic code', rangelow=1850, stand = True)


line1 = ax3.get_lines()[0]  # Get the first line from ax3
new_ax3.plot(line1.get_xdata(), line1.get_ydata(), label='Internal code', color='C0')
offsets1 = ax3.collections[0].get_offsets()
new_ax3.scatter(offsets1[:, 0], offsets1[:, 1], color='C0')

line2 = ax3.get_lines()[1]  # Get the second line from ax3
new_ax3.plot(line2.get_xdata(), line2.get_ydata(), label='Economic code', color='C1')
offsets2 = ax3.collections[1].get_offsets()
new_ax3.scatter(offsets2[:, 0], offsets2[:, 1], color='C1')

new_ax3.set_title('Google')
new_ax3.set_ylabel("Cosine Similarity (std)")
new_ax3.set_xticks(range(1850, 2000, 20))

line3 = ax4.get_lines()[0]  # Get the first line from ax4
new_ax4.plot(line3.get_xdata(), line3.get_ydata(), color='C0')
offsets3 = ax4.collections[0].get_offsets()
new_ax4.scatter(offsets3[:, 0], offsets3[:, 1], color='C0')


line4 = ax4.get_lines()[1]  # Get the second line from ax4
new_ax4.plot(line4.get_xdata(), line4.get_ydata(), color='C1')
offsets4 = ax4.collections[1].get_offsets()
new_ax4.scatter(offsets4[:, 0], offsets4[:, 1], color='C1')

new_ax4.set_title('COHA')
new_ax4.set_xticks(range(1850, 2000, 20))
new_ax4.yaxis.set_tick_params(labelleft=True)


### health ###

#health system
keywords['medicine'] = [
    "medicine", "medical",
    "hospital", "hospitals",
    "doctor", "doctors", "physician", "physicians",
    "clinic", "clinics",
    "nurse", 'nurses'
]

#health code
keywords['Healthcare code'] = [
    "health", "healthy", "welfare", "provision", "provide", "care", "treat",
    "treatment", "sick", "sickness", "disease", "diagnose", "therapy"
]


# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['medicine']))

simdim.simdim(google, keywords, 'medicine', 'Healthcare code', 'Economic code', rangelow=1850)
simdim.simdim(coha, keywords, 'medicine', 'Healthcare code', 'Economic code', rangelow=1850)

ax5 = simdim.simdim(google, keywords, 'medicine', 'Healthcare code', 'Economic code', rangelow=1850, stand=True)
ax6 = simdim.simdim(coha, keywords, 'medicine', 'Healthcare code', 'Economic code', rangelow=1850, stand=True)


line1 = ax5.get_lines()[0]  # Get the first line from ax3
new_ax5.plot(line1.get_xdata(), line1.get_ydata(), label='Internal code', color='C0')
offsets1 = ax5.collections[0].get_offsets()
new_ax5.scatter(offsets1[:, 0], offsets1[:, 1], color='C0')

line2 = ax5.get_lines()[1]  # Get the second line from ax3
new_ax5.plot(line2.get_xdata(), line2.get_ydata(), label='Economic code', color='C1')
offsets2 = ax5.collections[1].get_offsets()
new_ax5.scatter(offsets2[:, 0], offsets2[:, 1], color='C1')

new_ax5.set_title('Google')
new_ax5.set_ylabel("Cosine Similarity (std)")
new_ax5.set_xticks(range(1850, 2000, 20))

line3 = ax6.get_lines()[0]  # Get the first line from ax4
new_ax6.plot(line3.get_xdata(), line3.get_ydata(), color='C0')
offsets3 = ax6.collections[0].get_offsets()
new_ax6.scatter(offsets3[:, 0], offsets3[:, 1], color='C0')


line4 = ax6.get_lines()[1]  # Get the second line from ax4
new_ax6.plot(line4.get_xdata(), line4.get_ydata(), color='C1')
offsets4 = ax6.collections[1].get_offsets()
new_ax6.scatter(offsets4[:, 0], offsets4[:, 1], color='C1')

new_ax6.set_title('COHA')
new_ax6.set_xticks(range(1850, 2000, 20))
new_ax6.yaxis.set_tick_params(labelleft=True)


### science ###

#science system
keywords['science'] = [
    "science", "sciences", "scientific", "university", "research", "study", "studies",
    "physics", "mathematics", "institute", "psychology", "philosophy",
    'humanities', 'sociology'
]
#discarded:



#science code
keywords['Scientific code'] = [
    "truth", "true", "untrue", "knowledge", "collective", "discover", "discovery",
    "understand", "understanding", 'comprehend', 'meaning', 'reason',
    "explain", "explanation", "method", "methodical"
]

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['Scientific code']))

simdim.simdim(google, keywords, 'science', 'Scientific code', 'Economic code', rangelow=1850)
simdim.simdim(coha, keywords, 'science', 'Scientific code', 'Economic code', rangelow=1850)

ax7 = simdim.simdim(google, keywords, 'science', 'Scientific code', 'Economic code', rangelow=1850, stand=True)
ax8 = simdim.simdim(coha, keywords, 'science', 'Scientific code', 'Economic code', rangelow=1850, stand=True)


line1 = ax7.get_lines()[0]  # Get the first line from ax3
new_ax7.plot(line1.get_xdata(), line1.get_ydata(), label='Internal code', color='C0')
offsets1 = ax7.collections[0].get_offsets()
new_ax7.scatter(offsets1[:, 0], offsets1[:, 1], color='C0')

line2 = ax7.get_lines()[1]  # Get the second line from ax3
new_ax7.plot(line2.get_xdata(), line2.get_ydata(), label='Economic code', color='C1')
offsets2 = ax7.collections[1].get_offsets()
new_ax7.scatter(offsets2[:, 0], offsets2[:, 1], color='C1')

new_ax7.set_title('Google')
new_ax7.set_ylabel("Cosine Similarity (std)")
new_ax7.set_xticks(range(1850, 2000, 20))

line3 = ax8.get_lines()[0]  # Get the first line from ax4
new_ax8.plot(line3.get_xdata(), line3.get_ydata(), color='C0')
offsets3 = ax8.collections[0].get_offsets()
new_ax8.scatter(offsets3[:, 0], offsets3[:, 1], color='C0')


line4 = ax8.get_lines()[1]  # Get the second line from ax4
new_ax8.plot(line4.get_xdata(), line4.get_ydata(), color='C1')
offsets4 = ax8.collections[1].get_offsets()
new_ax8.scatter(offsets4[:, 0], offsets4[:, 1], color='C1')

new_ax8.set_title('COHA')
new_ax8.set_xticks(range(1850, 2000, 20))
new_ax8.yaxis.set_tick_params(labelleft=True)





# create graph final

handles, labels = new_ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='outside center right', ncol=1)

subfig1.suptitle('Political System',fontweight='bold')
subfig2.suptitle('Educational System',fontweight='bold')
subfig3.suptitle('Healthcare System',fontweight='bold')
subfig4.suptitle('Scientific System',fontweight='bold')


plt.show()









#%% Protestant Ethic


keywords['work'] = [
    "work", "works", "worked", "working",
    "job", "jobs",
    "career", "careers",
    "employment", "employed",
    "labor", "labors", 'labour', 'labours'
]

# discarded:
#"profession", "professions", "professional",
#"occupation", "occupations",

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


keywords['Religion'] = [
    "redemption", "salvation", "god", "religion", "holy", "calling", "faith", "pious",
    "spiritual", "sacred", "divine", "belief", "worship"
]




keywords['Morality'] = [
    'good', 'bad',
    'moral', 'immoral', "morality",
    'honest', 'dishonest', "honesty",
    'virtuous', 'virtue', 'vice',
    'sinful', "sin",
    'evil',
    "decent", "decency",
    "noble",
    "honour", "honourable"
    "integrity",
    "dignity"
]

# find related terms
for year, model in google.items():
    print(year, model.most_similar(positive=keywords['poor']))

for year, model in coha.items():
    print(year, model.most_similar(positive=['poor', 'poverty']))


simdim.simdim(google, keywords, 'work', 'Morality', 'Affluence', 'Religion', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'work', 'Morality', 'Affluence', 'Religion', rangelow=1850, stand=False)

simdim.simdim(google, keywords, 'work', 'Morality', 'Affluence', 'Religion', rangelow=1850, stand=True)
simdim.simdim(coha, keywords, 'work', 'Morality', 'Affluence', 'Religion', rangelow=1850, stand=True)



# tests:

keywords['identity'] = [
    "identity", "fulfilling", "expression", "express"
]

#simdim.simdim(models_all, keywords, 'work', 'rich', 'poor', ci=0)
#simdim.simdim(models_all, keywords, 'work', 'moralpos', 'moralneg', ci=0)

#simdim.simdim(models_all, keywords, 'work', 'identity', 'Religion', ci=0)






#%% Economy: privat profits vs. social benefits


keywords['econ'] = [
    "economy", "invest", "economic", "business", "money", "trade"
]

keywords['private'] = [
    "private", "profit", "profits", "gain", "money", "revenue", "earn", "income"
]

keywords['public'] = [
    "social", "benefit", "benefits", "welfare", "society",
    "community", "public", "wellbeing"
]

simdim.simdim(google, keywords, 'econ', 'private', 'public', rangelow=1850)
simdim.simdim(coha, keywords, 'econ', 'private', 'public', rangelow=1870)

simdim.simdim(google, keywords, 'econ', 'private', 'public', rangelow=1850, stand = True)
simdim.simdim(coha, keywords, 'econ', 'private', 'public', rangelow=1870, stand=True)






