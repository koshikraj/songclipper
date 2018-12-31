document.addEventListener('DOMContentLoaded', function() {
    var submit = document.getElementById('submit');

    // onClick's logic below:
    submit.addEventListener('click', function() {
        submit.value = 'Fetching details ...';
        submit.disabled = true;
        submit.style.backgroundColor = '#95db80';
        const fileQuery = document.getElementById('songquery').value;

        fetch('http://localhost:8888/clip?song=' + fileQuery)
            .then(function(response) {
                return response.json();
            })
            .then(function(myJson) {
                console.log(JSON.stringify(myJson));
                submit.value = 'Downloading ...';
                document.getElementById('songdetails').innerHTML='Downloading ' + myJson.data.title;
                document.getElementById('clickhere').innerHTML='<a target="_blank" href="'+ myJson.data.link +'">Click here</a> if not downloaded automatically';

                try {
                    chrome.downloads.download({
                        url: myJson.data.link,
                        filename: myJson.data.title + '.mp3'
                    });
                }
                catch(error) {
                    chrome.downloads.download({
                        url: myJson.data.link,
                        filename: fileQuery + '.mp3'
                    });

                }

                chrome.downloads.onChanged.addListener(function(dItem){
                    console.log(dItem.state);

                    if (dItem.state.current === 'complete')
                    {
                        console.log('completeted');
                        submit.value = 'Download';
                        submit.disabled = false;
                        submit.style.backgroundColor = '#4CAF50';
                    }

                })
            });
    });
});
