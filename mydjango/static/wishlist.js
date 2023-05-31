let wishlist = [];

function addToWishlist(imageId) {
    const iconElement = document.querySelector(`i[data-id="${imageId}"]`);

    if (!wishlist.includes(imageId)) {
        wishlist.push(imageId);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        if (iconElement) {
            iconElement.classList.add('wishlisted');
        }
    } else {
        const index = wishlist.indexOf(imageId);
        wishlist.splice(index, 1);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        if (iconElement) {
            iconElement.classList.remove('wishlisted');
        }
    }
}


function displayWishlistedImages() {
    const wishlistedContainer = document.getElementById('wishlisted-container');
    const storedWishlist = localStorage.getItem('wishlist');

    if (storedWishlist) {
        wishlist = JSON.parse(storedWishlist);
    }

    wishlist.forEach(imageId => {
        const iconElement = document.querySelector(`i[data-id="${imageId}"]`);
        if (iconElement) {
            iconElement.classList.add('wishlisted');
        }
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
