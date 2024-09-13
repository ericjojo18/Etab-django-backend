// document.querySelectorAll('.pagination a').forEach((link) => {
//     link.addEventListener('click', (event) => {
//         event.preventDefault();
//         const url = link.href;

//         fetch(url)
//             .then((response) => response.text())
//             .then((html) => {
//                 document.querySelector('#pagination').innerHTML = new DOMParser().parseFromString(html, 'text/html')
//                 .querySelector('tbody').innerHTML;

//                 // Mettre a jour l'url de la pafination
//                 document.querySelectorAll('.pagination').innerHTML = new DOMParser()
//                 .parseFromString(html, 'text/html')
//                 .querySelector('.pagination').innerHTML;

//                 // Mettre a jour l'url sans refresh la page
//                 window.history.pushState(null, null, url);

//                 // Recharger les liens de la pafination pour les nouvelles pages
//                 document.querySelectorAll('.pagination a').forEach((link) => {
//                     link.addEventListener('click', (event) => {
//                         event.preventDefault();
//                         const url = link.href;
//                         fetch(url)
//                             .then((response) => response.text())
//                             .then((html) => {
//                                 document.querySelector('#pagination').innerHTML = new DOMParser().parseFromString(html, 'text/html')
//                                 .querySelector('tbody').innerHTML;
//                             })
//                             .catch((error) => {
//                                 console.error('erreur lors de la recuoperation de la page', error);
//                             });
//                     });
//                 });

//             })
//             .catch((error) => {
//                 console.error('erreur lors de la recuoperation de la page', error);
//             });
// });
// })


document.addEventListener('DOMContentLoaded', function() {
    // Récupérer tous les liens de pagination
    const paginationLinks = document.querySelectorAll('.pagination-link');

    paginationLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            // Prévenir le comportement par défaut
            event.preventDefault();

            // Supprimer la classe active de tous les éléments
            paginationLinks.forEach(link => link.classList.remove('active'));

            // Ajouter la classe active à l'élément cliqué
            this.classList.add('active');

            // Optionnel: Charger la nouvelle page (en utilisant AJAX ou autre)
            const url = link.href;
            fetch(url)
                .then(response => response.text())
                .then(html => {
                    document.querySelector('#content').innerHTML = html;
                })
                .catch(error => console.error('Erreur:', error));
        });
    });
});
