$(document).ready(function() {var formatter = new CucumberHTML.DOMFormatter($('.cucumber-report'));formatter.uri('demosmart\smartin.feature');
formatter.feature({
  "line": 1,
  "name": "Login Functonality",
  "description": "",
  "id": "login-functonality",
  "keyword": "Feature"
});
formatter.scenario({
  "line": 3,
  "name": "Successful Login with Valid Credentials",
  "description": "",
  "id": "login-functonality;successful-login-with-valid-credentials",
  "type": "scenario",
  "keyword": "Scenario"
});
formatter.step({
  "line": 4,
  "name": "User is on Home page",
  "keyword": "Given "
});
formatter.step({
  "line": 6,
  "name": "User enters Credentials to Login",
  "rows": [
    {
      "cells": [
        "Tester",
        "test"
      ],
      "line": 7
    }
  ],
  "keyword": "When "
});
formatter.step({
  "line": 8,
  "name": "message displayed Login Successful",
  "keyword": "Then "
});
formatter.match({});
formatter.result({
  "status": "undefined"
});
formatter.match({});
formatter.result({
  "status": "undefined"
});
formatter.match({});
formatter.result({
  "status": "undefined"
});
});