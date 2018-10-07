# Contents

# Resources & references
- Wikipedia: [JSON](https://en.wikipedia.org/wiki/JSON)
- Copter Labs: [JSON: What It Is, How It Works, & How to Use It](https://www.copterlabs.com/json-what-it-is-how-it-works-how-to-use-it/)
- [json.org](json.org)
- The [json](https://docs.python.org/3/library/json.html) module from the Python standard library
- A JSON validator: [JSONLint](https://jsonlint.com/)
- pandas' [read_json](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_json.html)
- See also: the [standards](#Standards-specification) section below

# Overview
- JavaScript Object Notation (JSON) is a lightweight data-interchange format that uses human-readable text to **transmit data objects** consisting of **attribute–value pairs** and **array data types**. (more below)
- JSON is a language-independent data format. It was derived from JavaScript, but many programming languages include code to generate and parse JSON-format data.
- JSON filenames use the extension `.json`.

# Standards specification
- Douglas Crockford introduced JSON in 2001 and first [specified](http://www.ietf.org/rfc/rfc4627.txt?number=4627) the JSON format in 2006.
    - Crockford is the maintainer of [json.org](json.org).
- Two competing standards made updates in 2013:
    - [ECMA 404](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf) - this standard is linked to by json.org.
    - [RFC 7159](https://tools.ietf.org/html/rfc7159) - developed by the IETF.  This obsoletes RFC 4627.
    - The ECMA standard describes only the allowed syntax, whereas the RFC covers some security and interoperability considerations.  RFC 7159 cleans up some ambiguities and inconsistencies in various JSON definitions, none of which caused any real-world pain.
    - For more detail see ["JSON Redux AKA RFC7159"](https://www.tbray.org/ongoing/When/201x/2014/03/05/RFC7159-JSON) by Tim Bray.

# General construction
- A _collection of_ **attribute/value pairs** (name/value pairs). In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
- An **ordered array of values**. In most languages, this is realized as an array, vector, list, or sequence.

# Data structures & types

Concise definitions are at [json.org](json.org).

There are six _structural tokens_ used to form JSON text:
1. `[`
2. `]`
3. `{`
4. `}`
5. `:`
6. `,`

And there are three _literal name tokens_ used within text, which must be lowercase:
1. `true`
2. `false`
3. `null`

**Whitespace is allowed** (ignored).

An **object** is an _unordered_ collection of keys-value pairs.
- The keys must be strings.
- It is recommended, but not required, that each key be unique.
- Objects are delimited with curly brackets, and use commas to separate each pair.

A **value** is fairly flexible; it can be:
- a string in double quotes,
- a number
- `true`, `false`, or `null`
- an object or an array

Values can be nested.

An **array** is an ordered collection of **values**; it is constructed with _brackets_ and comma-separated.

Some valid objects:

```json
{}
```

```json
{
    "field A": null,
    "subfields": {
        "sf1": true,
        "sf2": 25,
        "sf3": [1, 2, 3]
    }
}

# Examples

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": true,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    },
    {
      "type": "mobile",
      "number": "123 456-7890"
    }
  ],
  "children": [],
  "spouse": null
}
```

```json
{
  "id": 1,
  "name": "Foo",
  "price": 123,
  "tags": [
    "Bar",
    "Eek"
  ],
  "stock": {
    "warehouse": 300,
    "retail": 20
  }
}
```

```json
{
"Image": {
    "Width":  800,
    "Height": 600,
    "Title":  "View from 15th Floor",
    "Thumbnail": {
        "Url":    "http://www.example.com/image/481989943",
        "Height": 125,
        "Width":  100
    },
    "Animated" : false,
    "IDs": [116, 943, 234, 38793]
  }
}
```

Orered arrays of values ("records" format):

```json
[{
    "col 1": "a",
    "col 2": "b"
}, {
    "col 1": "c",
    "col 2": "d"
}]
```

```json
[
    {
       "precision": "zip",
       "Latitude":  37.7668,
       "Longitude": -122.3959,
       "Address":   "",
       "City":      "SAN FRANCISCO",
       "State":     "CA",
       "Zip":       "94107",
       "Country":   "US"
    },
    {
       "precision": "zip",
       "Latitude":  37.371991,
       "Longitude": -122.026020,
       "Address":   "",
       "City":      "SUNNYVALE",
       "State":     "CA",
       "Zip":       "94085",
       "Country":   "US"
    }
]
```
