# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:38:51 2023

@author: ADMIN
"""
# make a dictionary of contractions
# You can use this package https://github.com/ian-beaver/pycontractions
contraction_mapping = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not",
                           "didn't": "did not",  "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not",
                           "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",
                           "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would",
                           "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would",
                           "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam",
                           "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have",
                           "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock",
                           "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have",
                           "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is",
                           "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as",
                           "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would",
                           "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have",
                           "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have",
                           "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are",
                           "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",
                           "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is",
                           "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have",
                           "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have",
                           "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all",
                           "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",
                           "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have",
                           "you're": "you are", "you've": "you have"}
#%% 
def break_url(df_text): # takes a df returns a df of dtype object
    import re
    '''Retrives url elements & Removes punctuation and special characters
    . , from each data point of a pandas DataFrame'''
    for i in range(0,df_text.shape[1],1):
        for j in range(0,df_text.shape[0],1):
            newString = df_text.iloc[j, i]
            newString= re.sub(r'(http://www.|https://www.)', '', newString) #removing http/www
            newString= re.sub(r'\/', ' ', newString)
            newString= re.sub(r'[\.-]', ' ', newString)
            newString = newString.lower()   #converting everything to lowercase
            newString = newString.split()
            df_text.iloc[j, i] = " ".join(newString).strip()
    return df_text
#%%
def remove_from_str(df_text): # takes a df returns a df of dtype object
    import re
    '''Removes urls, punctuation and special characters . , from each data point
    of a pandas DataFrame'''
    for i in range(0,df_text.shape[1],1):
        for j in range(0,df_text.shape[0],1):
            newString = df_text.iloc[j, i]
            newString=re.sub(r'@[A-Za-z0-9_]+','',newString)                #removing user mentions
            newString=re.sub("[#\.,]","",newString)                             #removing hash symbols
            newString= ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in newString.split(" ")]) #contraction mapping
            newString= re.sub(r'http\S+', '', newString)                   #removing links
            newString= re.sub(r"'s\b","",newString)                        #removing 's
            newString = re.sub("[^a-zA-Z]", " ", newString)             #Fetching out only letters
            newString = newString.lower()                              #converting everything to lowercase
            newString = newString.split()
            df_text.iloc[j, i] = " ".join(newString).strip()
    return df_text
#%%
def remove_stop_words(df_text): # takes a df returns a df of dtype object
    import spacy
    en = spacy.load('en_core_web_sm')
    stopwords = en.Defaults.stop_words
    '''Removes stop words from each data point of a pandas DataFrame'''
    for i in range(0,df_text.shape[1],1):
        for j in range(0,df_text.shape[0],1):
            newString = df_text.iloc[j, i]
            temp = []
            for token in newString.split(): # breaking each data point to tokens
                if token not in stopwords:
                    temp.append(token) # appending only if not in spacy stopword list
            df_text.iloc[j, i] = " ".join(temp).strip() # joining tokens to string
    return df_text
#%%
def lemma(df_text): # takes a df returns a df of dtype object
    import spacy
    en = spacy.load('en_core_web_sm')
    '''Lemmatizes tokens in each data point of a pandas DataFrame'''
    for i in range(0,df_text.shape[1],1):
        for j in range(0,df_text.shape[0],1):
            newString = df_text.iloc[j, i]
            doc = en(newString.lower())
            temp = []
            for token in doc:
                temp.append(token.lemma_)
            df_text.iloc[j, i] = " ".join(map(str, temp)) # joining tokens to string
    return df_text
#%%




