function renderEditPage(employeeId) {
  const employeeCard = document.querySelector(`[data-id="${employeeId}"]`);
  console.log('employeeCard.dataset : ', employeeCard.dataset)


  if (employeeCard) {
    // Extract employee data from data attributes
    const firstName = employeeCard.dataset.firstName;
    const lastName = employeeCard.dataset.lastName;
    const gender = employeeCard.dataset.gender;
    const birthDate = employeeCard.dataset.birthDate;
    const position = employeeCard.dataset.position;
    const account = employeeCard.dataset.account;
    const password = employeeCard.dataset.password;
    const salary = employeeCard.dataset.salary;

    // Hide the add form if visible
    const addFormContainer = document.getElementById('add-employee-form');
    if (addFormContainer) {
      addFormContainer.classList.add('hidden');
    }

    // Show and populate the edit form
    const editFormContainer = document.getElementById('edit-form-container');
    if (editFormContainer) {
      editFormContainer.classList.remove('hidden');

      // Populate the form fields with employee data
      document.getElementById('first-name').value = firstName || '';
      document.getElementById('last-name').value = lastName || '';
      document.getElementById('gender').value = gender || '';
      document.getElementById('birth-date').value = new Date(birthDate).toISOString().split('T')[0]; // Convert date format
      document.getElementById('position').value = position || '';
      document.getElementById('account').value = account || '';
      document.getElementById('password').value = password || '';
      document.getElementById('salary').value = salary || '';
      // Set employee ID to be used for updates
      document.getElementById('edit-form').setAttribute('data-employee-id', employeeId);
    }
  } else {
    console.error('Employee not found for ID:', employeeId);
  }
}

// Function to render the add employee form
function renderaddemployee() {
  // Hide the edit form if it is visible
  const editFormContainer = document.getElementById('edit-form-container');
  if (editFormContainer) {
    editFormContainer.classList.add('hidden'); // Hide the edit form
  }

  // Show the add employee form
  const addFormContainer = document.getElementById('add-employee-form');
  if (addFormContainer) {
    addFormContainer.classList.remove('hidden'); // Make sure the add employee form is visible
  }
}

// Function to update the employee details
function updateEmployee(event) {
  event.preventDefault();  // Prevent form submission

  const employeeId = document.getElementById('edit-form').getAttribute('data-employee-id');
  const updatedEmployee = {
    first_name: document.getElementById('first-name').value,
    last_name: document.getElementById('last-name').value,
    account: document.getElementById('account').value,
    password: document.getElementById('password').value,
    gender: document.getElementById('gender').value,
    birth_date: document.getElementById('birth-date').value,
    position: document.getElementById('position').value,
    salary: parseFloat(document.getElementById('salary').value),
  };

  fetch(`/employees/update/${employeeId}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    },
    body: JSON.stringify(updatedEmployee),  // Send the updated employee data
  })
  .then(response => {
    if (response.ok) {
      console.log('Employee updated successfully');
      window.location.reload();  // Reload the page to see updated data
    } else {
      console.error('Failed to update employee:', response.statusText);
    }
  })
  .catch(error => console.error('Error:', error));
}

function deleteEmployee() {
  const employeeId = document.getElementById('edit-form').getAttribute('data-employee-id');

  if (!confirm("Are you sure you want to delete this employee?")) {
    return; // If the user cancels the deletion, stop the function
  }

  fetch(`/employees/delete/${employeeId}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value, // Include CSRF token for security
    },
  })
    .then(response => {
      if (response.ok) {
        console.log('Employee deleted successfully');
        window.location.reload(); // Reload the page to reflect the deletion
      } else {
        console.error('Failed to delete employee:', response.statusText);
      }
    })
    .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  const searchElement = document.getElementById('search');
  if (searchElement) {
      searchElement.addEventListener('input', function() {
          const searchTerm = this.value.toLowerCase();
          document.querySelectorAll('.employee-card').forEach(item => {
              const name = item.querySelector('h3').textContent.toLowerCase();
              if (name.includes(searchTerm)) {
                  item.style.display = '';
              } else {
                  item.style.display = 'none';
              }
          });
      });
  }
});