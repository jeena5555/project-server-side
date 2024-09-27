const cart = {
    items: [],

    init() {
        this.loadFromLocalStorage();
        this.renderCart();
        this.bindEvents();
    },

    loadFromLocalStorage() {
        const savedCart = localStorage.getItem('cart');
        this.items = savedCart ? JSON.parse(savedCart) : [];
    },

    saveToLocalStorage() {
        localStorage.setItem('cart', JSON.stringify(this.items));
    },

    addItem(name, price) {
        const existingItem = this.items.find(item => item.name === name);
        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            this.items.push({ name, price, quantity: 1 });
        }
        this.saveToLocalStorage();
        this.renderCart();
    },

    updateQuantity(name, newQuantity) {
        const item = this.items.find(item => item.name === name);
        if (item) {
            if (newQuantity > 0) {
                item.quantity = newQuantity;
            } else {
                this.items = this.items.filter(i => i.name !== name);
            }
            this.saveToLocalStorage();
            this.renderCart();
        }
    },

    calculateTotal() {
        return this.items.reduce((total, item) => total + (parseFloat(item.price) * item.quantity), 0).toFixed(2);
    },

    renderCart() {
        const cartItemsContainer = document.getElementById('cart-items');
        const totalElement = document.getElementById('total');

        cartItemsContainer.innerHTML = this.items.map(item => `
            <div class="bg-white p-4 rounded-lg mb-4">
                <div class="flex justify-between items-center">
                    <span class="font-semibold">${item.name}</span>
                    <div class="flex items-center">
                        <button class="bg-gray-200 px-2 py-1 rounded-l" onclick="cart.updateQuantity('${item.name}', ${item.quantity - 1})">-</button>
                        <span class="px-4">${item.quantity}</span>
                        <button class="bg-gray-200 px-2 py-1 rounded-r" onclick="cart.updateQuantity('${item.name}', ${item.quantity + 1})">+</button>
                    </div>
                </div>
                <p class="text-gray-600">${item.price}</p>
            </div>
        `).join('');

        totalElement.textContent = this.calculateTotal();
    },

    bindEvents() {
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', function() {
                const name = this.getAttribute('data-name');
                const price = this.getAttribute('data-price');
                cart.addItem(name, price);
            });
        });

        document.getElementById('search').addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            document.querySelectorAll('.menu-item').forEach(item => {
                const name = item.querySelector('h3').textContent.toLowerCase();
                const description = item.querySelector('p:nth-child(3)').textContent.toLowerCase();
                item.style.display = (name.includes(searchTerm) || description.includes(searchTerm)) ? 'block' : 'none';
            });
        });

        document.querySelectorAll('.category-btn').forEach(button => {
            button.addEventListener('click', function() {
                const category = this.getAttribute('data-category');
                document.querySelectorAll('.menu-item').forEach(item => {
                    item.style.display = (category === 'All' || item.getAttribute('data-category') === category) ? 'block' : 'none';
                });
            });
        });
    }
};

document.addEventListener('DOMContentLoaded', () => cart.init());
