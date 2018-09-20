python_list = ['Alex','Andrew','Joe','Daniel']  #students in python
webapps_list = ['Andrew','Austin','Jeff','Daniel']  # students in webapps

python_set = set(python_list)
webapps_set = set(webapps_list)


print(list(python_set - webapps_set))  # prints only python but not webapps


