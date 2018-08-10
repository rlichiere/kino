
# TODO stuff

Roughly up to date TODOs, ideas, etc.


## Features

### Required
* catalog : create models views for users:
  * create/edit models (Items, Locations, Addresses, etc)
* create a `location` module to manage geographic places
  * `Location`
  * `PostalAddress`
  * `GPSAddress`
  * `RoadbookAddress`
    * `RoadbookStep`
* create a `people` module to manage persons mechanisms
  * Participant
    * represents a participant
    * optional OneToOne with User (to be able to log in the site, or not)
    * exposes a list of Capacities
    * a Participant can be assigned to several tasks in several projects
  * Capacity
    * represents a capacity exposed by participants, and/or required for projects tasks
* create a `project` module to allow people to manage their projects:
  * project's Phases
    * define project phases (ex: Writing, Preprod, Prod, PostProd, etc)
  * project's Tasks
    * create project's tasks (ex: find a scenery, build or buy an accessory)
    * define tasks required capacities
    * distribute tasks among phases
  * project's People
    * search/book/assign people to tasks according to capacities
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
* implement a data exporter (database -> .yaml)
  * this will be usefull to backup data and prepair datasets for tests 



## Refactor

* refactor ItemPicture as a PictureGallery
  * is a list of Pictures
  * ranked
  * all Item models should expose a PictureGallery
* implement a highlevel class to expose structural tools as interfaces
  * logger
  * config accelerators
  * ... ?
