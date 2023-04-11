Computrabajo Web Scraper
This Python program extracts job offers from the Computrabajo website and saves the data to a CSV file. It also sends an email with the collected information as an attachment.

Getting Started
Prerequisites
You need to have Python 3 installed on your system, as well as the following libraries:

beautifulsoup4
selenium
pandas
numpy
openpyxl
smtplib
email.mime.text
email.mime.multipart

You can install them by running the following command:
pip install -r requirements.txt
Usage
Clone the repository:

git clone https://github.com/your-username/computrabajo.git
Change into the project directory:

cd computrabajo
Customize the configuration file config.py with your preferred search criteria, email settings, and file paths.

Run the program:

python main.py
Check the generated CSV file and email attachment with the extracted information.
File Structure
The project follows this file structure:

computrabajo-Scrapper/
├── data/
│   └── data.csv
├── src/
│   ├── functions_computrabajo_scrapper.py
│   └── send_email.py
├── config.py
├── main.py
├── README.md
└── requirements.txt
The data folder stores the CSV file with the extracted information.
The src folder contains the Python modules with the main functions of the program.
The config.py file sets the program parameters.
The main.py file runs the main program.
The README.md file is this document.
The requirements.txt file lists the required libraries and their versions.
Authors
Oscar Caro
