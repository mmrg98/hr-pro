from datetime import datetime
class Employee:
        def __init__(self,name, age, salary, employment_year):
                self.name=name
                self.age=age
                self.salary=salary
                self.employment_year=employment_year
        def get_working_years(self):
                return " Working Years: %d" % int((datetime.now().year)-(self.employment_year))
        
        def __str__(self):
                return "Name: %s, Age: %s, Salary: %s,%s" %(self.name, self.age, self.salary,Employee.get_working_years(self))
        

class Manager(Employee):
        def __init__(self,name, age, salary, employment_year,bonus_percentage):
                Employee.__init__(self,name, age, salary, employment_year)
                self.bonus_percentage=bonus_percentage
        def get_bonus(self):
                return "Bonus: %d" % (float(self.bonus_percentage)*int(self.salary))
        def __str__(self):
                return "%s, %s"% (str(Employee.__str__(self)),self.get_bonus())
        
def main():
            emp_list=[Employee("Mariam","21","2000",2017),Employee("Nora","23","3000",2018)]
            
            mang_list=[Manager("Sara","31","5000",2011,.10),Manager("Ahmed","43","7000",2008,.15)]
            str_op=""""Options:
            1. Show Employees
            2. Show Managers
            3. Add An Employee
            4. Add A Manager
            5. Exit
"""
            print(str_op)
            op=int(input("What would you like to do?"))
            while op!=5:
                    if op==1:
                            for i in emp_list:
                                    print(i)
                            op=int(input("What would you like to do?"))
                    elif op==2:
                            for i in mang_list:
                                    print(i)
                            print(str_op)
                            op=int(input("What would you like to do?"))
                    elif op==3:
                            name=input("Name: ")
                            age=input("Age: ")
                            salary=input("Salary: ")
                            employment_year=int(input("Employment Year: "))
                            emp_list.append(Employee(name,age,salary,employment_year))
                            print("Employee added succesfully")
                            print(str_op)
                            op=int(input("What would you like to do?"))
                    elif op==4:
                            name=input("Name: ")
                            age=input("Age: ")
                            salary=input("Salary: ")
                            employment_year=int(input("Employment Year: "))
                            bonus_percentage=float(input("Bonus Percentage: "))
                            mang_list.append(Manager(name,age,salary,employment_year,bonus_percentage))
                            print("Manager added succesfully")
                            print(str_op)
                            op=int(input("What would you like to do?"))
                    else:
                            print("choose correct option ")
                            print(str_op)
                            op=int(input("What would you like to do?"))
                            
                            
                        
                
        





            

if __name__ == '__main__':
            main()
