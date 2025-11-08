// JavaScript for fetching random users from API
// Developer: Anisha Karki

// Function to fetch data
function fetchRandomUser() {
    fetch('https://randomuser.me/api/')
        .then(response => response.json())
        .then(data => {
            const user = data.results[0];
            document.getElementById('user-photo').src = user.picture.large;
            document.getElementById('user-name').innerText = `${user.name.first} ${user.name.last}`;
            document.getElementById('user-email').innerText = user.email;
        })
        .catch(error => {
            console.error('Error fetching user:', error);
        });
}

// Fetch one user when page loads
fetchRandomUser();

// Fetch new user when button is clicked
document.getElementById('new-user-btn').addEventListener('click', fetchRandomUser);
