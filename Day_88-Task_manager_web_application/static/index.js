function errorBtn() {
    elem = document.querySelector('.message');
    elem.style.display = 'none';
}

function addProject() {
    elem = document.querySelector('.project-form');
    elem.style.display = 'block';
}

function addTask() {
    elem = document.querySelector('.task-form');
    elem.style.display = 'block';
}

function openProject() {
    elem = document.querySelector('.add-task-form');
    elem.style.display = 'flex';
}

function closeProject() {
    elem = document.querySelector('.add-task-form');
    elem.style.display = 'none';
}
