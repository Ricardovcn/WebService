var req = new XMLHttpRequest();
var btn = document.querySelector('#btn');

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
    req.open('GET', 'http://api.openweathermap.org/data/2.5/weather?q=' + cidade + '&appid=29dd02bbff0a3d4c7dd7b14d112dc0fa&units=metric&lang=pt&mode=xml');
    req.send(null);

    var element = document.getElementById('infoCidade');
    element.classList.remove('hide');   
}



req.onloadend = function() {
    
    dados_clima = new DOMParser().parseFromString(req.responseText, "text/xml");

    document.querySelector('#clima').src = 'http://openweathermap.org/img/w/'+ dados_clima.getElementsByTagName('weather')[0].getAttribute('icon') +'.png';
    document.querySelector('#longitude').innerHTML = dados_clima.getElementsByTagName('coord')[0].getAttribute('lon');
    document.querySelector('#latitude').innerHTML = dados_clima.getElementsByTagName('coord')[0].getAttribute('lat');
    document.querySelector('#temperaturaAtual').innerHTML =  dados_clima.getElementsByTagName('temperature')[0].getAttribute('value')+ '  °C';
    document.querySelector('#temperaturaMinima').innerHTML = dados_clima.getElementsByTagName('temperature')[0].getAttribute('min')+ '  °C';
    document.querySelector('#temperaturaMaxima').innerHTML = dados_clima.getElementsByTagName('temperature')[0].getAttribute('max')+ '  °C';
    document.querySelector('#pressao').innerHTML = dados_clima.getElementsByTagName('pressure')[0].getAttribute('value') + ' hpa';
    document.querySelector('#nascerSol').innerHTML = dados_clima.getElementsByTagName('sun')[0].getAttribute('rise')
    document.querySelector('#porSol').innerHTML = dados_clima.getElementsByTagName('sun')[0].getAttribute('set');

    var coordenadas = { lat: dados_clima.getElementsByTagName('coord')[0].getAttribute('lat'), lng: dados_clima.getElementsByTagName('coord')[0].getAttribute('lon') };

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

