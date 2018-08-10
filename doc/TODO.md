
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
* implement a data exporter (database -> .yaml)
  * this will be usefull to backup data and prepair datasets for tests 
* implement regexps on model fields



## Refactor

* refactor ItemPicture as a PictureGallery
  * is a list of Pictures
  * ranked
  * all Item models should expose a PictureGallery
* implement a highlevel class to expose structural tools as interfaces
  * logger
  * config accelerators
  * ... ?
