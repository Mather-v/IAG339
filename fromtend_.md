# HTML
```
<!DOCTYPE html>
<html lang="es ">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi página web</title>
    <link rel="stylesheet" href="css/style.css">
</head>


<body>

    <header>
        <h1>Bienvenidos al sistema</h1>
        <nav>
            <ul>
                <li><a href="https://google.com" target="_blank"> Ir a google </a></li>
                <li><a href="https://facebook.com" target="_blank"> Ir a Facebook</a></li>
                <li><a href="https://instagram.com" target="_blank">Ir a Instagram</a></li>
            </ul>
        </nav>

    </header>


    <!-- no se puede ver desde la interfaz del usuario -->
    <!-- comentarios, nos ayudan a documentar nuestro desarrollo -->
    <h1>Hola Mundo 🥵🥵🥵🥵🥵🙄🍻😁🙈h-1</h1>
    <h2>h-2</h2>
    <h3>h-3</h3>
    <h4>h-4</h4>
    <h5>h-5</h5>
    <h6>h-6</h6>

    <p> Etiqueta de tipo <strong>párrafo</strong> <i>Acá la cursiva</i> </p>
    <p><b>tambien para negrilla</b> </p>
    <p> <em>Tambien para la cursiva</em> </p>
    <p> <em> <b> <u>Subrayado</u> </b> </em> </p>

    <!-- <p>
        1.	Item  
        2.	Item 
        3.	Item 

    </p> -->

    <!-- Esxisten 2 tipos de lista  -->
    <!-- ol ordenared list -->

    <ol>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ol>

    <!-- ul unordered list -->

    <ul>
        <li>Item A</li>
        <li>Item B</li>
        <li>Item C</li>
    </ul>

    <footer>
        <address>
            Autor: Bartolomé Sintes Marco<br>
            correo: bartolome.sintes@example.com
        </address>

        <p>Última modificación: 28 de noviembre de 2017</p>
    </footer>
</body>

</html>
```
# CSS

```
/* body {
    background-color: burlywood;
} */
 /* Resetear estilos */
  *{
    margin: 0;
    padding: 0;
  }

header{
    background-color: #007acc;
    color: white;
    padding: 20px;
    text-align: center;
}

nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
    margin-top: 10px;
}

nav ul li{
    margin: 0 15px;
}

nav ul li a{
    color: white;
    text-decoration: none;
    font-weight: bold;
}

h1 {
    color: blue;
}

h2 {
    color: green;
}

h3 {
    color: orange;
}
```
