###
fixed_menu = $ '#fixed-menu'

$ window
.scroll ->
  top_class = 'on-top'
  $a = $ @
  pos = Math.max(0, 169 - $a.scrollTop())

  fixed_menu
  .css 'top', pos

  if pos then fixed_menu.removeClass top_class else fixed_menu.addClass top_class
.trigger 'scroll'
###
