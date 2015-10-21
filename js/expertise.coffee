---
---
expertise =
  select: (category) ->
    $('#categories a.active').removeClass('active')
    $(category).addClass('active')
    $('#skills ul').addClass('hidden')
    $(category.dataset.target).removeClass('hidden')

$ ->
  $('#categories a').click (ev) ->
    ev.preventDefault()
    expertise.select(this)

  expertise.select($('#categories a')[0])
