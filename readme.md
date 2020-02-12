# Items to discuss

## HTTP methods
- GET without an id - get or search objects
- GET with an id - get an object
- POST without an id - create a new object
- PUT with an id - make changes to an existing object
- DELETE with an id - delete an object

## Overall flow of HTTP

- Request object
  - Method
  - Path
  - Parameters
  - Body as JSON or urlencoded
- Response object
  - Headers
  - Status code: 200, 404, etc.
  - Body encoded as JSON

## Permissions:
- Change settings.py to AllowAny in the REST_FRAMEWORK section

## Models:
- Review models.py
- makemigrations and migrate
- Running a Django-enabled script

## Serializers
- Convert an object to a JSON structure and back

## Views:
- Different ways to do it. We're going to use class-based views
- urls.py maps browser urls to views
- Use PostMan app to test an API
