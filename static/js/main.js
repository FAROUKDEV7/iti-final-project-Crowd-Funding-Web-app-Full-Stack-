function showPage(pageId) {
    // Hide all pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
            });
            
    // Show the selected page
    document.getElementById(pageId).classList.add('active');
            
    // Scroll to top
    window.scrollTo(0, 0);
    }
        
    // User dropdown toggle
    document.getElementById('user-profile').addEventListener('click', function() {
    document.getElementById('dropdown-menu').classList.toggle('show');
    });
        
    // Close dropdown when clicking outside
    window.addEventListener('click', function(e) {
        if (!e.target.matches('.user-profile *')) {
        document.getElementById('dropdown-menu').classList.remove('show');
            }
    });
        
    // Login function
    function login() {
        // Simulate login
        document.getElementById('user-actions').style.display = 'none';
        document.getElementById('user-profile').style.display = 'flex';
        showPage('home');
        alert('Login successful!');
    }
        
    // Register function
    function register() {
        // Simulate registration
        alert('Registration successful! Please check your email to activate your account.');
        showPage('login');
    }
        
    // Reset password function
    function resetPassword() {
        alert('Password reset link has been sent to your email.');
        showPage('login');
    }
        
    // Logout function
    function logout() {
        document.getElementById('user-actions').style.display = 'flex';
        document.getElementById('user-profile').style.display = 'none';
        showPage('home');
    }
        
    // Initialize page
    document.addEventListener('DOMContentLoaded', function() {
        // Check if user is logged in (for demo purposes)
        const isLoggedIn = false; // Change to true to simulate logged in state
            
        if (isLoggedIn) {
            document.getElementById('user-actions').style.display = 'none';
            document.getElementById('user-profile').style.display = 'flex';
        }
    });