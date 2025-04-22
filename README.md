Measuring Historical Changes in Capitalist Ideology with Word Embeddings
=================
Code associated with my paper on capitalist ideology. Preprint available here: https://osf.io/preprints/socarxiv/pxj7m_v1

## Instructions
<i>Load data</i>
<br/>
 * Clone repository.
 * Create a folder named "data" in project main directory.<br/>
 * Download data from https://nlp.stanford.edu/projects/histwords/ (SGNS All English (1800s-1990s)), unzip, and save files in data folder.<br/>
 * Use "prepare embeddings.py" to convert word vectors into the format used by the gensim package.<br/>
 <br/>

<i>Analyze data using the following functions in "analysis.py"</i>
<br/>
 * semchange: Visualizes how a given input term changes its position in the embeddings space over time relative to its nearest neighbors.<br/>
 * simdim: Estimates the cosine similarity over time between a word list ("key") and any number of additional word lists ("dimensions"). Creates a figure for up to three dimensions.<br/>

<i>Reproduce figures used in paper in "create figures.py"</i>
<br/>
 * This script essentially combines two figures produced with the "simdim" function.

Also check out my interactive web app to explore diachronic word embeddings: https://huggingface.co/spaces/BrickTamland/Histwords-Webapp
