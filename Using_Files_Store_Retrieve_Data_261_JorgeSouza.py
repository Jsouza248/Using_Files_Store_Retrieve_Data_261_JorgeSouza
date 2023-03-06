#JorgeSouza, 261, Using files to store and retrieve data

from datetime import datetime
import locale

FILENAME = ""

def GetEmpName():
    empname = input("Enter Employee Name: ")
    return empname

def GetDatesWorked():
    while True:
        date_str = input("Enter From Date (yyyy-mm-dd): ")
        try:
            fromdate = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid Date Format. Try Again.")
            print()
            continue
        break

    while True:
        date_str = input("Enter To Date (YYYY-MM-DD): ")
        try:
            todate = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid Date Format. Try Again.")
            print()
        if todate <= fromdate:
            print("To date must be after from date. Please try again.")
            print()
        else:
            break
        return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked: '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input("Enter Hourly Rate: "))
    return hourlyrate 
def GetTaxRate():
    taxrate = float(input("Enter Tax Rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate 
    incometax = grosspay * taxrate 
    netpay = grosspay - incometaxrate
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    with open(FILENAME, "r") as EmpFile:

        while True:
            rundate = input("Enter Start Date for Report (MM/DD/YYYY) or ALL for all data in file: ")
            if (rundate.upper() == "ALL"):
                break
            try:
                rundate = datetime.strptime(rundate, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date formate. Try Again.")
                print()
                continue
        while True:
            EmpDetail = EmpFile.readline()

            if not EmpDetail:
                break

            EmpDetail = EmpDetail.replace("\n", "")

            EmpList = EmpDetail.split("|")

            fromdate = EmpList[0]
            if (str(rundate).upper() != "ALL"):
                checkdate = datetime.strptime(fromdate, "%Y-%m-%d")
                if (checkdate < rundate):
                    continue

            todate = EmpList[1]
            empname = EmpList[2]
            hours = float(EmpList[3])
            hourlyrate = float(EmpList[4])
            taxrate = float(EmpList[5])
            grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
            print("*******************")
            print("Name: ", empname)
            print("HJours Worked: ", f"{hours:,.2f}")
            print("Hourly Rate: ", f"{hourlyrate:,.2f}")
            print("Gross Pay: ", f"{grosspay:,.2f}")
            print("Tax Rate: ", f"{taxrate:,.1%}")
            print("Income Tax: ", f"{incometax:,.2f}")
            print("Net Pay: ", f"{netpay:,.2f}")
            print("*******************")
            print()
            TotEmpployees += 1
            TotHours += hours
            TotTax += incometax
            TotNetPay += netpay
            EmpTotals["TotEmp"] = TotEmployees
            EmpTotals["TotHrs"] = TotHours
            EmpTotals["TotGrossPay"] = TotGrossPay
            EmpTotals["TotTax"] = TotTax
            EmpTotals["TotNetPay"] = TotNetPay
            DetailsPrinted = True
        if (DetailsPrinted):
            PrintTotals(EmpTotals)
        else:
            print("No Detail Information to Print")

def PrintTotals(EmpTotals):
    print()
    print(f'Total Number of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')
#
# Correct up to here!!! Add FileName and update again to see if its correct
#
#
if __name__ == "__main__":
    with open(FILENAME, "a") as EmpFile:

        EmpTotals = {}
        DetailsPrinted = False
        while Ture:
            empname = GetEmpName()
            if (empname.upper() == "END"):
                break
            fromdate, todate = GeGetDatesWorked()
            hours = GetHoursWorked()
            taxrate = GetTaxRate()
            fromdate = fromdate.strftime('%Y-%m-%d')
            todate = todate.strftime('%Y-%m-%d')
            EmpDetail = fromdate + "|" + todate + "|" + empname + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"
            EmpFile.write(EmpDetail)

        EmpFile.clse()
        printinfo(DetailsPrinted)
