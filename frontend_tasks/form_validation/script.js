// Simple Form Validation
const form = document.getElementById('signupForm');
const msg = document.getElementById('message');

form.addEventListener('submit', function(e) {
  e.preventDefault();

  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const password = document.getElementById('password').value.trim();

  msg.textContent = '';
  msg.style.color = 'red';

  // check empty fields
  if (name === '' || email === '' || password === '') {
    msg.textContent = 'Please fill in all fields!';
    return;
  }

  const emailPattern = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
  if (!emailPattern.test(email)) {
    msg.textContent = 'Invalid email format!';
    return;
  }

  
  if (password.length < 6) {
    msg.textContent = 'Password must be at least 6 characters!';
    return;
  }

  // success message
  msg.style.color = 'green';
  msg.textContent = 'Form submitted successfully!';
  form.reset();
});
