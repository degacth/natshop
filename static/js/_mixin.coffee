_.mixin
  log: console.log.bind console
  int: (v) -> parseInt v
  a: (decorator, f) -> decorator f
