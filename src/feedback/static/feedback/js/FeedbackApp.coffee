angular.module "FeedbackApp", ['ngResource', 'vcRecaptcha']


.controller "FeedbackFormController", ($scope, Feedback) ->
  angular.extend $scope,
    feedback: {}
    messages: {}

    submit: -> (new Feedback @feedback).$save().then -> $scope.feedback.submitted = yes

    captcha_success: (res) -> $scope.feedback.captcha = res


.factory 'Feedback', ($resource) ->
  $resource "#{window.ng_config.api}/feedback/:id", id: "@id", {}, {stripTrailingSlashes: false}
