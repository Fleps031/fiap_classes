function debuggerProMaster(texto, numeroCoisas) {
    console.log(getNDashes(numeroCoisas))
    console.log(texto)
    console.log(getNDashes(numeroCoisas))
}

function getNDashes(n) {

    let dashes = ''

    for (let i = 0; i < n; i++) {
        dashes += '-'
    }

    return dashes
}