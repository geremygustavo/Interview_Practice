# Interview_Practice
Requirements


pipenv

To install pipenv environment run :

```
pipenv install
pipenv shell
pipenv run python -m pytest
```

To run Test run 

```
pipenv run python -m pytest
```




BUG Report

		Title
RESET APP STATE item does not refresh Products  Selected
		Environment
Browser Google Chrome

Account  user=standart_user - pwd: secret_sauce
		Steps to Reproduce


	1. Login https://www.saucedemo.com/  page with credential
	2. Select  Product from products page
	3. Click ADD TO CART button
	4. Click on Items Icon 
	5. Click RESET APP STATE

		Expected Result
Counter of Cart Icon should be  refresh to empty
List of product selected before should return to  ADD TO CART state
		Actual Result
Counter of Cart Icon  refresh to empty
List of product selected before keep as  selected 
		Visual Proof (screenshots, videos, text)	


		Severity/Priority
Mayor

		Title
it is possible to add an order without products
		Environment
Browser Google Chrome

Account  user=standart_user - pwd: secret_sauce
		Steps to Reproduce


	1. Login https://www.saucedemo.com/  page with credential
	2. Click Cart Icon 
	3. Click CHECKOUT button
	4. Input data in the form
	5. Click CONTINUE button
	6. Click Finish button
		Expected Result
It should not be possible to add an order without products, the order must have at least one product
		Actual Result
it is possible to add an order without products
		Visual Proof (screenshots, videos, text)	



		Severity/Priority
Mayor



Test Cases


id
TCS-1
Title
Functional- add multiple products to cart
Descriptio
validate that product add to car successfully
Project
SWAGLABS
Prerequisites
Standar Credentials: user=standart_user - pwd: secret_sauce
Steps

#
Action
Data
Expected Result
Status
Notes
1
Login https://www.saucedemo.com/ page with credential
url https://www.saucedemo.com/
Loging successfully


2
Select Product from products page




3
Click ADD TO CART button

the number of Car Icon must be increased plus one








Expected Result
Products added to cart successfully





id
TCS-2
Title
Functional- Add new Order
Descriptio
validate that order is added successfully
Project
SWAGLABS
Prerequisites
Standar Credentials: user=standart_user - pwd: secret_sauce
Steps

#
Action
Data
Expected Result
Status
Notes
1
Login https://www.saucedemo.com/ page with credential
url https://www.saucedemo.com/
Loging successfully


2
Select Product from products page




3
Click ADD TO CART button

the number of Car Icon must be increased plus one


4
Click Cart Icon

List of pproduct display in the cart page


5
Click CHECKOUT button

CHECKOUT: YOU INFORMATION page display


6
Input data in the form
Fist Name = Abel - Last Name = Mallcu - ZIP/Postal Code = +591



7
Click CONTINUE button

CHEKOUT: OVERVIEW Page display


8
Click Finish button

CHEKOUT: COMPLETE! text is display in the page


Expected Result
ORDER add successfully




id
TCS-3
Title
Functional- Cancel Order
Descriptio
validate that order is canceled
Project
SWAGLABS
Prerequisites
Standar Credentials: user=standart_user - pwd: secret_sauce
Steps

#
Action
Data
Expected Result
Status
Notes
1
Login https://www.saucedemo.com/ page with credential
url https://www.saucedemo.com/
Loging successfully


2
Select Product from products page




3
Click ADD TO CART button

the number of Car Icon must be increased plus one


4
Click Cart Icon

Listof pproduct display in the cart page


5
Click CHECKOUT button

CHECKOUT: YOU INFORMATION page display


6
Input data in the form
Fist Name = Abel - Last Name = Mallcu - ZIP/Postal Code = +591



7
Click CONTINUE button

CHEKOUT: OVERVIEW Page display


8
Click Cancel button

redirect to PRODUCTS Page display


Expected Result
ORDER Canceled successfully



