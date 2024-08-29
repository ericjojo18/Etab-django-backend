/*==================== MENU ====================*/

const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");

menuBtn.addEventListener('click', ()=>{
    sideMenu.style.display = 'block';
})

closeBtn.addEventListener('click', ()=>{
    sideMenu.style.display = 'none';
})

themeToggler.addEventListener('click', ()=>{
    document.body.classList.toggle('dark-theme-variables');
    themeToggler.querySelector('span').classList.toggle('active');

    themeToggler.querySelector('span').classList.toggle('active');
})

const deleteButton = document.getElementsByClassName('btn delete');
const alertBox = document.querySelector('.alert');
const dashboard = document.querySelector('.machin');
let urlToDelete = ""
    // Fonction pour afficher le modal
    function onModal() {
            alertBox.style.display = 'block';
            
            urlToDelete = event.target.getAttribute('data-url');
        }

        // Fonction pour masquer le modal
        function closeModal() {
            alertBox.style.display = 'none';
        }

        Array.from(deleteButton).forEach(element=>element.addEventListener('click', onModal))


        // Événement pour le bouton Non
        cancelDelete.addEventListener('click', closeModal);
        confirmDelete.addEventListener('click', ()=>{
            window.location.href = urlToDelete;
        })

        