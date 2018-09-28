var req = new XMLHttpRequest();
var btn = document.querySelector('#btn');
var map;

var cidade_input = document.querySelector("#cidade");

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, options);
});

$(document).ready(function () {
    $('.collapsible').collapsible();
});

cidade_input.addEventListener('keypress', function (e) {
    if (e.which == 13){
        btn.onclick();
    }
});

btn.onclick = function () {
    var cidade = document.querySelector('#cidade').value;
    req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=29dd02bbff0a3d4c7dd7b14d112dc0fa&units=metric&lang=pt');
    req.send(null);

 

   

    var element = document.getElementById('infoCidade');
    element.classList.remove('hide');   
}



req.onloadend = function() {
    var resp = req.responseText;
    var resp_obj = JSON.parse(resp);

    document.querySelector('#clima').src = 'http://openweathermap.org/img/w/' + resp_obj.weather[0].icon + '.png';
    document.querySelector('#longitude').innerHTML = resp_obj.coord.lon;
    document.querySelector('#latitude').innerHTML = resp_obj.coord.lat;
    document.querySelector('#temperaturaAtual').innerHTML = resp_obj.main.temp + ' C';
    document.querySelector('#temperaturaMinima').innerHTML = resp_obj.main.temp_min + ' C';
    document.querySelector('#temperaturaMaxima').innerHTML = resp_obj.main.temp_max + ' C';
    var tempt = resp_obj.main.temp_max+resp_obj.main.temp_min;
    document.querySelector('#temperaturaMedia').innerHTML = tempt/2 + " C";
    document.querySelector('#pressao').innerHTML = resp_obj.main.pressure + ' hpa';
    document.querySelector('#nascerSol').innerHTML = new Date(resp_obj.sys.sunrise * 1000).getHours()+":"+ new Date(resp_obj.sys.sunrise * 1000).getMinutes();
    document.querySelector('#porSol').innerHTML = new Date(resp_obj.sys.sunset * 1000).getHours() + ":" + new Date(resp_obj.sys.sunset * 1000).getMinutes();

    var coordenadas = { lat: resp_obj.coord.lat, lng: resp_obj.coord.lon };

    var mapa = new google.maps.Map(document.getElementById('divMap'), {
        zoom: 15,
        center: coordenadas
    });

    var marker = new google.maps.Marker({
        position: coordenadas,
        map: mapa,
        title: 'Meu marcador'
    });
}

