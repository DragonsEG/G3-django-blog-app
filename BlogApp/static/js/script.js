// Listen to the scroll event
window.addEventListener('scroll', function () {
  const navbar = document.getElementById('navbar')
  const scrollTop = window.scrollY

  // Check if the user has scrolled past a certain point (e.g., 100 pixels)
  if (scrollTop > 30) {
    navbar.style.background =
      'linear-gradient(55deg, #541f1f, #000000, #420000)'
  } else {
    navbar.style.background = 'transparent'
  }
})

function isPasswordValid(password) {
  // Define password requirements (customize as needed)
  const minLength = 8 // Minimum length
  const hasUpperCase = /[A-Z]/ // At least one uppercase letter
  const hasLowerCase = /[a-z]/ // At least one lowercase letter
  const hasDigit = /\d/ // At least one digit (0-9)
  const hasSpecialChar = /[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]/ // At least one special character

  // Check each requirement
  const isValidLength = password.length >= minLength
  const hasUpperCaseLetter = hasUpperCase.test(password)
  const hasLowerCaseLetter = hasLowerCase.test(password)
  const hasDigitCharacter = hasDigit.test(password)
  const hasSpecialCharacter = hasSpecialChar.test(password)

  // Return true if all requirements are met, false otherwise
  return (
    isValidLength &&
    hasUpperCaseLetter &&
    hasLowerCaseLetter &&
    hasDigitCharacter &&
    hasSpecialCharacter
  )
}

document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('SIform')
  const submitBtn = document.getElementById('submitBtn')

  form.addEventListener('submit', function (event) {
    // Prevent the default form submission
    event.preventDefault()

    // Perform your form validation here (e.g., check password requirements)
    const isFormValid = validateForm() // Implement your validation logic

    if (isFormValid) {
      // If the form is valid, allow submission
      form.submit()
      submitBtn.disabled = true // Disable the button to prevent multiple submissions
    }
  })

  function validateForm() {
    // Implement your form validation logic here
    // Return true if the form is valid, false otherwise
    const password1 = form.querySelector('[name="password1"]').value
    const password2 = form.querySelector('[name="password2"]').value

    // Example: Check if passwords match
    const warnUl = document.getElementById('warn')
    const warn2Ul = document.getElementById('warn2')
    if (isPasswordValid(password1)) {
      warnUl.style.display = 'none' // Hide the warning div if the password is valid
    } else {
      warnUl.style.display = 'block' // Show the warning div if the password is invalid
    }

    if (password1 !== password2) {
      warn2Ul.style.display = 'block'
      return false
    } else {
      warn2Ul.style.display = 'none'
    }

    return true // Form is valid
  }
})
