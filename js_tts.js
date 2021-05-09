const gTTS = require('gtts');
      
var speech = "Time for you to take your meds. Please tap on the touch sensor on the side of the box to let us know!";
var gtts = new gTTS(speech, 'en');
  
gtts.save('./audio/timeformeds.mp3', function (err, result){
    if(err) { throw new Error(err); }
    console.log("Text to speech converted!");
});