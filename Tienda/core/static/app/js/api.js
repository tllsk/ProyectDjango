/*VISTA VISITA*/
/*VISTA INDEX*/
const datos_v = document.querySelector('#productos')
const url_v = 'https://fakestoreapi.com/products'

fetch(url_v)
    .then(res => res.json())
    .then(data => {
        data.forEach(producto => {
            const attr1 = document.createAttribute("align")
            attr1.value = "center"
            const attr = document.createAttribute("class")
            attr.value = "col-md-4 mb-3"

            var div = document.createElement('div')
            div.setAttributeNode(attr)
            div.setAttributeNode(attr1)
            div.setAttribute('id', producto.id)
            div.addEventListener('click', function() {
                window.location.href = `ficha_producto_ropa.html?id=${producto.id}`
            });
            div.style.border = '1px solid #3a3a3b'
            div.innerHTML = `<img class="ropa" src="${producto.image}" width="32%">
                        <div>
                            <h2>${producto.title}</h2>
                            <span>${producto.price}</span>
                        </div>`
            datos_v.appendChild(div)
        })
    })

/*VISTA ADMIN*/
/*VISTA INDEX*/
const datos_a = document.querySelector('#productos_adm')
const url_a = 'https://fakestoreapi.com/products'

fetch(url_a)
    .then(res => res.json())
    .then(data => {
        data.forEach(producto => {
            const attr1 = document.createAttribute("align")
            attr1.value = "center"
            const attr = document.createAttribute("class")
            attr.value = "col-md-4 mb-3"

            var div = document.createElement('div')
            div.setAttributeNode(attr)
            div.setAttributeNode(attr1)
            div.setAttribute('id', producto.id)
            div.addEventListener('click', function() {
                window.location.href = `../admin/ficha_producto.html?id=${producto.id}`
            })
            div.style.border = '1px solid #3a3a3b'
            div.innerHTML = `<img class="ropa" src="${producto.image}" width="32%">
                        <div>
                            <h2>${producto.title}</h2>
                            <span>${producto.price}</span>
                        </div>`
            datos_a.appendChild(div)
        })
    })

/*VISTA CLIENTE*/
/*VISTA INDEX*/
const datos_c = document.querySelector('#productos_cli')
const url_c = 'https://fakestoreapi.com/products'

fetch(url_c)
    .then(res => res.json())
    .then(data => {
        data.forEach(producto => {
            const attr1 = document.createAttribute("align")
            attr1.value = "center"
            const attr = document.createAttribute("class")
            attr.value = "col-md-4 mb-3"

            var div = document.createElement('div')
            div.setAttributeNode(attr)
            div.setAttributeNode(attr1)
            div.setAttribute('id', producto.id)
            div.addEventListener('click', function() {
                window.location.href = `../cliente/ficha_producto.html?id=${producto.id}`
            })
            div.style.border = '1px solid #3a3a3b'
            div.innerHTML = `<img class="ropa" src="${producto.image}" width="32%">
                        <div>
                            <h2>${producto.title}</h2>
                            <span>${producto.price}</span>
                            <a class="btn btn-sm btn-primary" href="../cliente/carrito.html">COMPRAR</a>
                        </div>`
            datos_c.appendChild(div)
        })
    })