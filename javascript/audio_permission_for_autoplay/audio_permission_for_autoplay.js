var AudioContext
var audioContext
window.onload = function() {
    navigator.mediaDevices.getUserMedia({audio: true}).then(()= > {AudioContext = window.AudioContext | | window.webkitAudioContext
        audioContext= new AudioContext()
    }).catch(e = > {console.error(`Audio permissions denied: ${e}`)
    })
}
