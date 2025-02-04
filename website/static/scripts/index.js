const socket = io.connect('https://pimemorizer.onrender.com');

const loginCont = document.querySelector('.login-container')
const signupCont = document.querySelector('.signup-container')

function showCreateAccount(){
     document.querySelector('.create-account-container').style.display = 'flex'
}

function hideCreateContainer(){
     document.querySelector('.create-account-container').style.display = 'none'
}
function hideLoginContainer(){
     document.querySelector('.login-container').style.display = 'none'
}

function loginUser(id){
     const logiinContainer = document.querySelector('.login-container')
     logiinContainer.style.display = 'flex'
     const loginHeader = document.querySelector('.login-header')
     
     socket.emit('user-login', {id})

     socket.on('response-login', (data)=>{
          const username = data.username
          const loginForm = document.getElementById('loginForm').action = `/login/${username}`
          loginHeader.textContent = `Welcome ${username}`

 

     })
}
 function showPassword(){
     let passwordInput = document.getElementById('passwordInput')

     if(passwordInput.type == 'password'){
          passwordInput.type = 'text'
     }else{
          passwordInput.type = 'password'
     }
 }
 function showPassword1(){
     let passwordInput = document.getElementById('passwordInput1')

     if(passwordInput.type == 'password'){
          passwordInput.type = 'text'
     }else{
          passwordInput.type = 'password'
     }
 }
 function showPassword2(){
     let passwordInput = document.getElementById('passwordInput2')

     if(passwordInput.type == 'password'){
          passwordInput.type = 'text'
     }else{
          passwordInput.type = 'password'
     }
 }

 function exitPrompt(){
     document.querySelector('.prompt-container').style.display = 'none'
 }