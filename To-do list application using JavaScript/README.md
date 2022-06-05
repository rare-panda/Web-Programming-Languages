Web Programming Languages
Due Date: July 16, 11:59PM
Complete Flask To-do List application by implementing all CRUD (Create, Read, Update, Delete) operations. Functions that needs to be completed are:
	User signup
	User sign in
	For registered users 
o	add a new to-do item
o	list all to-do items (title, description, complete/incomplete)  
o	edit to-do items (change title and description, mark as completed)
o	delete to-do items 
Signup and signin functions have already been implemented and source code is provided under Hands-on folder.  Add new item is also demonstrated but you will need to follow along the video and write the code yourself. You will implement remaining functionalities from scratch.
On listing page, along with each item information, provide buttons (or links) for edit and delete. For marking items as completed, you will need to add a new boolean attribute to table tbl_todo (column name: isComplete, datatype: boolean/tinyint, values: 0,1). When a new item is created, it will take default value of 0.
More details
1. The form for edit page should be pre-loaded with existing data from database.  Input fields should not be initially blank. 
 
2. IDs for todo items will be different from item numbers (1, 2, 3, …) displayed on listing page. You will need IDs for edit and delete. 
 
3. A checkbox on edit page would suffice to mark the item as completed. You do not need to mark the item as completed on homepage (listing page).

5. Have a separate file for database connection parameters (username, password, port number etc.) and keep in under parent directory of your application files. (../config.py)


Deliverables:
	Screenshots for each function listed above
	Application source code (zipped)
You will send complete application code/folder.
Important note: Database table names and attribute names should match with the names used in hands-on videos. You will not send your database files and TAs will assume you have exact same structure/schema for the database. 


