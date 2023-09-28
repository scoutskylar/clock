var clockAnimationFrame = 0;
var clockElement = document.getElementById('clock');
var offsetElement = document.getElementById('offset');
var errorElement = document.getElementById('errorMargin');
var offset = 0;

function updateClock() {
    clockElement.innerText = new Date(Date.now() + offset).toLocaleTimeString();
    clockAnimationFrame = requestAnimationFrame(updateClock);
}

function stopClock() {
    cancelAnimationFrame(clockAnimationFrame);
}

async function resync() {
    let syncStartTimestamp = Date.now();
    let response = await fetch('/sync');
    let syncEndTimestamp = Date.now();
    let syncServerTimestamp = parseInt(await response.text());
    let syncError = Math.ceil((syncEndTimestamp - syncStartTimestamp) / 2) + 1;
    offset = syncServerTimestamp - Math.ceil((syncEndTimestamp + syncStartTimestamp) / 2);;
    if (offsetElement) offsetElement.innerText = offset;
    if (errorElement) errorElement.innerText = syncError;
}

updateClock();
resync();
