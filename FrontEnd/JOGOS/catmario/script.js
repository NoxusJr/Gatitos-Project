const cat = document.querySelector('.cat');
const pipe = document.querySelector('.pipe');

const jump = () => {
  cat.classList.add('jump');

  setTimeout(() => {
    cat.classList.remove('jump');
  }, 500);
}

const loop = setInterval(() => {

  console.log('loop')
  
  const pipePosition = pipe.offsetLeft;
  const catPosition = +window.getComputedStyle(cat).bottom.replace('px', '');
    
if (pipePosition <= 38 && pipePosition > 0 && catPosition < 80) { 

    pipe.style.animation = 'none';
    pipe.style.left = `${pipePosition}px`;

    cat.style.animation ='none';
    cat.style.bottom = `${catPosition}px`;

    cat.src = 'images/game-over.png';
    cat.style.width = '100px';
    cat.style.marginLeft = '0px';

    clearInterval(loop);
    

  }
} , 10);
  
document.addEventListener('keydown' , jump);