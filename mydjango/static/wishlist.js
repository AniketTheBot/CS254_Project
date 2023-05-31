let wishlist = [];

function addToWishlist(imageId) {
    if (!wishlist.includes(imageId)) {
        wishlist.push(imageId);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
    }
}

function displayWishlistedImages() {
    const wishlistedContainer = document.getElementById('wishlisted-container');
    const storedWishlist = localStorage.getItem('wishlist');

    if (storedWishlist) {
        wishlist = JSON.parse(storedWishlist);
    }

    wishlist.forEach(imageId => {
        const imageElement = document.querySelector(`img[data-id="${imageId}"]`);
        if (imageElement) {
            const clonedImage = imageElement.cloneNode(true);
            wishlistedContainer.appendChild(clonedImage);
        }
    });
}

if (document.getElementById('wishlisted-container')) {
    displayWishlistedImages();
}
