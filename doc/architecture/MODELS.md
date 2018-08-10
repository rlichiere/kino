
## Leafs models

* Country



## Address models

* PostalAddress
* GPSAddress
* RoadbookAddress
  * RoadbookStep


## Location

Represents a geographical location.
Can be composed of :
- 0,1 PostalAddress
- 0,1 GPSAddress
- 0..N RoadbookAddress


## Contact

Represents a person.
Contains all information required to contact that person.


## Item

* ItemCategory
* Item
* ItemPicture
