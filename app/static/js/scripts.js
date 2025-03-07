// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('a[href^="#"]');
  
  for (const link of links) {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);
      
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 70, // Offset for fixed header
          behavior: 'smooth'
        });
      }
    });
  }
});

// Flash message auto-dismiss
document.addEventListener('DOMContentLoaded', function() {
  const flashes = document.querySelectorAll('.flashes li');
  
  if (flashes.length > 0) {
    setTimeout(function() {
      flashes.forEach(function(flash) {
        flash.style.opacity = '0';
        setTimeout(function() {
          flash.style.display = 'none';
        }, 500);
      });
    }, 5000);
  }
}); 