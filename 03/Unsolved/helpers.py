def studentInformation():
    #Prompts for student information
    first = input('Please enter the student\'s first name:')
    middle = input('Please enter the student\'s middle name:')
    last = input('Please enter the student\'s last name:')
    address = input('Please enter the student\'s current address:')
    email = input('Please enter the student\'s electronic email:')
    phone = input('Please enter the student\'s phone number:')
    
    # Returning values
    return [first, middle, last, address, email, phone]
# Definition to create a student
def createStudent(**student):
    #setting student directory
    studentDict = dict.fromkeys(['firstName', 'middleName', 'lastName', 'address', 'email', 'phone'])

    studentDict['firstName'] = student.get('firstName', 'N/A')
    studentDict['middleName'] = student.get('middleName', 'N/A')
    studentDict['lastName'] = student.get('lastName', 'N/A')
    studentDict['address'] = student.get('address', 'N/A')
    studentDict['email'] = student.get('email', 'N/A')
    studentDict['phone'] = student.get('phone', 'N/A')

    #returning values
    return studentDict

def printSeperator(repetitions = 18):
    print('=' * repetitions)

def printStudent(student):
    print('You\'ve entered:')
    printSeperator()

    for key, value in student.items():
        print('The student\'s {0} is {1}.'.format(key, value))
    printSeperator()
def confirm(message):
    confirmation = (input(message).lower() == 'y')
    return confirmation
def printSummary(students):
    print('You\'ve entered the following information:')
    printSeperator()
    for student in students:
        printStudent(student)
    printSeperator()
