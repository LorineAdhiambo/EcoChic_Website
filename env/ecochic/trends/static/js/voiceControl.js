document.getElementById('start botton').addEventListener('click', function(){
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const command = event.results[0][0].transcript.toLowerCase();
        if (command.include('home')) {
            window.location.href = '/';
        } else if (command.include('team')) {
            window.location.href = '/team';
        } else if (command.include('contact')) {
            window.location.href = '/contact';
        }
    };

    recognition.onerror = function(event) {
        console.log('Error occurred in recognition: ' + event.error);
        // console.error(event.error);
    };
});