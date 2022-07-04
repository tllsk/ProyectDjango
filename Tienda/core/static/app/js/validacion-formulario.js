$('#registro').validate({
    "rules": {
        "rut": {
            required: true,
        },
        "nombres": {
            required: true,
        },
        "apellidos": {
            required: true,
        },
        "correo": {
            required: true,
            email: true,
        },
        "direccion": {
            required: true,
        },
        "password": {
            required: true,
            minlength: 10,
        },
        "password2": {
            required: true,
            minlength: 10,
            equalTo: "#password",
        },
    },
    messages: {
        "rut": {
            required: 'Debe ingresar un RUT válido',
        },
        "nombres": {
            required: 'Debe ingresar sus nombres',
        },
        "apellidos": {
            required: 'Debe ingresar sus apellidos',
        },
        "correo": {
            required: 'Debe ingresar su correo electrónico',
            email: 'Formato de correo incorrecto'
        },
        "direccion": {
            required: 'Debe ingresar su dirección',
        },
        "password": {
            required: 'Debe ingresar una password',
            minlength: 'La mínima cantidad de caracteres de la contraseña es 10',
        },
        "password2": {
            required: 'Debe repetir la misma password',
            minlength: 'La mínima cantidad de caracteres de la contraseña es 10',
            equalTo: 'La repetición de contraseña debe coincidir con la contraseña original',
        },
    }
});

$('#mantenerU').validate({
    "rules": {
        "id": {
            required: true,
        },
        "rut": {
            required: true,
        },
        "nombres": {
            required: true,
        },
        "apellidos": {
            required: true,
        },
        "direccion": {
            required: true,
        },
        "password": {
            required: true,
            minlength: 10,
        },
    },
    messages: {
        "id": {
            required: 'Debe ingresar un ID válido',
        },
        "rut": {
            required: 'Debe ingresar un RUT válido',
        },
        "nombres": {
            required: 'Debe ingresar sus nombres',
        },
        "apellidos": {
            required: 'Debe ingresar sus apellidos',
        },
        "direccion": {
            required: 'Debe ingresar su dirección',
        },
        "password": {
            required: 'Debe ingresar una password',
            minlength: 'La mínima cantidad de caracteres de la contraseña es 10',
        },
    }
});

$('#mantenerP').validate({
    "rules": {
        "id": {
            required: true,
        },
        "categoria": {
            required: true,
        },
        "nombre": {
            required: true,
        },
        "descripcion": {
            required: true,
        },
        "precio": {
            required: true,
        },
        "descuentoSub": {
            required: true,
        },
        "descuentoOferta": {
            required: true,
        },

    },
    messages: {
        "id": {
            required: 'Debe ingresar un ID válido',
        },
        "nombre": {
            required: 'Debe ingresar el nombre',
        },
        "descripcion": {
            required: 'Debe ingresar la descripcion',
        },
        "categoria": {
            required: 'Debe seleccionar una categoria',
        },
        "precio": {
            required: 'Debe ingresar un precio',
        },
        "descuentoSub": {
            required: 'Debe Ingresar un numero',
        },
        "descuentoOferta": {
            required: 'Debe ingresar un numero',
        },  
    }
});

$('#mantenerB').validate({
    "rules": {
        "id": {
            required: true,
        },
        "categoria": {
            required: true,
        },
        "nombre": {
            required: true,
        },
        "cantidad": {
            required: true,
        },
    },
    messages: {
        "id": {
            required: 'Debe ingresar un ID válido',
        },
        "nombre": {
            required: 'Debe seleccionar el nombre',
        },
        "categoria": {
            required: 'Debe seleccionar una categoria',
        },
        "cantidad": {
            required: 'Debe ingresar la cantidad',
        },
    }
});

$('#ingresar').validate({
    "rules": {
        "correo": {
            required: true,
        },
        "contraseña": {
            required: true,
        },
    },
    messages: {
        "correo": {
            required: 'Debe ingresar su correo electrónico',
            email: 'Formato de correo incorrecto'
        },
        "contraseña": {
            required: 'Debe ingresar una contraseña',
        },
    }
});
function validateEmail(email) {
    var re = /\S+@\S+\.\S+/;
    return re.test(email);
}

// Valida el rut con su cadena completa "XXXXXXXX-X"
function validateRut(rutCompleto) {
    if (!/^[0-9]+-[0-9kK]{1}$/.test(rutCompleto))
        return false;
    var tmp = rutCompleto.split('-');
    var rut = tmp[0];
    var digv = tmp[1];
    if (digv == 'k') digv = 'K';
    return (dv(rut) == digv);
}

function dv(T) {
    var M = 0,
        S = 1;
    for (; T; T = Math.floor(T / 10))
        S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
}

// Uso de la función validateRut
// alert( Fn.validateRut('16560241-2') ? 'válido' : 'inválido');


$.validator.addMethod(
    "validateemail",
    function(value, element, validate) {
        debugger
        if (validate) {
            return validateEmail(value);
        }
    },
    "Formato de correo incorrecto"
);

$.validator.addMethod(
    "onenumber",
    function(value, element, validate) {
        if (validate) {
            var re = new RegExp('.*[0-9].*');
            resp = re.test(value);
            return resp;
        }
    },
    "La contraseña debe contener al menos un número"
);

$.validator.addMethod(
    "onemayus",
    function(value, element, validate) {
        if (validate) {
            var re = new RegExp('.*[A-Z].*');
            resp = re.test(value);
            return resp;
        }
    },
    "La contraseña debe contener al menos una mayúscula"
);

$.validator.addMethod(
    "rut",
    function(value, element, validate) {
        if (validate) {
            return validateRut(value);
        }
    },
    "El formato del rut no es válido"
);

$("#rut").rules("add", { rut: true });
$("#correo").rules("add", { validateemail: true });
$("#password").rules("add", { onenumber: true });
$("#password").rules("add", { onemayus: true });

$('#buscarfoto').on('change', function(e) {
    let file = '../images/' + e.target.files[0].name;
    $('#fotoperfil').attr('src', file);
});
$('#mostrar-bordes').on('click', function(e) {
    let borde = $('.borde-bootstrap-row').css('border');
    if (borde.includes('1px')) {
        $('.borde-bootstrap-row').css({ 'border': '0px solid blue' });
    } else {
        $('.borde-bootstrap-row').css({ 'border': '1px solid blue' });
    }
});




const pass = document.querySelector('#rngPass');
const panel = document.createElement('p');
panel.setAttribute('id', 'pass');
const btn = document.createElement('button');
const div = document.createElement('div');

btn.textContent = "Generar";

btn.addEventListener("click", function() {
    long=15;
    var caracteres = "abcdefghijklmnopqrstuvwxyz012346789ABCDEFGHIJKLMNOPQRSTUVWXYZ012346789";
    var contraseña = "";
    for (i=0; i<long; i++) contraseña += caracteres.charAt(Math.floor(Math.random()*caracteres.length));
    panel.innerHTML=contraseña;
});


div.appendChild(panel);
div.appendChild(btn);
pass.appendChild(div);


