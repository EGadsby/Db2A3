import csv

def myreader(filename:str)->list:
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list

def mywriter(filename:str, mylist:list):
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write multiple rows
        writer.writerows(mylist)

def main():
    # read PERFORMANCE data
    mydata = myreader('Student_Performance_Data.csv')
    wrdata = mywriter('new_student_performance.csv')
    
    print("STUDENT_PERFORMANCE_DATA")
    for i in range(0,29):
        print(mydata[i])
        mywriter.writerow('new_student_performance.csv',mydata[i])
    print("=============================================================================================")
    # read DEPT data
    mydata = myreader('Department_Information.csv')
    print("DEPARTMENT_DATA")
    for i in range(0,29):
        print(mydata[i])
    print("=============================================================================================")
    # read COUNCIL data
    mydata = myreader('Student_Counceling_Information.csv')
    print("STUDENT_COUNCELING_DATA")
    for i in range(0,29):
        print(mydata[i])
    print("=============================================================================================")
    # read EMPLOYEE data
    mydata = myreader('Employee_Information.csv')
    print("EMPLOYEE_INFORMATION")
    for i in range(0,29):
        print(mydata[i])

import csv

def check_department_information(csv_file):

    mydata = myreader(csv_file)
    for row_num, row in enumerate(mydata, start=1): 
        for col_num, value in enumerate(row, start=1):
            if len(value.strip()) == 0:  
                print(f"blank value at row {row_num}")
            if (col_num == 3):
                myList = value.split('/')
                if len(myList) == 3:      
                    print(myList)
                    DOE = myList[2]
                    if (int(DOE) < 1900):
                        print(f"date is too early at {row_num}")
    

def check_Number(number):
    if not isinstance(number, (int, float)):
       return False;
    else: 
        return True;
    


# Example usage:
print("department information")
check_department_information("Department_Information.csv")
# print("Student performance")
# check_department_information('Student_Performance_Data.csv')
# print("Student Counceling")
# check_department_information('Student_Counceling_Information.csv')
        
# main()
