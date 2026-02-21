
document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
  
    // Get the form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const contactNumber = document.getElementById('contactNumber').value;
    const requirement = document.getElementById('requirement').value;
    const message = document.getElementById('message').value;
  
    // Debugging logs
    console.log({ name, email, contactNumber, requirement, message });
  
    // Validate the form
    if (name && email && contactNumber && requirement && message) {
      // Show SweetAlert success message
      Swal.fire({
        title: 'Success!',
        text: 'Your message has been sent.',
        icon: 'success',
        confirmButtonText: 'OK'
      }).then(() => {
        // Optionally, submit the form data here if you have a backend to send to
        // e.g., via AJAX or fetch()
        document.getElementById('contactForm').reset(); // Reset the form
      });
    } else {
      // Show SweetAlert error message
      Swal.fire({
        title: 'Error!',
        text: 'Please fill in all the required fields.',
        icon: 'error',
        confirmButtonText: 'OK'
      });
    }
  });