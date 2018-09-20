# 5 Classes: Patient, Doctor, Clerk, Book, Nurse
# Used __init__ constructor for every class
# self is used in every class

class Patient():
    def __init__(self, pname, page, pphone, disease, fees ):
        self.pname = pname
        self.page = page
        self.pphone = pphone
        self.__disease = disease
        self.fees = fees

    def getpname(self):
        print("Patient name :", self.pname)

    def getpage(self):
        print("age : ", self.page)

    def getpphone(self):
        print("phone : ", self.pphone)

    def getfees(self):
        print("fees : ", self.fees)

# defining private member
    def getdisease(self):
        print("Disease is : ", self.__disease)

# Inheritance of patient class for doctor class
class Doctor(Patient):
    def __init__(self, dname, dphone, specialisation, pname, page, pphone, fees, disease):
        Patient.__init__(self,pname,page,pphone,disease,fees)
        self.dname = dname
        self.dphone = dphone
        self.spec = specialisation
        self.pname = pname
        self.page = page
        self.pphone = pphone
        self.disease = disease
        self.fees = fees

    def getdname(self):
        print(" Doctor name : ", self.dname)

    def getdphone(self):
        print(" Phone : ", self.dphone)

    def getspec(self):
        print(" Specialisation : ", self.spec)


class Clerk():
    def __init__(self, name ):
        self.cname = name

    def getcname(self):
        print("Clerk name : ", self.cname)


    def cdisplay(self):
        print("The name of the clerk on duty is ", self.cname)

class Book():
    def __init__(self, date, patients_visited ):
        self.date = date
        self.patients_visited = patients_visited

    def getdate(self):
        print("date : ", self.date)

    def getpat_visi(self):
        print("Patients visited : ", self.patients_visited)

class Nurse():
    def __init__(self,nname, dept):
        self.nname = nname
        self.dept = dept

    def getnname(self):
        print("Nurse name : ", self.nname)

    def getdept(self):
        print("Department : ", self.dept)

# Multiple inheritance
class Hospital(Doctor, Patient, Nurse, Book):
    def __init__(self,dname, dphone, specialisation, pname, page, pphone, disease, fees, nname, dept, date, patients_visited ):
        super(Hospital, self).__init__(dname, dphone, specialisation, pname, page, pphone, disease, fees)  # used super class
        Patient.__init__(self, pname,page,pphone,disease,fees)
        Nurse.__init__(self,nname,dept)
        Book.__init__(self, date, patients_visited)

XYZ = Hospital("Bernard", 987654321, "Cardiology", "Alex", 56, 123456789, "Pulmonary Blockage", " $1000", "Kristy", "Anaesthesia", " 19th September, 2018", 123)

print("")
print("-----DOCTOR DETAILS----- ")
XYZ.getdname()
XYZ.getdphone()
XYZ.getspec()

print("")
print("-----PATIENT DETAILS----- ")
XYZ.getpname()
XYZ.getpage()
XYZ.getpphone()
XYZ.getfees()
XYZ.getdisease()

print("")
print("-----NURSE DETAILS----- ")
XYZ.getnname()
XYZ.getdept()

print("")
print("-----LOG BOOK----- ")
XYZ.getdate()
XYZ.getpat_visi()

print("")
print("-----CLERK-----")
clerk1 = Clerk("molly")
clerk1.cdisplay()








