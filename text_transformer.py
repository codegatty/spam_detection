from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from gensim.utils import tokenize
import string

def text_transformer(txt):
    ps=PorterStemmer()
    txt=txt.lower()
    txt=list(tokenize(txt))
    y=[]
    for i in txt:
        if i.isalnum():
            y.append(i)
    text=y[:];#python list are mutable
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text=y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    return ' '.join(y)
