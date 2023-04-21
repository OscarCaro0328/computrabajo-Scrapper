import collections
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


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
 

    # Combine all the job descriptions into a single string
    #all_text = " ".join(lists)

    # Split the text into individual words
    #words = all_text.split()
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

    """
    #We take the word "experiencia" and form phrases with 3 words before and 3 words after
    experiencia_phrases = []
    for i, word in enumerate(words):
        if word == "experiencia":
            experiencia_phrases.append(words[i-3:i+4])
    



    # Count the frequency of each word
    word_counts = collections.Counter(words)

    # Print the 10 most common words and their counts
    for word, count in word_counts.most_common(100):
        print(f"{word}: {count}")
    """
     
    

#def word_count():
