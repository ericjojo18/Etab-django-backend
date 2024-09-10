function openModals(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

// Fonction pour fermer la modale
function closeModals(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Fermer la modale en cliquant en dehors de la zone de contenu
window.onclick = function(event) {
    var modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
}