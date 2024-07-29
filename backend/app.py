<!DOCTYPE html>
<html>
<head>
    <title>Indoor-Routes Application</title>
</head>
<body>
    <h1>Welcome to Indoor-Routes application!</h1>
    <button onclick="startTracking()">Start Tracking</button>
    <button onclick="stopTracking()">Stop Tracking</button>
    <p id="location"></p>

    <script>
        let watchID;

        function startTracking() {
            if (navigator.geolocation) {
                watchID = navigator.geolocation.watchPosition(showPosition, showError, {
                    enableHighAccuracy: true,
                    timeout: 5000,
                    maximumAge: 0
                });
            } else {
                document.getElementById("location").innerHTML = "Geolocation is not supported by this browser.";
            }
        }

        function stopTracking() {
            if (watchID) {
                navigator.geolocation.clearWatch(watchID);
            }
        }

        function showPosition(position) {
            let location = "Latitude: " + position.coords.latitude +
                " Longitude: " + position.coords.longitude;
            document.getElementById("location").innerHTML = location;

            fetch('/location', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ location: location }),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }

        function showError(error) {
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    document.getElementById("location").innerHTML = "User denied the request for Geolocation.";
                    break;
                case error.POSITION_UNAVAILABLE:
                    document.getElementById("location").innerHTML = "Location information is unavailable.";
                    break;
                case error.TIMEOUT:
                    document.getElementById("location").innerHTML = "The request to get user location timed out.";
                    break;
                case error.UNKNOWN_ERROR:
                    document.getElementById("location").innerHTML = "An unknown error occurred.";
                    break;
            }
        }
    </script>
</body>
</html>
