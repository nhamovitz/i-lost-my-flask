**[click here for project log](https://docs.google.com/document/d/15nM9X0eWFdvy0PJBg230Rwo3XFstrA24aJVE9tW1lio/edit#)**

---

## TODO
- validation (ideally both client- and server- side) that the date given isn't in the future (or too far in the past?)
- stop it from breaking if server-side required-fields-exist validation fails and it does the `flash`.

- [modals for an item view instead of a separate `/item/<int:id>` route](https://docs.google.com/document/d/15nM9X0eWFdvy0PJBg230Rwo3XFstrA24aJVE9tW1lio/edit#heading=h.go2a2g6fa62b)

- :check: implement contacting the author
  - a `mailto:`, but there's no accounts, so that's really all you get!
  - .. guess I could make the UI a little clearer.. (?)
- implement auto-emailing

- implement matching lost and found items based off similar content in descriptions
  - when you resolve one, aggregate the list of all the other ones, from most-to-least likely to be the complement, and ask if you'd like to resolve any of those as well

- fix the font sizes, they're a little all over the place (esp in the submission form)

- (maybe) implement template inheritance - `import`, `include`, or `macro` - to replace the replication of the item 'preamble'

- 'where is this particular found item?' stuff (stashed under `current_loc`)
  - add a required question just to the 'found' form
  - validate that it's null if it's a 'lost' item and that it's present if it's a found item
  - insert `TEXT` into the database
  - deal with display somehow

- add the wireframe sketches referenced in the project log as "(Fig 1)" to the repo