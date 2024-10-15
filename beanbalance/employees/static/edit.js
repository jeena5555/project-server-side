function renderEditPage(employeeId) {
  const employeeCard = document.querySelector(`[data-id="${employeeId}"]`);
  console.log('employeeCard.dataset : ', employeeCard.dataset)
  console.log('employeeCard : ', document.querySelector(`[data-id="${employeeId}"]`).dataset.account)


  if (employeeCard) {
    // Extract employee data from data attributes
    const firstName = employeeCard.dataset.firstName;
    const lastName = employeeCard.dataset.lastName;
    const gender = employeeCard.dataset.gender;
    const birthDate = employeeCard.dataset.birthDate;
    const position = employeeCard.dataset.position;
    const account = employeeCard.dataset.account;
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

  const addEmployeeForm = document.querySelector('#add-employee-form form');
  if (addEmployeeForm) {
    addEmployeeForm.removeEventListener('submit', submitAddEmployeeForm);

    addEmployeeForm.addEventListener('submit', submitAddEmployeeForm);
  }
}

// ฟังก์ชันแยกสำหรับการจัดการการส่งฟอร์ม
function submitAddEmployeeForm(event) {
    event.preventDefault(); // ป้องกันการรีเฟรชหน้า

    const formData = new FormData(this); // ดึงข้อมูลฟอร์มจากฟอร์มที่ใช้งานอยู่

    // Log ข้อมูลทั้งหมดในฟอร์มที่ถูกส่งออกมา
    // for (let [key, value] of formData.entries()) {
    //   console.log(`${key}: ${value}`);
    // }

    fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // ป้องกัน CSRF
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            window.location.reload(); // รีเฟรชหน้าเมื่อสำเร็จ
        } else {
            handleFormErrors(data.errors); // แสดงข้อผิดพลาด
        }
    })
    .catch(error => console.error('Error:', error));
}

// ฟังก์ชันสำหรับแสดงข้อผิดพลาดในฟอร์มพนักงาน
function handleFormErrors(errors) {
    // ลบข้อความข้อผิดพลาดเก่าทั้งหมด
    document.querySelectorAll('.error-message').forEach(error => error.remove());

    // แสดงข้อผิดพลาดใหม่
    for (let field in errors) {
        let fieldElement = document.querySelector(`#add-employee-form [name="${field}"]`);
        if (fieldElement) {
            let errorMessage = document.createElement('p');
            errorMessage.classList.add('text-red-500', 'text-sm', 'mt-2', 'error-message');
            errorMessage.textContent = errors[field];
            fieldElement.parentElement.appendChild(errorMessage);
        }
    }
}

function updateEmployee(event) {
  event.preventDefault();  // Prevent form submission

  const employeeId = document.getElementById('edit-form').getAttribute('data-employee-id');
  const firstNameInput = document.getElementById('first-name');
  const lastNameInput = document.getElementById('last-name');
  const accountInput = document.getElementById('account');
  const birthDateInput = document.getElementById('birth-date');
  const salaryInput = document.getElementById('salary');
  
  const firstName = firstNameInput.value.trim();
  const lastName = lastNameInput.value.trim();
  const account = accountInput.value.trim();
  const birthDate = birthDateInput.value;
  const salary = parseFloat(salaryInput.value);

  // ดึง account ปัจจุบันจาก employeeCard
  const currentAccount = document.querySelector(`[data-id="${employeeId}"]`).dataset.account;
  console.log('currentAccount : ', currentAccount)

  // ลบข้อความข้อผิดพลาดเก่า
  document.querySelectorAll('.error-message').forEach(error => error.remove());

  let hasError = false;

  // Validate first_name
  if (!/^[a-zA-Z]+$/.test(firstName)) {
    let firstNameError = document.createElement('p');
    firstNameError.classList.add('text-red-500', 'text-sm', 'mt-2', 'error-message');
    firstNameError.textContent = "First name should not contain numbers.";
    firstNameInput.parentElement.appendChild(firstNameError);
    hasError = true;
  }

  // Validate last_name
  if (!/^[a-zA-Z]+$/.test(lastName)) {
    let lastNameError = document.createElement('p');
    lastNameError.classList.add('text-red-500', 'text-sm', 'mt-2', 'error-message');
    lastNameError.textContent = "Last name should not contain numbers.";
    lastNameInput.parentElement.appendChild(lastNameError);
    hasError = true;
  }

  // ดึงข้อมูล account ที่มีอยู่จาก data-account ที่ถูกตั้งไว้ใน DOM
  const existingAccounts = Array.from(document.querySelectorAll('[data-account]'))
                                .map(elem => elem.getAttribute('data-account'));

  // Validate account (ห้ามซ้ำ แต่ไม่รวม account ปัจจุบันที่กำลังแก้ไข)
  if (account !== currentAccount && existingAccounts.includes(account)) {
    let accountError = document.createElement('p');
    accountError.classList.add('text-red-500', 'text-sm', 'mt-2', 'error-message');
    accountError.textContent = `The username '${duplicateName}' is already taken. Please choose a different username.`;
    accountInput.parentElement.appendChild(accountError);
    hasError = true;
  }

  // Validate birth_date (ต้องเป็นวันที่ก่อนปี 2005)
  const birthYear = new Date(birthDate).getFullYear();
  if (birthYear >= 2005) {
    let birthDateError = document.createElement('p');
    birthDateError.classList.add('text-red-500', 'text-sm', 'mt-2', 'error-message');
    birthDateError.textContent = "Birth date must be before 2005.";
    birthDateInput.parentElement.appendChild(birthDateError);
    hasError = true;
  }

  // Validate salary (ต้องมากกว่า 1)
  if (salary <= 1) {
    let salaryError = document.createElement('p');
    salaryError.classList.add('text-red-500', 'text-sm', 'mt-2', 'error-message');
    salaryError.textContent = "Salary must be greater than 1.";
    salaryInput.parentElement.appendChild(salaryError);
    hasError = true;
  }

  // ถ้ามีข้อผิดพลาด ให้หยุดการทำงาน
  if (hasError) {
    return;
  }

  // ถ้าไม่มีข้อผิดพลาด ให้ส่งข้อมูลไปยังเซิร์ฟเวอร์
  const updatedEmployee = {
    first_name: firstName,
    last_name: lastName,
    account: account,
    birth_date: birthDate,
    salary: salary,
  };

  fetch(`/employees/update/${employeeId}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    },
    body: JSON.stringify(updatedEmployee),  // ส่งข้อมูลพนักงานที่อัปเดต
  })
  .then(response => {
    if (response.ok) {
      console.log('Employee updated successfully');
      window.location.reload();  // รีโหลดหน้าเพื่อดูข้อมูลที่อัปเดต
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