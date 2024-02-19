# restaurant_inspection_system

Restaurant Inspection System:

CRUD apis:

1. Create Restaurant Score:
Endpoint: POST /api/restaurants
	Request Body:
	json
	{
  		"business_name": "Example Restaurant",
  		"business_address": "123 Main St",
  		"business_city": "San Francisco",
  		"business_state": "CA",
  		"business_postal_code": "94101",
  		"business_latitude": 37.7749,
  		"business_longitude": -122.4194,
  		"business_phone_number": "123-456-7890",
  		"inspection_id": "12345",
  		"inspection_date": "2023-01-15T12:00:00Z",
  		"inspection_score": 90,
  		"inspection_type": "Routine",
  		"violation_id": "V123",
  		"violation_description": "Missing handwashing station",
  		"risk_category": "High"
	}
	
	Response:
	Status Code: 201 Created
	Body: The created restaurant object

2. Read Restaurant Score:
Endpoint: GET /api/restaurants/{business_id}
	Response:
	Status Code: 200 OK
	Body: Restaurant object matching the provided business_id

	Example Response Body:
	json

	{
  		"business_id": "12345",
  		"business_name": "Example Restaurant",
  		"business_address": "123 Main St",
  		"business_city": "San Francisco",
  		"business_state": "CA",
  		"business_postal_code": "94101",
  		"business_latitude": 37.7749,
  		"business_longitude": -122.4194,
  		"business_phone_number": "123-456-7890",
  		"inspection_id": "12345",
  		"inspection_date": "2023-01-15T12:00:00Z",
  		"inspection_score": 90,
  		"inspection_type": "Routine",
  		"violation_id": "V123",
  		"violation_description": "Missing handwashing station",
  		"risk_category": "High"
	}

3. Update Restaurant Score:
Endpoint: PUT /api/restaurants/{business_id}
	Request Body:
	Same format as the Create endpoint
	
	Response:
	Status Code: 200 OK
	Body: Updated restaurant object

4. Delete Restaurant Score:
Endpoint: DELETE /api/restaurants/{business_id}
	Response:
	Status Code: 204 No Content
	
5. Additional Endpoint for Tagging Outdated Restaurants:
Endpoint: POST /api/restaurants/{business_id}/tag-outdated
	Response:
	Status Code: 200 OK
	Body: Updated restaurant object with a flag indicating it's outdated

These endpoints provide basic CRUD functionality for managing restaurant scores. Depending on the requirements, additional endpoints for searching/filtering restaurants, pagination, or authentication/authorization can be added. Additionally, proper validation and error handling should be implemented to ensure data integrity and security.




Arcihtectural choices and tradeoffs:

1. Database

	•I will use simple relational database for storing the the information about restaurants and their ratings. 
	We can simple Relational database service like AWS's Aurora Postgres service, which is managed database of AWS. It comes with below features.
	
	PROs:
	•If we use relational database we can easily extend it to add other metadata information like ( Each of below can be its own table )
		a. Location of restaurant
		b. Inspector information of the restaurant
		c. Restaurant metadata ( like the menu details, employee data )   
	• Automatic fail-over
	• Backup and Recovery
	• Isolation and security
	• Industry compliance
	• Push-button scaling
	• Automated Patching with Zero Downtime
	• Advanced Monitoring
	• Routine Maintenance
	• Backtrack: restore data at any point of time without using backups
	• RDS proxy: A proxy service for connection pooling and load balancing across multiple read and write replicas of DB.

	CONs:
	• In case the Database does not involve lot of relations spanning across multiple different type of tables. Then we might have to switch back to non-relational database service 	like mongoDB or DynamoDB 

2. API Service

	•I will use Contenarized service distributed across multiple regions of same country. If the service is PAN-national, I will deploy my service to multiple countries across the 	world. Ex. AWS's Elastic container service.

	PROs:
	• Multi-region setup can be enabled.
	• Better availaibility in case of failure of one region or one zone of the region.
	• Automatic recovery in case once instance of container goes down by specifying max and min available service instances that run at a time.
	• We can enable automatic scaling based on CPU or memory usage of whole cluster of containers.
	• Blue-Green or rolling deployment to maximize availability at the time of deployment.

3. Load balancer

	• A simple load balancer service like AWS's Application Load balancer can be used to make sure the load is distributed across the different containers.


4. Authentication and Authorization

	• I will use TLS 1.3 security certificate for transport layer security issued by any reliable global authorities like godaddy.com or Digicert to protect our APIS.
	• Also I will use HTTP/3 which is quic over UDP application layer protocol for reduced latency and improved congestion control.


	PROs:	
	• TLS 1.3 is modern and latest version of transport layer security to make sure that all traffic to our service APIs is encrypted.

5. CI(continuous Integregration) and CD(Continuous deployment):
	• CI
		1. In the Continuous integration stage all the unit-tests, performance tests and integration tests should be run and evidences should be uploaded at appropriate propritery 		application to maintain the sanity of production deployments.
		2. We should configure our pipeline to do Open source scans, vulnerability scans and security scans which will make sure that we are commiting a secure code and the open 		source package we are using do not contain any security issues.
	• CD
		1. I will use blue-green strategy or rolling updates strategy to make sure that our service is always up during deployment time as well.

6. Infrastructure:
	• To maintain our infrastructure I will use something like cloudformation or AWS's Cloud developement kit ot Terraform so that all the infrastrure can be reliably maintained 	and 	deployed across multiple environments such as Dev, UAT, PROD.
	

7. Code language:
	• Since this is just simple API service which should be available only to limited amount of users across the world. I will use simple python api framework like flask or django.
	• For example. Instagrams backend service still runs on python backend which serves millions of users across the world.
	• If I would do something differnt in the code-base, I would have used something like Java springboot which is enterprise level framework for building APIS.

8. Database Schema Creation tool:
	• In order to deploy our Database schemas across multiple environments reliably, I would use some schema creation and maintainance tool like Liquibase or Alembic. So that we can	maintain migration files to keep our database always updated to latest versions.

9.Testing:
	1. Make sure all the unit-tests are writen with minimum code coverage of 80%
	2. Since this backend API service make sure you do load testing or performance testing to make sure that your APIs are able to handle estimated amount of load.
	3. Write integration tests to make sure in case there are multiple components dependent on each other they are thoroghly tested.
	
	
