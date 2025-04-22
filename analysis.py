#%% import packages

from functions.semchange import semchange
from functions.simdim import simdim
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

#%%  most similar terms by decade

for x, y in google.items():
    print(x)
    print(y.most_similar("gdp"))


#%% visualize semantic change over time (PCA with keyword as passive projection)

semchange(googlefiction, "gay", rangelow=1870, rangehigh=2000, rangestep=60, export=False)



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




simdim(google, "Google", keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=False)
simdim(coha, "COHA", keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=False)




#extra: google books fiction
simdim(googlefiction, "Google Fiction", keywords, 'econ', 'Liberalism', 'Regulation', rangelow=1850, stand=True)


#%% Meritocracy


keywords['Work'] = [
    "work", "works", "worked", "working",
    "job", "jobs",
    "career", "careers",
    "employment", "employed",
    "labor", "labors", 'labour', 'labours',
]

# discarded:
#"profession", "professions", "professional",
#"occupation", "occupations",

keywords['merit'] = [
    'merit', 'merits', 'merited', # nimmt ab, coha zu
    'deserve', 'deserved', 'deserves', 'deserving', # nimmt zu
    'just', 'justice', 'justly', #nimmt zu
    "effort", "efforts", # nimmt leicht zu
    'perform', 'performance', # leichte zunahme, coha abnahme
    'reward', 'rewards', 'rewarded', #google abnahme, coha zunahme
    'accomplish', 'accomplishment',  # leichte zunahme, coha zunahme
    'achieve', 'achievement' # konstant, coha abnahme
]

'''
#discarded:
# 'fair', 'fairness' (polysemy)
# 'just', 'justice', 'justly',  #nimmt zu

#    'merit', 'merits', 'merited',  # nimmt ab, coha zu
    'deserve', 'deserved', 'deserves', 'deserving',  # nimmt zu

    'perform', 'performance',  # leichte zunahme, coha abnahme
    'reward', 'rewards', 'rewarded',  #google abnahme, coha zunahme
    'accomplish', 'accomplishment',  # leichte zunahme, coha zunahme
    'achieve', 'achievement',  # konstant, coha abnahme
'''

#test
keywords['merit'] = [
    'talent', 'talents', "talented",  # zunahme, coha abnahme
    'skill', 'skills', "skilled",  # konstant, coha abnahme
    'able', 'ability', 'abilities',  # konstant, coha abnahme
    "effort", "efforts",  # nimmt leicht zu
    "commitment", "commit", "commited",
    "dedication", "dedicate", "dedicated"
]

simdim(google, "Google", keywords, 'Affluence', 'Work', 'Inheritance', 'merit', rangelow=1850, stand=False)
simdim(coha, 'COHA', keywords, 'Affluence', 'Work', 'merit', 'Inheritance', rangelow=1850, stand=False)

simdim(google, "Google", keywords, 'Affluence', 'Work', 'Inheritance', 'merit', rangelow=1850, stand=True)
simdim(coha, 'COHA', keywords, 'Affluence', 'Work', 'merit', 'Inheritance', rangelow=1850, stand=True)

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



keywords['luckinherit'] = keywords['luck'] + keywords['Inheritance']

# find related terms
for year, model in google.items():
    print(year, model.most_similar(positive=keywords['Inheritance']))

for year, model in google.items():
    print(year, model.most_similar(positive=['Inheritance']))


simdim(google, keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=False)
simdim(coha, keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=False)



#extra: google books fiction
simdim(googlefiction, keywords, 'Affluence', 'Work', 'Inheritance', rangelow=1850, stand=True)



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


keywords['alienation'] = [
    # Core concepts
    "exploitation", "exploit", "exploited", "exploiting", "exploits",
    "alienation", "alienated", "alienating", "alienates",
    "oppression", "oppress", "oppressed", "oppressing", "oppressive",
    "commodification", "commodify", "commodified", "commodifies",
    "coercion", "coerce", "coerced", "coercing", "coercive",
    "force", "forced", "forcing",
    "disempowerment", "disempowered", "disempower", "disempowering",
    "extraction", "extract", "extracted", "extracting"]

