const observer = new IntersectionObserver((elements) => {
  elements.forEach((element) => {
    if (element.isIntersecting) {
      element.target.classList.add('show')
    } else {
      element.target.classList.remove('show')
    }
  })
})

const hiddenElements = document.querySelectorAll('.hide')
const hiddenLeftElements = document.querySelectorAll('.hideL')
const hiddenRightElements = document.querySelectorAll('.hideR')

hiddenElements.forEach((element) => observer.observe(element))
hiddenLeftElements.forEach((element) => observer.observe(element))
hiddenRightElements.forEach((element) => observer.observe(element))
