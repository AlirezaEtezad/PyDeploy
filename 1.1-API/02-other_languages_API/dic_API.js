var settings = {
  "url": "https://api.ditionaryapi.dev/api/v2/entries/en/hello",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});