import collections
import difflib
import nltk
import csv
import string
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def read_csv(path_to_csv):
    # Open the CSV file for reading
    with open(path_to_csv, 'r',encoding='UTF-16') as file:
        reader = csv.reader(file, delimiter='\t')
        # Read each row of the CSV file into a list of lists 
        #and converts all strings to small caps
        data = [[word.lower() for word in row] for row in reader]
    return data

def remove_duplicates(job_listings):
    unique_listings = []
    unique_descriptions = set()

    for listing in job_listings:
        if listing[2] not in unique_descriptions:
            unique_listings.append(listing)
            unique_descriptions.add(listing[2])

    return unique_listings

def separate_data(data):
    #the data matrix has n listings times 4 columns
    #The columns are Job Title, Company and City, Job Description, Job details
    job_titles, companies_cities, job_descriptions, job_details = [list(col) for col in zip(*data)]

    #All companies are separated from the city by a '-'
    #if a string has more than one '-', we eliminate the first one which is part of the name,
    #and leave the second one to be able to separate company from city  
    for i, s in enumerate(companies_cities):
        if s.count("-") > 1:
           companies_cities[i] = s.replace("-", " ", 1)
        #Separate companies from cities
    companies = []
    cities = []

    for cc in companies_cities:
        split_cc = cc.split('-')
        companies.append(split_cc[0].strip())
        cities.append(split_cc[1].strip())
        
    return job_titles, companies, cities, job_descriptions, job_details

def remove_stop_words(lists_of_strings):
    # Remove stop words in Spanish and English
    stopwords_sp = stopwords.words('spanish')
    stopwords_en = stopwords.words('english')
    stopwords_all = set(stopwords_sp + stopwords_en)
    result = []

    for string in lists_of_strings:
        words = string.split()
        words = [word for word in words if word.lower() not in stopwords_all]
        result.append(" ".join(words))
    return result 

     
def word_count(strings):
    words = ' '.join(strings).split()  # Concatenate and split the strings into words
    word_freq = collections.Counter(words)  # Use Counter to count the frequency of each word
    for word, frequency in word_freq.most_common(100):
        print(word, frequency) 

def diferenciador(list1,list2):
    diff = difflib.ndiff(list1, list2)

    for line in diff:
        print(line)

def remove_punctuation(original_list):
    # List comprehension to remove punctuation and symbols, except for decimal points in numbers
    cleaned_list = []
    for string in original_list:
        # Use a regular expression to replace all non-alphanumeric characters, except for decimal points in numbers
        cleaned_string = re.sub(r'(?<!\d)[^\w\s]+|[^\w\s]*(?<=\d)[^\w\s]+[^\w\s]*(?!\d)', ' ', string)
        cleaned_list.append(cleaned_string)
    return cleaned_list


def test_analysis(list1):
    # Convert the cleaned job listings into a document-term matrix
    vectorizer = CountVectorizer()
    doc_term_matrix = vectorizer.fit_transform(list1)
    # Get the list of feature names
    feature_names = vectorizer.get_feature_names_out()

    # Apply LDA algorithm to the document-term matrix
    lda_model = LatentDirichletAllocation(n_components=5, random_state=42)
    lda_model.fit(doc_term_matrix)

    # Assign the most representative terms to each topic
    for topic_idx, topic in enumerate(lda_model.components_):
        print("Topic %d:" % (topic_idx))
        top_terms_idx = topic.argsort()[:-11:-1]
        top_terms = [feature_names[i] for i in top_terms_idx]
        print(top_terms)