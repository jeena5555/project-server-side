function payment(csrf_token) {
  const cartData = localStorage.getItem('cart');

  if (cartData) {
    const cart = JSON.parse(cartData);

    fetch('/menu/payment/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify(cart)
    })
    .then((cart) => {
      console.log("Item deleted successfully");
      window.location.reload();
    })
    .catch((error) => console.error("Error:", error));
  }
}
