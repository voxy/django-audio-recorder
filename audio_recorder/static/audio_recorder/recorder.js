var promise = navigator.mediaDevices.getUserMedia({audio: true, video: false});

var recordButton = document.getElementById('js-record-button');
var stopButton = document.getElementById('js-stop-button');
var audio = document.getElementById('js-audio');
var uploadSpan = document.getElementById('js-upload-span');
var audioFile = document.querySelectorAll('[data-django-audio-recorder]')[0];

promise.then(function(stream) {
  var recorder = new MediaRecorder(stream);
  recorder.chunks = [];

  recordButton.addEventListener("click", function(){
    recordButton.disabled = true;
    stopButton.disabled = false;
    audio.removeAttribute('src');
    recorder.start();
  });

  stopButton.addEventListener("click", function(){
    stopButton.disabled = true;
    uploadSpan.classList.remove('hidden');
    recorder.stop();
  });

  recorder.ondataavailable = function(e) {
    this.chunks.push(e.data);
  };

  recorder.onstop = function(event) {
    var blob = new Blob(this.chunks, {'type': 'audio/wav;'});
    this.chunks = [];
    var formData = new FormData();
    formData.append('audio_file', blob, "replace-me.wav");
    $.ajax({
        type: "POST",
        url: audioFile.dataset.url,
        data: formData,
        processData: false,
        contentType: false,
        success: function(data){
            uploadSpan.classList.add('hidden');
            recordButton.disabled = false;
            audioFile.value = data.id;
            audio.src = data.url;
        },
        error: function(jqXHR, textStatus, errorThrown){
            uploadSpan.classList.add('hidden');
            recordButton.disabled = false;
            console.error('jqXHR:', jqXHR);
            console.error('textStatus:', textStatus);
            console.error('errorThrown:', errorThrown);
        },
    });

  };

});

promise.catch(function(err) { console.log(err.name); });