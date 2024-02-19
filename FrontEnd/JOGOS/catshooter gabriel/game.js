window.onload = function() {
    var canvas = document.getElementById('gameCanvas');
    var ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    var player = {
        x: canvas.width / 2,
        y: canvas.height - 50,
        size: 50,
        color: 'blue'
    };

    var zombies = [];
    var zombieSize = 30;
    var spawnRate = 1000;
    var lastSpawn = -spawnRate;
    var speed = 3;
    var life = 100; // Vida inicial
    var shots = 100; // Tiros iniciais

    function spawnZombie() {
        var zombieType = Math.random();
        var zombieSpeed;
        var zombieDamage;

        if (zombieType < 0.33) {
            // Zombie rápido
            zombieSpeed = speed * 2;
            zombieDamage = 1;
        } else if (zombieType < 0.66) {
            // Zombie lento
            zombieSpeed = speed / 2;
            zombieDamage = 2;
        } else {
            // Zombie parado
            zombieSpeed = 0;
            zombieDamage = 4;
            var damageInterval = setInterval(function() {
                if (zombies.length > 0) {
                    life -= zombieDamage;
                    console.log('Você levou ' + zombieDamage + ' de dano! Vida restante: ' + life);
                    if (life <= 0) {
                        console.log('Game over! Tiros totais disparados: ' + (100 - shots));
                        clearInterval(damageInterval);
                        return;
                    }
                }
            }, 2500); // A cada 2.5 segundos
        }

        var zombie = {
            x: Math.random() * (canvas.width - zombieSize),
            y: 0,
            size: zombieSize,
            speed: zombieSpeed,
            damage: zombieDamage,
            color: 'green'
        };
        zombies.push(zombie);
    }

    function drawText(text, x, y, color, size) {
        ctx.fillStyle = color;
        ctx.font = size + 'px Arial';
        ctx.fillText(text, x, y);
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = player.color;
        ctx.fillRect(player.x, player.y, player.size, player.size);

        drawText('Vidas: ' + life, 20, 40, 'white', 24);
        drawText('Tiros restantes: ' + shots, 20, 80, 'white', 24);

        var time = Date.now();
        if (time > (lastSpawn + spawnRate)) {
            lastSpawn = time;
            spawnZombie();
        }

        for (var i = 0; i < zombies.length; i++) {
            var zombie = zombies[i];
            zombie.y += zombie.speed;

            ctx.fillStyle = zombie.color;
            ctx.fillRect(zombie.x, zombie.y, zombie.size, zombie.size);

            if (zombie.y > canvas.height - player.size) {
                zombies.splice(i, 1);
                i--;
                life -= zombie.damage;
                console.log('Você levou ' + zombie.damage + ' de dano! Vida restante: ' + life);
                if (life <= 0) {
                    console.log('Game over! Tiros totais disparados: ' + (100 - shots));
                    return;
                }
            }
        }

        requestAnimationFrame(animate);
    }

    canvas.addEventListener('click', function(event) {
        var rect = canvas.getBoundingClientRect();
        var x = event.clientX - rect.left;
        var y = event.clientY - rect.top;
        for (var i = 0; i < zombies.length; i++) {
            var zombie = zombies[i];
            if (x > zombie.x && x < zombie.x + zombie.size && y > zombie.y && y < zombie.y + zombie.size) {
                zombies.splice(i, 1);
                i--;
                shots--;
                console.log('Zumbi abatido! Tiros restantes: ' + shots);
            }
        }
    });

    animate();
}