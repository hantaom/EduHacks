//workbcjobs.api.gov.bc.ca/v1
var rp = require("Request-Promise-Native");
var PythonShell = require('python-shell');


// var url = "https://catalogue.data.gov.bc.ca/api/action/datastore_search?resource_id=df92bf55-45b2-42a3-b5a8-6d2857df2ffe&limit=500"
// var options = {
//   url: url,
//   headers: {
//     'User-Agent': 'Request-Promise-Native'
//   },
//   // body: {
//   //   id: 1,
//   //   Caption: "Full-time"
//   // },
//   // json: true
//
// };
//
//
// rp(options).then(function (ret) {
//
//   console.log(JSON.parse(ret)['result']['records']);
//
//
//
// });

var options = {
  args: ['--field 0 --education 0']
};

PythonShell.run('parsedata.py', function (err, data) {
  if (err) throw err;
  console.log(data);
});

