angular.module "FeedbackApp", ['ngResource', 'vcRecaptcha']

.config ($httpProvider)->
#  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
  $httpProvider.defaults.headers.common['X-CSRFToken'] = window.ng_config.api.csrf;

.controller "FeedbackFormController", ($scope, FeedbackModel) ->
  angular.extend $scope,
    feedback: {}
    messages: {}

    submit: -> if @FeedbackForm.$valid
      @messages = {}
      fb = new FeedbackModel @feedback
      fb.$save (data) ->
        $scope.messages.success = 'Сообщение успешно отправлено'
      , (data) -> $scope.messages.errors = data.data

    captcha_success: (res) ->
      $scope.feedback.captcha = res

.factory 'FeedbackModel', ($resource) -> $resource "#{window.ng_config.api.url}/feedback/:id", id: "@id", {}, {stripTrailingSlashes: false}
