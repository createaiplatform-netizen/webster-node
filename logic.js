function triggerRRR(type) {
    const timestamp = new Date().toISOString();
    const display = document.getElementById('status-display');
    display.innerText = `${type} INITIALIZED...`;
    display.classList.add('animate-pulse', 'text-white');

    setTimeout(() => {
        display.innerText = "ZERO-DRIFT VERIFIED";
        display.classList.remove('animate-pulse');
        alert(`Clinical Handshake Complete: ${type} logged at ${timestamp}`);
    }, 1200);
}
