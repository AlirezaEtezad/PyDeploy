var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://fruityvice.com/api/fruit/peach',
  'headers': {
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
