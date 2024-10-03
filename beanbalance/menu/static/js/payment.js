let selectedPaymentMethod = 'Cash';

function setPaymentMethod(method) {
    selectedPaymentMethod = method;
    updatePaymentDisplay();
    updateButtonStyles();
}

function updatePaymentDisplay() {
    const cashPayment = document.getElementById('cashPayment');
    const cardPayment = document.getElementById('cardPayment');
    const qrCodePayment = document.getElementById('qrCodePayment');

    cashPayment.classList.add('hidden');
    cardPayment.classList.add('hidden');
    qrCodePayment.classList.add('hidden');

    switch (selectedPaymentMethod) {
        case 'Cash':
            cashPayment.classList.remove('hidden');
            break;
        case 'Card':
            cardPayment.classList.remove('hidden');
            break;
        case 'QR Code':
            qrCodePayment.classList.remove('hidden');
            break;
    }
}

function updateButtonStyles() {
  const buttons = document.querySelectorAll('.payment-method-button');
  buttons.forEach(button => {
      button.classList.remove('bg-gray-500');
  });

  const selectedButton = document.getElementById(`${selectedPaymentMethod.toLowerCase().replace(' ', '')}Button`);
  if (selectedButton) {
      selectedButton.classList.add('bg-gray-500');
  }
}

document.addEventListener('DOMContentLoaded', function() {
  updatePaymentDisplay();
  updateButtonStyles();
});

function updateReceive(digit) {
    let receive = document.getElementById('receive').innerText;
    let [whole, decimal] = receive.split('.');

    if (decimal.length < 2) {
        decimal = decimal + digit;
    } else {
        whole = whole + decimal[0];
        decimal = decimal[1] + digit;
    }

    whole = whole.replace(/^0+/, '') || '0';

    if (whole.length > 7) {
        whole = whole.slice(-7);
    }

    document.getElementById('receive').innerText = whole + '.' + decimal;
}

function deleteLastDigit() {
    let receive = document.getElementById('receive').innerText;
    let [whole, decimal] = receive.split('.');

    if (decimal === '00') {
        whole = whole.slice(0, -1) || '0';
    } else {
        decimal = '0' + decimal[0];
    }

    document.getElementById('receive').innerText = whole + '.' + decimal;
}


function showBillSummary() {
    const summaryReceiveElement = document.getElementById('summaryReceive');
    const changeElement = document.getElementById('change');
    const receiveCashElement = document.getElementById('receive_cash');
    const messageElement = document.getElementById('message');

    const changeDiv = document.getElementById('div-change');
    const receiveDiv = document.getElementById('div-receive');
    const messageDiv = document.getElementById('div-message');

    changeDiv.classList.add('hidden');
    receiveDiv.classList.add('hidden');
    messageDiv.classList.add('hidden');

    console.log(selectedPaymentMethod);

    if (selectedPaymentMethod === 'Cash') {
        const total = parseFloat(document.getElementById('total').innerText);
        const receive = parseFloat(document.getElementById('receive').innerText);

        if (receive < total) {
            showCustomAlert('The received amount is less than the total. Please check again.');
            return;
        }

        const change = receive - total;
        summaryReceiveElement.innerText = '฿' + total.toFixed(2);
        receiveCashElement.innerText = '฿' + receive.toFixed(2);
        changeElement.innerText = '฿' + change.toFixed(2);

        changeDiv.classList.remove('hidden');
        receiveDiv.classList.remove('hidden');

        document.getElementById('billSummaryPopup').classList.remove('hidden');
        document.getElementById('billSummaryPopup').classList.add('flex');
    } else {
        summaryReceiveElement.innerText = '฿' + document.getElementById('total').innerText;
        messageDiv.classList.remove('hidden');
        messageElement.innerText = 'Please wait while we process your order...';
        document.getElementById('billSummaryPopup').classList.remove('hidden');
        document.getElementById('billSummaryPopup').classList.add('flex');
    }
}

function closeBillSummary() {
  const billSummaryPopup = document.getElementById('billSummaryPopup');
  billSummaryPopup.classList.add('hidden');
  billSummaryPopup.classList.remove('flex');
}

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

function closeBillSummary() {
    document.getElementById('billSummaryPopup').classList.add('hidden');
    document.getElementById('billSummaryPopup').classList.remove('flex');
}


function confirmOrder(csrf_token) {
  const cartData = localStorage.getItem('cart');
  const total = parseFloat(document.getElementById('total').innerText);

  const paymentMethod = selectedPaymentMethod;


  if (cartData) {
    const cart = JSON.parse(cartData);
    const data = {
      cart: cart,
      total: total,
      payment_method: paymentMethod
    };

    fetch('/menu/payment/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify(data)
    })
    .then((cart) => {
      console.log("Item deleted successfully");
      localStorage.removeItem('cart');
      alert("Thank you for your order!");
      window.location.href = '/menu/';
    })
    .catch((error) => console.error("Error:", error));
  }
}
