// Function to render the edit form and populate fields
function rendereditpage(employeeId) {
  // Find the employee card by using the ID or some other approach
  const employeeCard = document.querySelector(`[data-id="${employeeId}"]`);
  console.log(employeeCard);

  if (employeeCard) {
    // Extract employee data from data attributes
    const firstName = employeeCard.dataset.firstName;
    const lastName = employeeCard.dataset.lastName;
    const gender = employeeCard.dataset.gender;
    const birthDate = employeeCard.dataset.birthDate;
    const position = employeeCard.dataset.position;

    // Hide the add form if visible
    const addFormContainer = document.getElementById('add-category-form');
    if (addFormContainer) {
      addFormContainer.classList.add('hidden');
    }

    // Show and populate the edit form
    const editFormContainer = document.getElementById('edit-form-container');
    if (editFormContainer) {
      editFormContainer.classList.remove('hidden'); // Show the form

      // Populate form fields with employee data
      document.getElementById('first-name').value = firstName || '';
      document.getElementById('last-name').value = lastName || '';
      document.getElementById('gender').value = gender || 'Male';
      document.getElementById('birth-date').value = birthDate || '';
      document.getElementById('position').value = position || '';
    }
  } else {
    console.error('Employee card not found for ID:', employeeId);
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

