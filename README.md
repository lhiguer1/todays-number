# Today's Number
Here we go for today's number. Ten balls; each ball has a number; numbers one through ten. Swirl the numbers. Pick a number. Today's number is...

## Number Attributes
| Attribute  | Type   | Description                                         | 
| :--------  | :----- | :-------------------------------------------------- |
| date       | string | Date in ISO 8601 format                             |
| number     | int    | Number of the day                                   |
| url        | string | URL of video                                        |
| transcript | string | Transcript obtained using Google Speech Recognition | 

### Endpoints
#### Base URL
`https://todays-number.herokuapp.com/api/numbers/`
#### Get all numbers
`/api/numbers/`
#### Get year's numbers
`/api/numbers/2021/`
#### Get month's numbers
`/api/numbers/2020/08/`
#### Get day's numbers
`/api/numbers/2020/08/17/`

#### Create a new number
Accounts with permissons can make POST, PUT, PATCH, and DELETE requests on the days number endpoint. However, any updates to the number are unlikely unless there is an update to a past number.
```json
// Content
{
  "number": 8,
  "url": "https://youtu.be/W-3MP27IU-I",
  "transcript": "here we go for today's n…ain today's number is 8"
}
```

### Examples
#### List of numbers
```json
[
  {
    "date": "2020-08-17",
    "number": 8,
    "url": "https://youtu.be/W-3MP27IU-I",
    "transcript": "here we go for today's n…ain today's number is 8"
  },
  {
    "date": "2020-08-18",
    "number": 3,
    "url": "https://youtu.be/c9jFcIwEQ3k",
    "transcript": "here we go for today's n…ber today's number is 3"
  },
  ...
]
```

### Single number
```json
{
  "date": "2020-08-17",
  "number": 8,
  "url": "https://youtu.be/W-3MP27IU-I",
  "transcript": "here we go for today's n…ain today's number is 8"
}
```