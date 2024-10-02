const cart = {
    items: [],

    init() {
        this.loadFromLocalStorage();
        this.renderCart();
        this.bindEvents();
    },

    loadFromLocalStorage() {
        const savedCart = localStorage.getItem('cart');
        if (savedCart) {
            this.items = JSON.parse(savedCart);
        } else {
            this.items = [];
        }
    },

    saveToLocalStorage() {
        localStorage.setItem('cart', JSON.stringify(this.items));
    },

    addItem(id, name, price) {
        const existingItem = this.items.find(item => item.id === id);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            this.items.push({ id, name, price, quantity: 1 });
        }
        this.saveToLocalStorage();
        this.renderCart();
    },

    updateQuantity(id, newQuantity) {
        const item = this.items.find(item => item.id === id);
        if (item) {
            if (newQuantity > 0) {
                item.quantity = newQuantity;
            } else {
                this.items = this.items.filter(i => i.id !== id);
            }
            this.saveToLocalStorage();
            this.renderCart();
        }
    },

    calculateTotal() {
        let total = 0;

        this.items.forEach(item => {
            const price = parseFloat(item.price);
            const quantity = item.quantity;
            total += price * quantity;
        });

        return total.toFixed(2);
    },

    renderCart() {
        const cartItemsContainer = document.getElementById('cart-items');
        const totalElement = document.getElementById('total');

        cartItemsContainer.innerHTML = this.items.map(item => `
            <div class="bg-white p-5 rounded-lg mb-4">
                <div class="flex justify-between items-center">
                    <div>
                        <span class="font-semibold">${item.name}</span>
                        <p class="text-gray-600">${item.price}</p>
                    </div>
                    <div class="flex items-center">
                        <button class="bg-gray-200 px-2 py-1 rounded-l" onclick="cart.updateQuantity('${item.id}', ${item.quantity - 1})">-</button>
                        <span class="px-4">${item.quantity}</span>
                        <button class="bg-gray-200 px-2 py-1 rounded-r" onclick="cart.updateQuantity('${item.id}', ${item.quantity + 1})">+</button>
                    </div>
                </div>

            </div>
        `).join('');

        totalElement.textContent = this.calculateTotal();
    },

    bindEvents() {
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', function() {
                const id = this.getAttribute('data-id');
                const name = this.getAttribute('data-name');
                const price = this.getAttribute('data-price');
                cart.addItem(id, name, price);
            });
        });

        document.getElementById('search').addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            document.querySelectorAll('.menu-item').forEach(item => {
                const name = item.querySelector('h3').textContent.toLowerCase();
                console.log('Name:', name);
                if (name.includes(searchTerm)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }

            });
        });

        document.getElementById('payment-btn').addEventListener('click', function() {
            if (cart.items.length > 0) {
                window.location.href = "payment/";
            } else {
                // alert("Please add items to your cart.");
                showCustomAlert("Please add items to your cart.");
            }
        });

    }
};

document.addEventListener('DOMContentLoaded', () => cart.init());


function showCustomAlert(message) {
    const alertBox = document.createElement('div');
    alertBox.innerText = message;
    alertBox.style.position = 'fixed';
    alertBox.style.top = '50%';
    alertBox.style.left = '50%';
    alertBox.style.transform = 'translate(-50%, -50%)';
    alertBox.style.padding = '20px';
    alertBox.style.backgroundColor = '#f8d7da';
    alertBox.style.color = '#721c24';
    alertBox.style.border = '1px solid #f5c6cb';
    alertBox.style.borderRadius = '10px';
    alertBox.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
    alertBox.style.zIndex = '1000';

    const closeButton = document.createElement('button');
    closeButton.innerText = 'Close';
    closeButton.style.marginTop = '10px';
    closeButton.style.padding = '5px 10px';
    closeButton.style.backgroundColor = '#721c24';
    closeButton.style.color = 'white';
    closeButton.style.border = 'none';
    closeButton.style.borderRadius = '5px';
    closeButton.style.cursor = 'pointer';

    closeButton.onclick = function() {
        alertBox.remove(); // Remove the alert box
        window.location.reload(); // Reload the page
    };

    alertBox.appendChild(closeButton);
    document.body.appendChild(alertBox);
}
