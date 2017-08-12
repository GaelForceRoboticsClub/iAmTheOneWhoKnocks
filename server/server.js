var express = require('express');
var bodyParser = require('body-parser');
var exec = require('child_process').exec;
var app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// if anyone spams this get request, i WILL record your ip/mac address and look you up
// then i'll secure this route which will be incredibly annoying to do so pls don't
app.get('/notify', (req,res)=>{
	exec('python ../test/remind.py', (err,out,stderr)=>{
		if(err) throw err;
		if(stderr) throw stderr;
		res.json({ success: true, message: 'notified all robotics pepes'});
	});
});

app.listen(3000, ()=>{
	console.log('server running on port 3000');
});