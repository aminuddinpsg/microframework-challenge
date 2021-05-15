# Introduction

Micro-Web-Framework Challenge using Flask for Python to upload picture using REST service

## Getting Started

To get started, you'll want to first clone this GitHub repository locally:

```bash
$ git clone https://github.com/aminuddinpsg/microframework-challenge.git
```
Next, you'll want to go into the sample app directory:

```bash
$ cd microframework-challenge
```

Then you'll want to install all of the Python requirements (via
[pip](http://pip.readthedocs.org/en/latest/)):

```bash
$ pip install -r requirements.txt
```
Using the following command to run the app in local
```bash
$ py -m venv env
$ env\Scripts\activate
$ set FLASK_APP=app.py
$ flask run --host=localhost --port=8080
```

To close the virtual environment run the following command
```bash
$ deactivate
```

## Upload using picture

The endpoint serve to upload a picture.

```http
POST /api/picture
```
## Upload using zip file

The endpoint serve to upload a zip file.

```http
POST /api/zip
```

## Generate thumbnails

The endpoint serve to generate thumbnail.

```http
POST /api/thumbnail
```
## Request Body

| Body | Type | Description |
| :--- | :--- | :--- |
| `file` | `multipart/form-data` | key to pass file format like picture |

## Responses

Upon successfully request the app returns a JSON response in the following format: 

```javascript
{
  "url" : string
}
```

Upon unsuccessfully request the app returns a JSON response in the following format: 

```javascript
{
  "msg" : string
}
```

Upon successfully request with mutliple pictures in a zip file or thumbnails creation the app returns a JSON response in the following format: 

```javascript
[
  {
    "url" : string
  },
  {
    "url" : string
  } ..
]
```

Upon unsuccessfully request with mutliple invalid pictures format in a zip file the app returns a JSON response in the following format: 

```javascript
[
  {
    "msg" : string
  },
  {
    "msg" : string
  } ..
]
```

The `url` attribute contains a permanent link for uploaded picture

The `msg` attribute contains a error message for failed request

## Status Codes

The app returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

