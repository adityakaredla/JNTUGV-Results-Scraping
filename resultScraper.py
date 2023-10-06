import requests
from bs4 import BeautifulSoup
import json
url = "https://results.jntukucev.ac.in/helper.php?gamaOne=getResult"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,te;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "cookie": "PHPSESSID=ab580ng56tf2sfjgcahn530g7g; lang=english; _gid=GA1.3.717399314.1696568166; _ga_G7QLRCLVJE=GS1.1.1696568162.1.1.1696568263.0.0.0; _ga=GA1.3.1704497817.1696568162; _ga_TN8VHQWHS4=GS1.1.1696568162.1.1.1696568263.0.0.0",
    "Referer": "https://results.jntukucev.ac.in/result/fe7382afad54ab1997c4101456948aa5",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

def studentWiseScraper(studentHallTicketNumber , resultSetNumber):
    data = {
        "hallticket" : studentHallTicketNumber,
        "result" : resultSetNumber
    }
    subjects = []
    grades = []
    points = []
    subjectCodes = []
    studentName = ''
    hallTicket = ''
    branch =''
    creditsSecured = ''
    sGPA = 0
    resultStatus = 0
    response = requests.post(url,data=data)
    if response.text == """<div class="isa_error">Invalid Hallticket, Please contact Exam Branch if you think this is a mistake.</div>""":
        return None
    soup = BeautifulSoup(response.text , "html.parser")
    elements = soup.find_all("div" , class_= "row")
    element = elements[1]
    elements = soup.find_all("div" , class_ = "cell")
    for element in elements:
        if "data-title" in element.attrs:

            if element.attrs['data-title'] == "Hall Ticket":
               hallTicket =  element.get_text().strip()

            if element.attrs['data-title'] == "Full Name":
               studentName =  element.get_text().strip()

            if element.attrs['data-title'] == "Branch":
               branch =  element.get_text().strip()

            if element.attrs['data-title'] == "Credits Secured":
               creditsSecured =  element.get_text().strip()

            if element.attrs['data-title'] == "SGPA":
               sGPA =  element.get_text().strip()

            if element.attrs['data-title'] == "Result Status":
               resultStatus =  element.get_text().strip()

            if element.attrs['data-title'] == "Subject Code":
                subjectCodes.append(element.get_text().strip())

            if element.attrs['data-title'] == "Subject":
                subjects.append(element.get_text().strip())

            if element.attrs['data-title'] == "Grade":
                grades.append(element.get_text().strip())

            if element.attrs['data-title'] == "Grade Point":
                points.append(element.get_text().strip())

    studentReport = []

    for subject , point , grade in zip(subjects , points , grades):
        studentReport.append(
            {
                "Subject" : subject,
                "Grade Point" : point,
                "Grade" : grade
            }
        )

    studentData = {
        "Hall Ticket" : hallTicket,
        "Name" : studentName,
        "Branch" : branch,
        "Credits Secured" : creditsSecured,
        "SGPA" : sGPA,
        "Subject Wise Report" : studentReport,
        "Result Status" : resultStatus
    }
    return studentData

def funcInitiator():
    hallTicketTemplate = input("Enter HallTicket String (Dept & Year) :")
    resultSetNumber = int(input("Enter Unique Result Code for Examination"))
    rollNumberRange = int(input("Enter Roll Number Range:"))
    fileName = input("Enter File Name to be saved :")
    classData = []
    for i in range(1 , rollNumberRange):
        seqNumber = i
        if len(str(seqNumber)) == 1 : seqNumber = "0" + str(seqNumber)
        studentData = studentWiseScraper(hallTicketTemplate + str(seqNumber) , resultSetNumber)
        if studentData != None : classData.append(studentData)

    if len(classData) > 0:
        classData = json.dumps(classData , indent=4)
        with open(fileName, "w") as file : 
            file.write(classData)
        print(fileName+" created in the Root Directory!!")

    else:
        print("No Data Exist with the given Info")

funcInitiator()