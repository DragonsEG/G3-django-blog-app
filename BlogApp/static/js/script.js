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
