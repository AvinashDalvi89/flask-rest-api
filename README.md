# flask-rest-api
This is REST API developed using python flask framework. To get data from database using GET method. 

## General guidelines for API 

* A URL identifies a resource.
* This REST API only allow GET method ( other method POST, PUT,PATCH, DELETE doesn't work).
* lookup parameter is mandatory to work. Length of lookup parameter should be more than 3 characters
* species parameter is non mandatory. It not pass API will work. 
* This API will in website or UI to build search functionality with additional parameters

API with all parameters : 
http://localhost:5000/api/v1.0/genes?lookup=brc&species=homo_sapiens

API with single parameter: 
http://localhost:5000/api/v1.0/genes?lookup=brc

## Error handling

Error responses should include a common HTTP status code, message for the developer, message for the end-user (when appropriate), internal error code (corresponding to some specific internally determined ID), links where developers can find more info. For example:

    {
      "status" : 400,
      "error" : "Search string length should be more than 3 characters"
    }

Use three simple, common response codes indicating (1) success, (2) failure due to client-side problem, (3) failure due to server-side problem:
* 200 - OK
* 400 - Bad Request
* 500 - Internal Server Error
* 405 - Method not found

### GET /genes

Example: http://example.com/api/v1.0/genes?lookup=brc&species=homo_sapiens

Response body:

    {
      [
        {
            "db": "core",
            "display_label": "brca2",
            "location": "NXFZ01006270.1:1008811-1022372",
            "species": "amphiprion_ocellaris",
            "stable_id": "ENSAOCG00000009260"
        },
        {
            "db": "core",
            "display_label": "brcc3",
            "location": "NXFZ01003698.1:30108-30983",
            "species": "amphiprion_ocellaris",
            "stable_id": "ENSAOCG00000004487"
        },
        {
            "db": "core",
            "display_label": "brcc3",
            "location": "16:32648577-32649452",
            "species": "amphiprion_percula",
            "stable_id": "ENSAPEG00000020392"
        }
    }


## Application run guidelines :
* Install flask pytho https://pypi.org/project/Flask/

         pip install Flask
* open terminal and go to project run
* run command
    python run.py
* This API has been testing using curl and postman code will not depend on any external library. Required library is already added in project folder. This can work in any environment.Can make database configuration based on enviroment by adding db.config. Keeping db-local.config, db-stage.config and db-prod.config. In each enviroment creating symbolic link to db.config to respective configuration file. 

        ln -s db.config db-local.config -- local 
        ln -s db.config db-stage.config -- stage
        ln -s db.config db-prod.config -- production

## Postman Request 

https://www.getpostman.com/collections/c9ad6e22e1c53b4572fb

## Versions

* V1.0
