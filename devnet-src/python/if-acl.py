aclNum = int(input("What is the IPv4 ACL number? "))

if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
    print("This is an extended IPv4 ACL.")
elif aclNum >= 200 and aclNum <= 299:
    print("this is fictional ACL ")
elif aclNum >= 300 and aclNum <= 399:
    print("this is notthing ")
else:
    print("This is not a standard or extended IPv4 ACL.")