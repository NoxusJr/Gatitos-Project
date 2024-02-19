async function asyncApiRequest(url, data, method) {

    const requestConfig = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    }

    const response = await fetch(url, requestConfig)
    const resultData = await response.json()

    return resultData;
}


async function loginAccount() {
    const url = 'http://127.0.0.1:5000/conta/logarConta'

    let email = String(document.getElementById('nick').value)
    let password = String(document.getElementById('password').value)

    const bodyData = {
        email: email,
        senha: password,
    };

    const response = await asyncApiRequest(url, bodyData, 'POST')

    if (response){
        window.location.href = "layout.html"
    } else {
        alert('ERRO AO TENTAR LOGAR')
    }
}


async function createAccount() {
    const url = 'http://127.0.0.1:5000/conta/criarConta'

    let name = String(document.getElementById('nick').value)
    let email = String(document.getElementById('gmail').value)
    let password = String(document.getElementById('password').value)

    const bodyData = {
        nome: name,
        email: email,
        senha: password,
    };

    const response = await asyncApiRequest(url, bodyData, 'POST')

    if (response){
        window.location.href = "login.html"
    } else {
        alert('ERRO AO TENTAR CRIAR A CONTA')
    }
}