
def main():
    emprate=[0]*5
    emphours=[0]*5
    empsalary=[0]*5
    counter = 0
    emplist = [0]*5
    while counter<5:
        print("Please enter the details of Employee", counter+1)
        print("Please enter pay rate per hour of employee:")
        emprate[counter]=float(input())
        print("Please enter number of hours worked by the employee:")
        emphours[counter]=float(input())
        salary = emprate[counter] * emphours[counter]
        empsalary[counter] = salary
        emplist[counter] = [counter+1,emprate[counter],emphours[counter],empsalary[counter]]
        counter += 1
    print(emplist)
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-Output-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")
    titles = ["Employee Number","Rate ","Hours Worked ","Salary "]
    t_format ="{:>8}" * (len(titles) + 1)
    print(t_format.format("", *titles))
    y_format ="{:10}" * (len(titles) + 1)
    print(y_format.format("", *emplist[0]))
    print(y_format.format("", *emplist[1]))
    print(y_format.format("", *emplist[2]))
    print(y_format.format("", *emplist[3]))
    print(y_format.format("", *emplist[4]))

main()

