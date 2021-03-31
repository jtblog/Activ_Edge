# NOTE
<hr>

### Question 3
This is a simple flask REST app that uses MongoDB.
I tested the api using POSTMAN

### app.py
Return json objects as responses and not just strings <br>
e.g. Any of the POST, PUT request gets json responses like this
```json
{
    "id" : 1,
    "name" : "Dow_Jones",
    "currentPrice" : 4789.00,
    "createDate" : 'datetimefield',
    "lastUpdate" : 'datetimefield'

}
```
except for the get request that gets all stocks

while GET request get json responses like those of the 
body schemas/models represented at the bottom of this markdown <br>

<br>
To use app.py <br>
Set the current flask app to alt.py <br>
Run the commands <br>

```bash
> set FLASK_APP=app.py
```
```bash
> flask run
```

<hr>

## Endpoints
<br>

```bash
'/api/stocks'  --  method = POST
```
```bash
'/api/stocks/<id>' --  method = PUT
```
```bash
'/api/stocks'  --  method = GET
```
```bash
'/api/stocks/<id>'   --  method = GET
```

<hr>

## Body Schemas/Models
### Stocks:
```json
{
    "id" : 1,
    "name" : "Dow_Jones",
    "currentPrice" : 4789.00,
    "createDate" : 'datetimefield',
    "lastUpdate" : 'datetimefield'
}
```
<hr>

# Thank you


### Question 1
Is a python script that returns the smallest of non occuring integer in any given array<br>

Run the command
```bash
> py minimum.py
```