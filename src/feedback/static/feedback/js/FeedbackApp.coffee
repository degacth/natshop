angular.module "FeedbackApp", ['ngResource', 'vcRecaptcha']


.controller "FeedbackFormController", ($scope, Feedback) ->
  angular.extend $scope,
    feedback:
      username: 'Alexander'
      phone: '9113322'
      email: 'degacth@yandex.ru'
      message: 'lorem ip sum'
    messages: {}

    submit: -> (new Feedback @feedback).$save().then -> $scope.feedback.submitted = yes

    captcha_success: (res) -> $scope.feedback.captcha = res


.factory 'Feedback', ($resource) ->
  $resource "#{window.ng_config.api}/feedback/:id", id: "@id", {}, {stripTrailingSlashes: false}
