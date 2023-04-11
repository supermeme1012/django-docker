# The Breaking Bad API task

The idea is to create a simple platform for DEA agents, to manage information about characters from the Breaking Bad/Better Call Saul universe. To make the DEA agents' life easier, they need to have an API endpoint that allows filtering information about characters by their name, date of birth, occupation or the fact whether they are a suspect.

As the DEA is trying to put drug lords behind bars, they are tracking their, and the people around them location. They store timestamps and particular locations as geographical coordinates in a related table. The endpoint that will expose the data needs to allow filtering of location entries, that were within a specific distance from a particular geographical point, as well as who they were assigned to, and the datetime range of when they were recorded. The ordering for this endpoint should allow taking into consideration distance from a specified geopraphical point, both ascending and descending.

## Requirements

Requirements of the project are as follows:

* Have a docker-compose setup for the product. There should be no need for external services to be installed in the local machine to be able to run the application.
* There are no requirements when it comes to database; any suitable can be used.
* You can use any extra library you want, but web framework to be used should be Django. 
* The data about characters should be stored in the local database. You can choose which fields are needed to fulfil the requirements of this task.
* The application needs to expose two API endpoints, one to manage the character data, and the other for their location entries. Read on for more information about the specific endpoints.

### Characters endpoint

It should allow to:
* List information about characters
* Create new entries
* Retrieve, modify and delete entries from local database
* Filter by name, suspect status and occupation. Filters should allow partial matches and be case-insensitive
* Order by name and date of birth. The only requirement to structure of the url is to use the `orderBy` keyword along with `ascending` one to manipulate the sorting order. `orderBy` will take the name of the field and the value of `ascending` will determine what is the direction of ordering, where `0` means descending and `1` means ascending.

### Location entries endpoint

It should allow to:
* List information about location entries
* Create new entries
* Retrieve, modify and delete entries from local database
* Show only those location entries that are within the given distance (in meters) from the specific geographical point provided as a pair of geographical coordinates.
* Filter by character assigned to specific location entry and datetime range that they were recorded within.
* Order location entries by distance from specific geographical point, both ascending and descending.

### Documentation

Documentation is a must! It should explain how to run the project and how to access the data required. It should show what the endpoints are and how they should be used, including what filters are available, and how the data can be ordered with examples of usage. One should not need to look into the code of the application to figure out how to use it.

### Additional notes

* At this stage of the proof of concept there is no need for authentication and permission management; data can be accessed and manipulated by anonymous users.
* Application will be run in local environment only, the built-in Django's server is all that is needed.

## Getting started

To get started, the initial project skeleton, along with a simple docker-compose setup was provided. In order to have the initial site up and running you should have [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/install/) installed on your computer, and run the following commands from the root of the project:

```bash
docker-compose build
docker-compose up
```

Browsing to `http://localhost:8000` should show Django's default "launching rocket" page.
