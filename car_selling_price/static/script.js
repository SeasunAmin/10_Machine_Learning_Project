const modal = document.querySelector('.modal');
const hideIcon = document.querySelector('.modal #hideIcon');
const hideButton = document.querySelector('.modal #hideButton');
const sub = document.querySelector('#showButton');

hideIcon.addEventListener('click', hideModal);
hideButton.addEventListener('click', hideModal);
sub.addEventListener('click', showModal);

function hideModal() {
    modal.id = 'hide';
}

function showModal() {
    modal.id = 'show';
}