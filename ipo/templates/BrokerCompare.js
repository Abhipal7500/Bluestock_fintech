// JavaScript
document.querySelectorAll('.side-menu .navbar-nav .nav-link').forEach(link => {
    link.addEventListener('click', () => {
      
      
        // Deactivate all links
      document.querySelectorAll('.side-menu .navbar-nav .nav-link').forEach(l => l.classList.remove('active'));
      
      
      // Activate the clicked link
      link.classList.add('active');
    });
  });