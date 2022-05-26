function butPress(element) {
    var inputVal = document.getElementById("input_1").value;
    var y, z, t;
    var x = inputVal;
    switch(element.id) {
        case "but0":
            document.getElementById("but6").innerHTML="Pounds";
            document.getElementById("but5").innerHTML="Grams";
            document.getElementById("but4").innerHTML="Ounces";
            document.getElementById("but3").innerHTML="Kilograms";
            break;
        case "but1":
            document.getElementById("but6").innerHTML="Kilometres";
            document.getElementById("but5").innerHTML="Metres";
            document.getElementById("but4").innerHTML="Miles";
            document.getElementById("but3").innerHTML="Inches";
            break;
        case "but2":
            document.getElementById("but6").innerHTML="Gigabytes";
            document.getElementById("but5").innerHTML="Bytes";
            document.getElementById("but4").innerHTML="Kilobytes";
            document.getElementById("but3").innerHTML="Megabytes";
            break;
        case "but3":
            if(document.getElementById("but3").innerHTML== "Megabytes"){
            y = x / 1000;
            z = x * 1000000;
            t = x * 1000;
            document.getElementById("but6").innerHTML=y +" GB";
            document.getElementById("but5").innerHTML=z +" B";
            document.getElementById("but4").innerHTML=t +" KB";
            document.getElementById("but3").innerHTML=x +" MB";
            break;
            }
            else if(document.getElementById("but3").innerHTML== "Kilograms"){
            y = x * 2.20462;
            z = x * 1000;
            t = x * 35.274;
            document.getElementById("but6").innerHTML=y +" Lb";
            document.getElementById("but5").innerHTML=z +" G";
            document.getElementById("but4").innerHTML=t +" Oz";
            document.getElementById("but3").innerHTML=x +" KG";
            break;
            }
            else if(document.getElementById("but3").innerHTML== "Inches"){
            y = x / 39370.079;
            z = x / 0.0254;
            t = x / 63360;
            document.getElementById("but6").innerHTML=y +" KM";
            document.getElementById("but5").innerHTML=z +" M";
            document.getElementById("but4").innerHTML=t +" Mi";
            document.getElementById("but3").innerHTML=x +" In";
            break;
            }
        case "but4":
            if(document.getElementById("but4").innerHTML== "Kilobytes"){
            y = x / 1000000  ;
            z = x * 1000 ;
            t = x / 1000  ;
            document.getElementById("but6").innerHTML=y +" GB";
            document.getElementById("but5").innerHTML=z +" B";
            document.getElementById("but4").innerHTML=x +" KB";
            document.getElementById("but3").innerHTML=t+ " MB";
            break;
            }
            else if(document.getElementById("but4").innerHTML== "Ounces"){
            y = x / 16 ;
            z = x * 28.3495;
            t = x / 35.274;
            document.getElementById("but6").innerHTML=y +" Lb";
            document.getElementById("but5").innerHTML=z +" G";
            document.getElementById("but4").innerHTML=x +" Oz";
            document.getElementById("but3").innerHTML=t +" KG";
            break;
            }
            else if(document.getElementById("but4").innerHTML== "Miles"){
            y = x / 1.60934;
            z = x / 160934;
            t = x * 63360;
            document.getElementById("but6").innerHTML=y +" KM";
            document.getElementById("but5").innerHTML=z +" M";
            document.getElementById("but4").innerHTML=x +" Mi";
            document.getElementById("but3").innerHTML=t +" In";
            break
            }
        case "but5":
            if(document.getElementById("but5").innerHTML== "Bytes"){
            y = x / 1000000000;
            z = x / 1000;
            t = x / 1000000;
            document.getElementById("but6").innerHTML=y +" GB";
            document.getElementById("but5").innerHTML=x +" B";
            document.getElementById("but4").innerHTML=z +" KB";
            document.getElementById("but3").innerHTML=t+ " MB";
            break;
            }
            else if(document.getElementById("but5").innerHTML== "Grams"){
            y = x / 453.592;
            z = x / 28.3495;
            t = x / 1000;
            document.getElementById("but6").innerHTML=y +" Lb";
            document.getElementById("but5").innerHTML=x +" G";
            document.getElementById("but4").innerHTML=z +" Oz";
            document.getElementById("but3").innerHTML=t +" KG";
            break;
            }
            else if(document.getElementById("but5").innerHTML== "Metres"){
            y = x / 1000;
            z = x / 1609.344;
            t = x * 39.701;
            document.getElementById("but6").innerHTML=y +" KM";
            document.getElementById("but5").innerHTML=x +" M";
            document.getElementById("but4").innerHTML=z +" Mi";
            document.getElementById("but3").innerHTML=t +" In";
            break;
            }
        case "but6":
            if(document.getElementById("but6").innerHTML== "Gigabytes"){
            y = x * 1000000000;
            z = x * 1000 ;
            t = x * 1000000  ;
            document.getElementById("but6").innerHTML=x +" GB";
            document.getElementById("but5").innerHTML=y +" B";
            document.getElementById("but4").innerHTML=z +" KB";
            document.getElementById("but3").innerHTML=t+ " MB";
            break;
            }
            else if(document.getElementById("but6").innerHTML== "Pounds"){
            y = x * 453.592;
            z = x * 16;
            t = x * 0.453592;
            document.getElementById("but6").innerHTML=x +" Lb";
            document.getElementById("but5").innerHTML=y +" G";
            document.getElementById("but4").innerHTML=z +" Oz";
            document.getElementById("but3").innerHTML=t +" KG";
            break;
            }
            else if(document.getElementById("but6").innerHTML== "Kilometres"){
            y = x * 1000;
            z = x * 0.621371;
            t = x * 39370.1;
            document.getElementById("but6").innerHTML=x +" KM";
            document.getElementById("but5").innerHTML=y +" M";
            document.getElementById("but4").innerHTML=z +" Mi";
            document.getElementById("but3").innerHTML=t +" In";
            break;
            }
}
}






