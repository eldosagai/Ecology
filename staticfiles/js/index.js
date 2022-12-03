document.addEventListener('DOMContentLoaded', function() {
    var parent = document.querySelector('.splitview'),
        topPanel = parent.querySelector('.top'),
        handle = parent.querySelector('.handle'),
        skewHack = 0,
        delta = 0;

    // If the parent has .skewed class, set the skewHack var.
    if (parent.className.indexOf('skewed') != -1) {
        skewHack = 1000;
    }

    window.addEventListener('mousemove', function(event) {
        if(!parent.contains(event.target)){
            handle.style.transition = "left .3s ease-in-out"
            topPanel.style.transition = "width .3s ease-in-out"
            handle.style.left = "";
            topPanel.style.width = "";
        }
        else{
            handle.style.transition = ""
            topPanel.style.transition = ""
            // Get the delta between the mouse position and center point.
            delta = (3*event.clientX - window.innerWidth / 2) * .5;

            // Move the handle.
            handle.style.left = delta + 'px';

            // Adjust the top panel width.
            topPanel.style.width = skewHack + delta + 'px';
        }
    });
});

const allId = document.querySelectorAll('[data-id');

allId.forEach(item => {
    item.addEventListener('click', () => {
        localStorage.removeItem('id')
        localStorage.setItem('id', item.dataset.id)
    })
})
