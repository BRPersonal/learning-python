str1,str2,str3,str4 = None,'','Hello','Krishna'
non_null = str1 or str2 or str3 or str4

#This will print Hello because str1 and str2 will evaluate to false
#since str3 evaluates to true, str4 will not be evaluated
print(f"non_null={non_null}")

