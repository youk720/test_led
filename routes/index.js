var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
router.get('/led', function(req, res, next){
  res.send(global_val);
});

module.exports = router;
