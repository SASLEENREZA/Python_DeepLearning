import numpy as num
import matplotlib.pyplot as mat

a=num.array([2.9,6.7,4.9,7.9,9.8,6.9,6.1,6.2,6,5.1,4.7,4.4,5.8])
b=num.array([4,7.4,5,7.2,7.9,6.1,6,5.8,5.2,4.2,4,4.4,5.2])
#calc mean for two lists
mean_a=num.mean(a)
mean_b=num.mean(b)
#calc deviations for slope
x=num.sum((a-mean_a)*(b-mean_b))
y=num.sum(pow(a-mean_a,2))

slope=x/y

intercept_y=mean_b-(slope*mean_a)
print("slope is {}".format(slope))
print("Y Intercept is {}".format(intercept_y))
#calc linear regression
values=(slope*a)+intercept_y
#plot linear regression graph
mat.scatter(a,b)
mat.plot(a,values, color='red')
#give the labels
mat.xlabel("males")
mat.ylabel("females")
#show the graph
mat.show()

