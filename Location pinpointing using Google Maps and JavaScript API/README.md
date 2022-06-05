Web Programming Languages 

Due Date: July 23, 11:59PM

- In this assignment, you will show your favorite restaurants and cafes on Google Map using Maps JavaScript API. 
- You will store your favorite restaurants/cafes in MySQL database and will make an AJAX call to a Python/Flask script when the html page is loaded.
  Python script will return the results in JSON form and you will parse the results and use each address information (latitude and longitude) for marking the location on the map.
- For each marker, create an info window that will display name and address information when clicked on the marker.
- You can center the map around your favorite city and manually insert 5-10 different markers (favorite restaurants and cafes in/around the chosen city) into the database table. 


Database name: FavoritePlaces
Table name: Restaurants

 

You can also use below SQL command to create the table.
	CREATE TABLE `Restaurants` (
  		`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  		`name` VARCHAR( 60 ) NOT NULL ,
  		`address` VARCHAR( 80 ) NOT NULL ,
  		`lat` FLOAT( 10, 6 ) NOT NULL ,
  		`lng` FLOAT( 10, 6 ) NOT NULL ,
  		`type` VARCHAR( 30 ) NOT NULL
	) ENGINE = MYISAM ;

Type will have values “restaurant” and “cafe”.


Solution hint:

You can use jsonif() function in Flask to convert database query results into JSON.

	from flask import jsonify

	rows = cursor.fetchall()
	response = jsonify(rows)
	return response

and JSON.parse() function (in Javascript) to parse the results.


Deliverables:

Screenshot of the results
Source files —HW4-yournetid.zip
