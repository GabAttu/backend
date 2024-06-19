// static/js/favorites.js

// Aggiungi o rimuovi ricetta dai preferiti
function toggleFavorite(recipeId) {
    fetch(`/toggle_favorite/${recipeId}/`)
        .then(response => response.json())
        .then(data => {
            if (data.is_favorite) {
                // Ricetta aggiunta ai preferiti, aggiorna interfaccia utente
                alert('Ricetta aggiunta ai preferiti!');
            } else {
                // Ricetta rimossa dai preferiti, aggiorna interfaccia utente
                alert('Ricetta rimossa dai preferiti.');
            }
            // Puoi aggiornare dinamicamente l'interfaccia utente qui se necessario
        })
        .catch(error => {
            console.error('Errore durante il toggle dei preferiti:', error);
        });
}
