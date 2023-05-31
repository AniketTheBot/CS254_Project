let wishlist = [];

function addToWishlist(bookId) {
    const iconElement = document.querySelector(`i[data-id="${bookId}"]`);

    if (!wishlist.includes(bookId)) {
        wishlist.push(bookId);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        if (iconElement) {
            iconElement.classList.add('wishlisted');
        }
    } else {
        const index = wishlist.indexOf(bookId);
        wishlist.splice(index, 1);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        if (iconElement) {
            iconElement.classList.remove('wishlisted');
        }
    }
}


function displayWishlistedBooks() {
    const wishlistedContainer = document.getElementById('wishlisted-container');
    const storedWishlist = localStorage.getItem('wishlist');

    if (storedWishlist) {
        wishlist = JSON.parse(storedWishlist);
    }

    wishlist.forEach(bookId => {
        const iconElement = document.querySelector(`i[data-id="${bookId}"]`);
        if (iconElement) {
            iconElement.classList.add('wishlisted');
        }
    });
}

if (document.getElementById('wishlisted-container')) {
    displayWishlistedImages();
}
