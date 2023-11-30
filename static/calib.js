let circles = [];

function createCircle() {
  let circle = document.createElement('div');
  circle.classList.add('clickable');
  circle.style.top = Math.random() * window.innerHeight + 'px';
  circle.style.left = Math.random() * window.innerWidth + 'px';

  circle.addEventListener('click', function() {
    this.style.display = 'none';
    circles.splice(circles.indexOf(this), 1);
  });

  circles.push(circle);
  document.body.appendChild(circle);
}

createCircle()
setInterval(createCircle(), 1000); // Create a new circle every second
