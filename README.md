Here we go for today's number. Ten balls; each ball has a number; numbers one through ten. Swirl the numbers. Pick a number. Today's number is...

## Number Attributes
| Attribute | Type   | Description             | 
| :-------- | :----- | :---------------------- |
| date      | string | Date in ISO 8601 format |
| number    | int    | Number of the day       |
| url       | string | URL of video            |

## Endpoints
### Get todays number
`/api`
### Get day's numbers
`/api/2020/08/17`
### Get month's numbers
`/api/2020/08`
### Get year's numbers
`/api/2021`

## Response
Request will return a JSON object.
```json
{
    "numbers": [
        {
            "date": "2020-08-17",
            "number": 8,
            "url": "https://youtu.be/W-3MP27IU-I"
        },
        {
            "date": "2020-08-18",
            "number": 3,
            "url": "https://youtu.be/c9jFcIwEQ3k"
        },
    ]
}
```
