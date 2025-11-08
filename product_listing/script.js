// Product Listing Page JS (works for any number of product cards)
// Shows alert when "Add to Cart" button is clicked

document.addEventListener('DOMContentLoaded', function () {
  const buttons = document.querySelectorAll('.cart-btn');

  buttons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      // find the product title in the same card
      const card = this.closest('.product-card');
      const titleEl = card ? card.querySelector('h3') : null;
      const productName = titleEl ? titleEl.innerText : 'Product';
      alert(productName + ' added to cart 🛒');
    });
  });
});
