class emp:
  "this is example of employee class"
  empcnt=0
  sumsal=0
  def __init__(self,ename,sal,fam,dept):
      self.ename=ename
      self.fam=fam
      self.sal=sal
      self.dept=dept
      emp.empcnt+=1
      emp.sumsal+=sal

  def display(self):
      print("name:",self.ename,"salary:",self.sal, "family:",self.fam, "department:",self.dept)


class fullTime(emp):
    def __init__(self,ename,sal,fam,dept):
        emp.__init__(self,ename,sal,fam,dept)


employee1=emp("sasleen",1000,"sss","development")
employee2=emp("reza",1500,"kkk", "testing")
employee3=emp("sirish",2000,"yyy", "support")
employee2.display()
print("total employees:", emp.empcnt)
avg=emp.sumsal/emp.empcnt
print("the salary average is",avg)


