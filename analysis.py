from src.data_analysis import data_analysis_functions as functions
import csv

path_to_csv='.\data\data.csv'

data=functions.remove_duplicates( functions.read_csv(path_to_csv))

job_titles, companies, cities, job_descriptions, job_details = functions.separate_data(data)

job_descriptions_cleaned=functions.remove_stop_words(functions.remove_punctuation(job_descriptions))
functions.word_count(job_descriptions_cleaned)
functions.test_analysis(job_descriptions_cleaned)
#functions.word_count(functions.remove_stop_words(functions.remove_punctuation(job_titles)))


# Open the file for writing
with open('data\job_descriptions.csv', mode='w', newline='', encoding='UTF-16') as file:
    writer = csv.writer(file)

    for row in job_descriptions:
        try:
            writer.writerow([row])
        except Exception as e:
            print(f"exception: {e}")
            print("caracter no valido")

print('Data written successfully.')

# Open the file for writing
with open('data\job_descriptions_cleaned.csv', mode='w', newline='', encoding='UTF-16') as file:
    writer = csv.writer(file)

    for row in job_descriptions_cleaned:
        try:
            writer.writerow([row])
        except Exception as e:
            print(f"exception: {e}")
            print("caracter no valido")

print('Data written successfully.')