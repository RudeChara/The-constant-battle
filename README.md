<!DOCTYPE html>
<html lang="ru">
<head>
 <title>мой сайт шапка</title>
 <meta charset="utf-8"><!--а это надо не скажу зачем-->
 <style type="text/css">
 body, html {
 padding: 0;
 margin: 0;
 background-color: teal; /*цвет бекраунда боди*/
 }
 .container {/*  c (.) начинаеться описание класса*/
 width: 750px;
 margin: 0 auto;/*про margin и border и pading я скину чуть позже*/

 background-color: #ccc;
 }
 header > h1 {
 margin: 0;
 padding: 15px 0;
 text-align: center; /*центрирование по центру текста*/
 text-transform: uppercase;/*высокий текст*/
 border-bottom: 1px solid #fefefe;
 }
 header > nav > ul {
 list-style-type: none;
 margin: 0;
 padding: 0;
 text-align: center;
 border-bottom: 1px solid #fefefe;
 }
 header > nav > ul > li {
 display: inline-block; /*что бы адаптировалосьи выстовлялось нормально а не просто текст есть border*/
 padding: 15px 30px;
 border-left: 1px solid #fefefe;
 }
 header > nav > ul > li:last-child {
 border-right: 1px solid #fefefe;
 }
 header > nav > ul > li > a {
 text-decoration: none; /*подчеркивание текста и точка и т.п я это убрал что-бы нормально меню было*/
 color: black;
 }
 header > nav > ul > li > a:hover {
 text-decoration: underline; /*а это по фану*/
 color: blue;
 }

 </style>
</head>
<!--мой пример юзать не советую там для адыкватной работы еще много стилев надо-->
<body>
 <div class="container"><!--стоить ставить дивы еще-->
 <header>
 <h1>Шапка сайта</h1>
 <nav>
 <ul class="menu"><!--Классы нужны для Css-->
 <li><a href="Vtm2.html">Статья 1</a></li>
 <li><a href="Vtm3.html">Статья 2</a></li>
 <li><a href="Vtm4.html">статья 3</a></li>
 </ul>
 </nav>
 </header>
 </div>
</body>
</html>