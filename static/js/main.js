// Animate skill bars when they come into view
function animateSkills() {
    const skillLevels = document.querySelectorAll('.skill-level');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const level = entry.target.getAttribute('data-level');
                entry.target.style.width = `${level}%`;
            }
        });
    });

    skillLevels.forEach(skill => observer.observe(skill));
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Initialize animations
document.addEventListener('DOMContentLoaded', function() {
    animateSkills();
});

// Add scroll reveal animations
window.addEventListener('scroll', function() {
    const elements = document.querySelectorAll('.animate-up, .animate-left, .animate-right');
    
    elements.forEach(element => {
        const position = element.getBoundingClientRect();
        
        if(position.top < window.innerHeight - 100) {
            element.style.opacity = '1';
            element.style.transform = 'translate(0)';
        }
    });
});

// Mobile Navigation
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const links = document.querySelectorAll('.nav-links li');

    hamburger.addEventListener('click', () => {
        // Toggle Nav
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active');

        // Animate Links
        links.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });
    });

    // Close mobile menu when clicking a link
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.classList.remove('active');
            
            links.forEach(link => {
                link.style.animation = '';
            });
        });
    });
}); 