let idade = 17
let habilitacão = true
let autorizacão = false 

if (idade == 18 && habilitacão == true && autorizacão == false) {
    console.log(`pode entrar`)
} else if (idade > 18 && habilitacão == true) {
    console.log(`pode entra`)
} else if (idade > 18 && autorizacão == false) {
    console.log(`nao poderas entrar`)
} else if (idade < 18) {
    console.log(`nao poderas entrar`)
} else if (idade < 18 && autorizacão == false) {
    console.log(`nao pode entrar`)
} 
    
