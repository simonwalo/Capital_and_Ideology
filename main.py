#%% import packages

import semchange
import simdim
from gensim.models import KeyedVectors


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
    print(y.most_similar("market"))


#%% visualize semantic change over time (PCA with keyword as passive projection)

semchange.semchange(google, "work", rangelow=1810, rangehigh=2000, rangestep=60, export=False)


#%% Protestant Ethic


keywords['work'] = [
    "work", "works", "worked", "working", "job", "jobs",
    "career",
    "profession", "professions", "professional",
    "occupation", "occupations",
    "employment", "employed",
    "labor", "labors", 'labour', 'labours'
]

# discarded: careers


keywords['rich'] = ["wealth", "wealthy", "rich", "affluence", "affluent"]
keywords['poor'] = ["poor", "poverty", "impoverished", "destitute", "needy"]

keywords['Affluence'] = keywords['rich'] + keywords['poor']



keywords['Religion'] = [
    "redemption", "salvation", "god", "religion", "holy", "calling", "faith", "pious",
    "spiritual", "sacred", "divine", "belief", "worship"
]



keywords['moralpos'] = [
    "good", "moral", "honest", "virtuous", "virtue", "decent", "noble",
    "honour", "integrity", "worth", "dignity", "just", "justice"
]

keywords['moralneg'] = [
    "evil", "immoral", "bad", "dishonest", "sinful", "vice", "unjust", "injustice"
]


keywords['Morality'] = [
    'good', 'evil', 'moral', 'immoral', 'good', 'bad', 'honest', 'dishonest',
    'virtuous', 'sinful', 'virtue', 'vice',
    "decent", "noble", "honour", "integrity", "worth", "dignity"
]

simdim.simdim(google, keywords, 'work', 'Morality', 'Affluence', 'Religion', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'work', 'Morality', 'Affluence', 'Religion', rangelow=1870, stand=False)

simdim.simdim(google, keywords, 'work', 'Morality', 'Affluence', 'Religion', rangelow=1850, stand=True)
simdim.simdim(coha, keywords, 'work', 'Morality', 'Affluence', 'Religion', rangelow=1870, stand=True)



# tests:

keywords['identity'] = [
    "identity", "fulfilling", "expression", "express"
]

#simdim.simdim(models_all, keywords, 'work', 'rich', 'poor', ci=0)
#simdim.simdim(models_all, keywords, 'work', 'moralpos', 'moralneg', ci=0)

#simdim.simdim(models_all, keywords, 'work', 'identity', 'Religion', ci=0)





#%% Alienation

keywords['work'] = [
    "work", "works", "worked", "working", "job", "jobs",
    "career",
    "profession", "professions", "professional",
    "occupation", "occupations",
    "employment", "employed"
]

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['work']))

# check coha keywords availability

    for year, model in coha.items():
            for term in keywords['work']:
                if model[term].all() == coha[1810]['biology'].all():
                    print('Keyword ', term, ' not available for ', year)

keywords['work2'] = [
    "work", "works", "worked", "working", "job",
    "career",
    "profession", "professional",
    "occupation",
    "employment", "employed"
]

# find related terms
for  year, model in coha.items():
    print(year, model.most_similar(positive=keywords['work2']))

keywords['Extrinsic'] = [
                    "earn", "earning", "earnings", "money",
                    "wage", "wages", "salary", "income", "remuneration", "pay",
]
#discarded because of theory: "secure", "security", "insecure", "insecurity"

keywords['Intrinsic'] = [
    "interesting", "interest", "interested",
    "boring", "bore", "bored",
    "fulfilling", "fulfill", "fulfilled",
    "stimulate", "stimulating", "stimulation",
    "product"
]
# temp discard:    "useful", "useless",
#     "expression", "express", "expressive",
#     "satisfy", "satisfying", "satisfied",

coha[1990].n_similarity(keywords['work'], ['product'])

simdim.simdim(google, keywords, 'work', 'Extrinsic', 'Intrinsic', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'work2', 'Extrinsic', 'Intrinsic', rangelow=1870, stand=False)

simdim.simdim(google, keywords, 'work', 'Extrinsic', 'Intrinsic', rangelow=1850, stand=True)
simdim.simdim(coha, keywords, 'work2', 'Extrinsic', 'Intrinsic', rangelow=1870, stand=True)







#%% (Neo-)Liberalism


keywords['econ'] = [
    "profit", "profitable", "cost", "benefit", "sell", "revenue", "gain",
    "loss", "capital", "invest", "economic", "price", "business", "money", "trade",
    "pay", "paid"
]

