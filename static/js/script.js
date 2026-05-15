function openModal(){

    document.getElementById("serviceModal").style.display = "block";

}
function closeModal(){

    document.getElementById('serviceModal').style.display = 'none';

}

function toggleMenu(){

    document.querySelector(".nav-links").classList.toggle("active");
}
/* Active Navbar Highlight */

const sections = document.querySelectorAll("section");

const navLinks = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop;

        const sectionHeight = section.clientHeight;

        if(pageYOffset >= sectionTop - 200){

            current = section.getAttribute("id");
        }
    });

    navLinks.forEach(link => {

        link.classList.remove("active");

        if(link.getAttribute("href") === "#" + current){

            link.classList.add("active");
        }
    });
});
/* Scroll Reveal Animation */

function revealSections(){

    const reveals = document.querySelectorAll(".reveal");

    reveals.forEach(section => {

        const windowHeight = window.innerHeight;

        const revealTop = section.getBoundingClientRect().top;

        const revealPoint = 150;

        if(revealTop < windowHeight - revealPoint){

            section.classList.add("active");
        }
    });
}

window.addEventListener("scroll", revealSections);