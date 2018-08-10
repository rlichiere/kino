
# TODO stuff

Roughly up to date TODOs, ideas, etc.


## Features

### Required
* catalog : create models views for users:
  * create/edit models (Items, Locations, Addresses, etc)
* improve `project` models admin pages
* improve `Project` model to allow people to manage their projects:
  * project's Items
    * create project's required items
    * search/book/use/release catalog's items
      * `book` and `use` can be `exclusive` or `shareable`
  * projects's Participations
    * represent the participation of a participant to a project, with a capacity
    * participation lifecycle
      * 2 entrypoints
        * a project manager invites a participant
        * a participant proposes itself to a project with a capacity
      * if the invitation/purposal is denied, the participation is cancelled
      * if the invitation/purposal is accepted, the participation is validated
      * both parts can request a cancellation of a valid participation.
        The reversed processed is then applied:
        * if the invitation/purposal is denied, the participation remains valid
        * if the invitation/purposal is accepted, the participation is cancelled

### Nice to have

##### Data exporter
* implement a data exporter (database -> .yaml)
  * this will be usefull to backup data and prepair datasets for tests 

##### RegExps
* implement regexps on model fields

##### fixtures
Define a generic way to distribute data models in categorized fixtures:
* each model should/can expose data according to fixture categories:
  * `minimum`: expose the minimum of data required for each model of module 
  * `realistic`: expose realistic data
  * `exhaustive`: expose data for all cases
  * `fat`: expose a bunch of data
* examples:
  * ```
    # /location/fixtures/country_minimum.yaml
    - model: location.country
      pk: 1
        fields:
            label: France
    ```
  * ```
    # /location/fixtures/country_realistic.yaml
    - model: location.country
      pk: 1
        fields:
            label: France
    - model: location.country
      pk: 2
        fields:
            label: Switzerland
    ```
  * ```
    # /location/fixtures/country_exhaustive.yaml
    - model: location.country
      pk: 1
        fields:
            label: A
    - model: location.country
      pk: 2
        fields:
            label: 1
    - model: location.country
      pk: 3
        fields:
            label: MoreExoticAndLongCountryNameInTheWorld
    ```
    
## Refactor

* refactor ItemPicture as a PictureGallery
  * is a list of Pictures
  * ranked
  * all Item models should expose a PictureGallery
* implement a highlevel class to expose structural tools as interfaces
  * logger
  * config accelerators
  * ... ?