keywords['econ'] = [
    "economy", "invest", "economic", "business", "money", "trade"
]



keywords['intervention'] = [
    "regulate", "intervention", "regulated", "govern", "regulation", "restrict",
    "prohibit", "control", "prescribe"
]

keywords['liberal'] = [
    "free", "unfettered", "freedom", "faire", "laissez", "liberalism", 'liberty'
]

#discarded:

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['liberal']))

simdim.simdim(google, keywords, 'econ', 'liberal', 'intervention', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'econ', 'liberal', 'intervention', rangelow=1870, stand=False)

simdim.simdim(google, keywords, 'econ', 'liberal', 'intervention', rangelow=1850, stand=True)
simdim.simdim(coha, keywords, 'econ', 'liberal', 'intervention', rangelow=1870, stand=True)











#%% Economization

### Economic code ###
keywords['econ'] = [
    "profit", "profitable", "cost", "benefit", "sell", "revenue", "gain",
    "loss", "capital", "invest", "economic", "price", "business", "money", "trade",
    "pay", "paid", "market"
]
#discarded: "maximize", "asset"


### Politics ###

#Political system
keywords['Politics'] = [
    "politics", "political", "policy", "legislative", "legislation", "government", "state"
]

#Political code
keywords['power'] = [
    "power", "rule", "influence", "law", "laws", "authority", "sovereign", "control", "command"
]

simdim.simdim(google, keywords, 'Politics', 'econ', 'power', rangelow=1850, stand=False)
simdim.simdim(coha, keywords, 'Politics', 'econ', 'power', rangelow=1850, stand=False)

simdim.simdim(google, keywords, 'Politics', 'econ', 'power', rangelow=1850, stand=True)
simdim.simdim(coha, keywords, 'Politics', 'econ', 'power', rangelow=1850, stand=True)


### education ###

#educational system
keywords['Education'] = [
    "education", "school", "teach", "university"
]

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['Education']))

#educational code
keywords['develop'] = [
    "study", "learn", "development", "develop", "skill", "critical", "thinking", "think", "growth", "empower"
]
#discarded because of data: "skills"
# discarded because of theory: "equal", "equality", "dignity", "curious", "curiosity", "stimulate", "stimulating"

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['develop']))

simdim.simdim(google, keywords, 'Education', 'develop', 'econ', rangelow=1850)
simdim.simdim(coha, keywords, 'Education', 'develop', 'econ', rangelow=1870)

simdim.simdim(google, keywords, 'Education', 'develop', 'econ', rangelow=1850, stand=True)
simdim.simdim(coha, keywords, 'Education', 'develop', 'econ', rangelow=1870, stand = True)




### health ###

#health system
keywords['medicine'] = [
    "medicine", "medical", "care", "hospital", "doctor", "physician"
]

#health code
keywords['health'] = [
    "health", "healthy", "welfare", "provision", "provide", "care", "treat",
    "treatment", "sick", "sickness", "disease",
]
#discarded: "diagnose", "therapy"

simdim.simdim(google, keywords, 'medicine', 'health', 'econ', rangelow=1850)
simdim.simdim(coha, keywords, 'medicine', 'health', 'econ', rangelow=1870)

simdim.simdim(google, keywords, 'medicine', 'health', 'econ', rangelow=1850, stand=True)
simdim.simdim(coha, keywords, 'medicine', 'health', 'econ', rangelow=1870, stand=True)




### science ###

#science system
keywords['science'] = [
    "science", "sciences", "scientific", "university", "research", "study", "studies",
    "physics", "mathematics", "institute", "psychology", "philosophy"
]
#discarded: humanities, sociology

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['science']))


#science code
keywords['scientific'] = [
    "truth", "true", "untrue", "knowledge", "collective", "discover", "discovery",
    "understand", "understanding", 'comprehend', 'meaning', 'reason',
    "explain", "explanation", "method", "methodical"
]

# find related terms
for  year, model in google.items():
    print(year, model.most_similar(positive=keywords['scientific']))

simdim.simdim(google, keywords, 'science', 'scientific', 'econ', rangelow=1850)
simdim.simdim(coha, keywords, 'science', 'scientific', 'econ', rangelow=1870)

simdim.simdim(google, keywords, 'science', 'scientific', 'econ', rangelow=1850, stand=True)
simdim.simdim(coha, keywords, 'science', 'scientific', 'econ', rangelow=1870, stand=True)












