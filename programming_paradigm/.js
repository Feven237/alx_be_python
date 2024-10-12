<html>
    <head>
        <title>
            Hello World
        </title>
    </head>
    <body>
        <script>
            var ken, seat, Greeting;
            ken = new Date();
            seat = ken.getHours();
            
            if (seat > 12) {
                Greeting = 'Good afternoon';
                document.write('<h3>' + Greeting + '</h3>');
            } else if (seat >= 0 && seat <= 12) {
                Greeting = 'Good morning';
                document.write('<h3>' + Greeting + '</h3>');
            } else {
                Greeting = 'Hello';
                document.write('<h3>' + Greeting + '</h3>');
            }
        </script>
    </body>
</html>
