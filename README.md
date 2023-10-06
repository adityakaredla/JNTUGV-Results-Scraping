# JNTUGV-Results-Scraping

This Python script is designed to scrape student result data from the Jawaharlal Nehru Technological University Kakinada UCEV (JNTUK UCEV) website. It allows you to retrieve result information for multiple students and save it in a JSON file.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- `requests`
- `BeautifulSoup(bs4)`
- `json`

You can install these libraries using pip

```
pip install bs4
```

## Usage

- Modify the script to set your desired parameters, such as the URL, headers, and other options.

- Run the script scraper.py using a Python interpreter.

- You will be prompted to enter the following information:
    - HallTicket Template (Department & Year)
    - Unique Result Code for Examination
    - Roll Number Range
    - File Name to save the results
  
- The script will scrape the data for each student in the specified range and save the results in a JSON file with the provided file name.

## Code Explanation

`studentWiseScraper` Function

- This function scrapes the result data for a single student with a given hall ticket number and result set number.
- It sends a POST request to the specified URL and extracts the relevant data using Beautiful Soup.
- The extracted data is organized into a dictionary and returned as a result.

`funcInitiator` Function

- This function initiates the scraping process for multiple students.
- It takes user input for hall ticket template, result set number, roll number range, and the file name to save the data.
- It calls the `studentWiseScraper` function for each student and collects the results in a list.
- The list is then converted to JSON and saved in a file with the provided name.

## Output Format

```
{
        "Hall Ticket": "20VV1A1225",
        "Name": "KAREDLA ADITYA LAKSHMI NARAYANA",
        "Branch": "INFORMATION TECHNOLOGY",
        "Credits Secured": "21.5",
        "SGPA": "8.16",
        "Subject Wise Report": [
            {
                "Subject": "Advanced Java Programming",
                "Grade Point": "7",
                "Grade": "C"
            },
            {
                "Subject": "Automata & Compiler Design",
                "Grade Point": "8",
                "Grade": "B"
            },
            {
                "Subject": "Cryptography & Network Security",
                "Grade Point": "9",
                "Grade": "A"
            },
            {
                "Subject": "Advanced Communication Skills Lab",
                "Grade Point": "9",
                "Grade": "A"
            },
            {
                "Subject": "Intellectual Property Rights and Patents",
                "Grade Point": "-",
                "Grade": "CMP"
            },
            {
                "Subject": "Machine Learning",
                "Grade Point": "7",
                "Grade": "C"
            },
            {
                "Subject": "Basics of AWS Framework",
                "Grade Point": "7",
                "Grade": "C"
            },
            {
                "Subject": "Advanced Java Programming Lab",
                "Grade Point": "10",
                "Grade": "A+"
            },
            {
                "Subject": "Multimedia & Animation Lab",
                "Grade Point": "10",
                "Grade": "A+"
            },
            {
                "Subject": "Cryptography & Network Security Lab",
                "Grade Point": "9",
                "Grade": "A"
            }
        ],
        "Result Status": "Pass"
    }
```
