# Canteen-Automation-System
Built using Django Framework and code behind is in Python.


Working : New user gets registered into the system using unm, pwd, email, mobile no(signup). He is redirected to Login page(cas/login).
in cas we have 3 models stock, billdetails, orderdetails. After successful login the user gets redirected to home page where he will
be able to see the available items . He can select the items and their quantities and place an order. If the selected items are avail in 
quantity then a bill is generated along with a unique bill number and the items along with total cost is shown to user.

Admin can update the stock quantity or cost using the Django Admin portal.

User can also see there previous orders.
