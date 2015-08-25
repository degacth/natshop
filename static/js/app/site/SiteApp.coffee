angular.module 'Site', ['Catalog', 'Customer', 'FeedbackApp']

.factory 'httpInterceptor', ($q) ->
  request: (config) -> config or $q.when config

  response: (response) ->
    if response.data._success
      alert response.data._success, 'success'
      delete response.data._success
      check_redirect response.data

    response or $q.when response

  responseError: (response) ->
    alert error = if response.data._error then response.data._error else response.status
    $q.reject response

.config ($httpProvider) -> $httpProvider.interceptors.push 'httpInterceptor'

alert = (text, type='danger') ->
  UIkit.modal.alert alert_text({text: text, type: type}), center: true

check_redirect = (obj) -> if obj._redirect then $(document).one 'hide.uk.modal', -> window.location.href = obj._redirect

alert_text = _.template '''
  <p class="uk-text-<%- type %>">
    <%- text %>
  </p>
'''
