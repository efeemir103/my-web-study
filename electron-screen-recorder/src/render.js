// Elements
const videoElement = document.querySelector('video');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const videoSelectButton = document.getElementById('videoSelectButton');
videoSelectButton.onclick = getVideoSources;
startButton.onclick = e => {
    mediaRecorder.start();
    startButton.classList.add('is-danger');
    startButton.innerText = 'Recording';
};
stopButton.onclick = e => {
    mediaRecorder.stop();
    startButton.classList.remove('is-danger');
    startButton.innerText = 'Start';
}

const { desktopCapturer, remote } = require('electron');
const { dialog, Menu } = remote;
const { writeFile } = require('fs');

let mediaRecorder; // MediaRecorder instance to capture footage.
const recordedChunks = [];


// Get the avaible video sources
async function getVideoSources() {
    const inputSources = await desktopCapturer.getSources({
        types: ['window', 'screen']
    });

    const videoOptionsMenu = Menu.buildFromTemplate(
        inputSources.map(source => {
            return {
                label: source.name,
                click: () => selectSource(source)
            };
        })
    );

    videoOptionsMenu.popup();
}

async function selectSource(source) {
    videoSelectButton.innerText = source.name;
    
    const constraints = {
        audio: false,
        video: {
            mandatory: {
                chromeMediaSource: 'desktop',
                chromeMediaSourceId: source.id
            }
        }
    }

    // Create a Stream
    const stream = await navigator.mediaDevices.getUserMedia(constraints);

    // Preview the source in a video element
    videoElement.srcObject = stream;
    videoElement.play();

    // Create Media Recorder
    const options = {mimeType: 'video/webm; codecs=vp9'}
    mediaRecorder = new MediaRecorder(stream, options);

    // Register Event Handlers
    mediaRecorder.ondataavailable = handleDataAvailable;
    mediaRecorder.onstop = handleStop;

}

// Captures all recorded chunks
function handleDataAvailable(e) {
    console.log('video data available');
    recordedChunks.push(e.data);
}


// Saves the video file on stop
async function handleStop(e) {
    const blob = new Blob(recordedChunks, {
        type: 'video/webm; codecs=vp9'
    });

    const buffer = Buffer.from(await blob.arrayBuffer());

    const {filePath} = await dialog.showSaveDialog({
        buttonLabel: 'Save video',
        defaultPath: `vid-${Date.now()}.webm`
    });

    console.log(filePath);

    writeFile(filePath, buffer, () => console.log('video saved successfully'));
}