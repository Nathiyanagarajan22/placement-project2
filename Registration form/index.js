document.getElementById('submit').addEventListener('click', function(e) {
    e.preventDefault(); 

    const user = document.getElementById('Username').value.trim();
    const pass = document.getElementById('Password').value.trim();
    const message = document.getElementById('result');

    if (user === 'java_batch' && pass === '@123') {
        message.textContent = '✅ Login Successful!';
        message.className = 'success';
    } else {
        message.textContent = '❌ Invalid Username or Password!';
        message.className = 'failed';
    }
});
