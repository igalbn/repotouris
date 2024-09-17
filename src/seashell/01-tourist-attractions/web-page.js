        window.onload = () => {
            drawAttractions();
        }

        function drawAttractions(){
            youtubeLinks.forEach(element => {

                const videoTitleElem = document.createElement('p');
                videoTitleElem.textContent = element['title'];
                document.body.appendChild(videoTitleElem);

                const videoLinkElem = document.createElement('a');
                videoLinkElem.href = element['url'];
                videoLinkElem.textContent = element['url'];
                document.body.appendChild(videoLinkElem);

            });
        }
