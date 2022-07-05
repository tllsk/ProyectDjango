/*VISTA VISITA*/
const dato_v = document.querySelector('#producto')
const getUrl_v = new URLSearchParams(window.location.search)
id = getUrl_v.get('id')
const url_v = 'https://fakestoreapi.com/products'

fetch(`${url_v}/${id}`)
    .then(res => res.json())
    .then(data => {
        const div = document.createElement('div')
        const precio = document.createElement('p')
        precio.innerHTML = data.price

        div.innerHTML = `<div class="container" style="display: flex; align-items: flex-end;">
                            <img class="ropa_ficha" src="${data.image}"width="90%">
                        <div style="margin-left: 3%;">
                            <p>Precio:</p>
                            <h2>$${data.price}<h2>
                            <h2>${data.title}</h2>
                            <p>Descripcion:</p>
                            <p>${data.description}</p>
                        </div>
                    </div>`
        dato_v.appendChild(div)
    })

/*VISTA CLIENTE*/
const dato_c = document.querySelector('#producto_cli');
const getUrl_c = new URLSearchParams(window.location.search);
id = getUrl_c.get('id');
const url_c = 'https://fakestoreapi.com/products';

fetch(`${url_c}/${id}`)
    .then(res => res.json())
    .then(data => {
        const div = document.createElement('div');

        div.innerHTML = `<div class="container" style="display: flex; align-items: flex-end;">
                        <img class="ropa_ficha" src="${data.image}"width="90%">
                        <div style="margin-left: 3%;">
                            <p>Precio:</p>
                            <h2>$${data.price}<h2>
                            <h2>${data.title}</h2>
                            <p>Descripcion:</p>
                            <p>${data.description}</p>
                        </div><a class="btn btn-sm btn-primary" href="../cliente/carrito.html">COMPRAR</a>
                    </div>`;
        dato_c.appendChild(div);
    });

/*VISTA ADMIN*/
const dato_a = document.querySelector('#producto_adm');
const getUrl_a = new URLSearchParams(window.location.search);
id = getUrl_a.get('id');
const url_a = 'https://fakestoreapi.com/products';

fetch(`${url_a}/${id}`)
    .then(res => res.json())
    .then(data => {
        const div = document.createElement('div');

        div.innerHTML = `<div class="container" style="display: flex; align-items: flex-end;">
                        <img class="ropa_ficha" src="${data.image}"width="90%">
                        <div style="margin-left: 3%;">
                            <p>Precio:</p>
                            <h2>$${data.price}<h2>
                            <h2>${data.title}</h2>
                            <p>Descripcion:</p>
                            <p>${data.description}</p>
                        </div>
                    </div>`;
        dato_a.appendChild(div);
    });