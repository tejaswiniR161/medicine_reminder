const gTTS = require('gtts');
      
var speech = "you did not take your medication, Alerting your caretaker!";
var gtts = new gTTS(speech, 'en');
  
gtts.save('./audio/alert.mp3', function (err, result){
    if(err) { throw new Error(err); }
    console.log("Text to speech converted!");
});