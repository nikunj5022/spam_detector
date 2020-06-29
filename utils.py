import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def preprocess(m):
    message = re.sub(pattern='[^a-zA-Z]', repl=' ', string=m)
    message = message.lower()
    words = message.split()
    words = [word for word in words if word not in set(stopwords.words('english'))]
    words = [PorterStemmer().stem(word) for word in words]
    message = ' '.join(words)
    return message