function rendereditpage(employeeId) {
  // Assuming employeeId is a string, if not, parse it as needed
  // Find the employee card by using the ID or some other approach
  const employeeCard = document.querySelector(`[data-id="${employeeId}"]`);
  console.log(employeeCard)

  if (employeeCard) {
    // Extract employee data from data attributes
    const firstName = employeeCard.dataset.firstName;
    const lastName = employeeCard.dataset.lastName;
    const gender = employeeCard.dataset.gender;
    const birthDate = employeeCard.dataset.birthDate;
    const position = employeeCard.dataset.position;

    // Show and populate the edit form
    const editFormContainer = document.getElementById('edit-form-container');
    editFormContainer.classList.remove('hidden'); // Show the form

    // Populate form fields with employee data
    document.getElementById('first-name').value = firstName || '';
    document.getElementById('last-name').value = lastName || '';
    document.getElementById('gender').value = gender || 'Male';
    document.getElementById('birth-date').value = birthDate || '';
    document.getElementById('position').value = position || '';
  } else {
    console.error('Employee card not found for ID:', employeeId);
  }
}