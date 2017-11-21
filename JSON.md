# Contents

# Resources & references
- Wikipedia: [JSON](https://en.wikipedia.org/wiki/JSON)
- Copter Labs: [JSON: What It Is, How It Works, & How to Use It](https://www.copterlabs.com/json-what-it-is-how-it-works-how-to-use-it/)
- [json.org](json.org)
- The [json](https://docs.python.org/3/library/json.html) module from the Python standard library
- A JSON validator: [JSONLint](https://jsonlint.com/)
- See also: the [standards](#Standards-specification) section below

# Overview
- JavaScript Object Notation (JSON) is a lightweight data-interchange format that uses human-readable text to **transmit data objects** consisting of **attribute–value pairs** and **array data types**. (more below)
- JSON is a language-independent data format. It was derived from JavaScript, but many programming languages include code to generate and parse JSON-format data.
- JSON filenames use the extension `.json`.

# Construction
- A _collection of_ **attribute/value pairs** (name/value pairs). In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.
- An **ordered array of values**. In most languages, this is realized as an array, vector, list, or sequence.

# Standards specification
- Douglas Crockford developed JSON (first message was the early 2000s), and first [specified](http://www.ietf.org/rfc/rfc4627.txt?number=4627) the JSON format in 2006.
    - Crockford is the maintainer of [json.org](json.org).
- Two competing standards made updates in 2013:
    - [ECMA 404](http://www.ecma-international.org/publications/files/ECMA-ST/ECMA-404.pdf) - this standard is linked to by json.org.
    - [RFC 7159](https://tools.ietf.org/html/rfc7159) - developed by the IETF.  This obsoletes RFC 4627.
    - The ECMA standard describes only the allowed syntax, whereas the RFC covers some security and interoperability considerations.  RFC 7159 cleans up some ambiguities and inconsistencies in various JSON definitions, none of which caused any real-world pain.
    - For more detail see ["JSON Redux AKA RFC7159"](https://www.tbray.org/ongoing/When/201x/2014/03/05/RFC7159-JSON) by Tim Bray.

# Examples
The following example shows a possible JSON representation describing a person.

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
