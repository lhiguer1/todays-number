# Today's Number
Here we go for today's number. Ten balls; each ball has a number; numbers one through ten. Swirl the numbers. Pick a number. Today's number is...

## Number Attributes
| Attribute  | Type   | Description                                         | 
| :--------  | :----- | :-------------------------------------------------- |
| date       | string | Date in ISO 8601 format                             |
| number     | int    | Number of the day                                   |
| url        | string | URL of video                                        |
| transcript | string | Transcript obtained using Google Speech Recognition | 

### Base URL
`https://todays-number.herokuapp.com/api/numbers/`

### Query qarameters
Filter list by `today`, `yesterday`, `week`, `month`, `year`<br>
`/api/numbers/?date_range={today,yesterday,week,month,year}`

Get list of dates before/after specified date<br>
`/api/numbers/?date_after=2020-08-16`<br>
`/api/numbers/?date_before=2022-12-01`<br>
`/api/numbers/?date_after=2021-01-01&date_before=2021-02-01`

### Examples
#### List
`/api/numbers/`
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
  }
]
```

#### Singleton
`/api/numbers/2020-08-17`
```json
{
  "date": "2020-08-17",
  "number": 8,
  "url": "https://youtu.be/W-3MP27IU-I",
  "transcript": "here we go for today's n…ain today's number is 8"
}
```
#### Statistics
`/api/statistics/`