'''
    # Descriptive/emotional
    "exhaustion", "exhaust", "exhausted", "exhausting",
    "burnout", "burned", "burnt", "burning",
    "monotony", "monotonous",
    "drudgery", "drudge", "drudging",
    "dehumanization", "dehumanize", "dehumanized", "dehumanizing",
    "subjugation", "subjugate", "subjugated", "subjugating",
    "dispossession", "dispossess", "dispossessed", "dispossessing",
    "misery", "miserable",
    "inequality", "unequal",
    "dependency", "dependent", "dependence", "depending",

    # Class/systemic critique
    "proletariat",
    "accumulation",
    "discipline",
    "powerlessness", "powerless",
    "unfreedom",
    "violence",
    "overwork", "overworked", "overworking",
    "precarity", "precarious",
    "gigification", "gigified"
]

'''

keywords['alienation'] = [
    "exploitation", "exploit", "exploited", "exploiting", "exploits",
    "alienation", "alienated", "alienating", "alienates",
    "oppression", "oppress", "oppressed", "oppressing", "oppressive",
    "commodification", "commodify", "commodified", "commodifies",
    "coercion", "coerce", "coerced", "coercing", "coercive",

    "tired", "tiring",
    "exhausted", "exhausting",
    "stress", "stressed", "stressful",
    "miserable", "suffering",
    "struggle", "struggling"
    "depressed",
    "bored", "boring",
    "meaningless", "worthless",
    "dangerous", "unsafe", "monotonous",


    'toil', 'toils',
    'trouble', 'troubles',
    'struggle', 'struggles', 'drudgery',
    'pain', 'pains',
    'fatigue', 'arduous', 'strenuous'
]

''' discarded
"resentment", "frustration",
"abused", "used", "trapped", "controlled", "manipulated",
    "dependent", "submissive", "obedient", "rigid", "thankless",
    "force", "forced", "forcing",
    "extraction", "extract", "extracted", "extracting",
'''


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
    print(year, model.most_similar(positive=['alienation']))

for  year, model in coha.items():
    print(year, model.most_similar(positive=['work']))

simdim(google, "Google", keywords, 'work', 'alienation', 'Intrinsic', rangelow=1850, stand=False)
simdim(coha, "COHA", keywords, 'work', 'alienation', 'Intrinsic', rangelow=1850, stand=False)

simdim(google, "Google", keywords, 'work', 'alienation', 'Intrinsic', rangelow=1850, stand=True)
simdim(coha, "COHA", keywords, 'work', 'alienation', 'Intrinsic', rangelow=1850, stand=True)

#extra: google books fiction
simdim(googlefiction, keywords, 'work', 'Extrinsic', 'Intrinsic', rangelow=1850, stand=True)



















##### NOT INCLUDED IN PAPER #####




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

simdim(google, "Google", keywords, 'econ', 'private', 'public', rangelow=1850)
simdim(coha, "COHA", keywords, 'econ', 'private', 'public', rangelow=1870)

simdim(google, keywords, 'econ', 'private', 'public', rangelow=1850, stand = True)
simdim(coha, keywords, 'econ', 'private', 'public', rangelow=1870, stand=True)







#%% moralische Bewertung von Ungleichheit & Steuern


keywords['just'] = [
    "good", "just", "justice", "fair"
]

keywords['unjust'] = [
    "evil", "immoral", "bad", "unjust", "injustice", "unfair"
]


keywords['inequality'] = [
    "inequality", "unequal", "inequalities", "disparity"
]

keywords['taxes'] = [
    "taxes", "taxation", "tax"
]

keywords['unemployment'] = [
    "unemployed", "unemployment"
]







