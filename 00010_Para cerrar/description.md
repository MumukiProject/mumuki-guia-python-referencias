Antes de terminar nos topamos con un último problema: Jazmín toca el piano familiar, pero con el uso se va desafinando, y Lucio, el afinador, tiene que afinarlo. En particular:

* Cada vez que Jazmin toca, el nivel de afinación del piano **(inicialmente en 100)** baja en un 1%
* El piano está afinado si su nivel de afinación está por encima del 80%
* Cada vez que Lucio afina al piano, su nivel de afinación aumenta tanto como tiempo le dedique: 5% por cada hora. Y nunca se pasa del 100%, claro.

> Desarrollá los objetos necesarios para que podamos hacer lo siguiente:
>
> ```python
> #Configura al piano de Jazmin
> Jazmin.piano=(PianoFamiliar)
> Jazmin.tocar
> #Pregunta si está afinado
> PianoFamiliar.esta_afinado?
> #Lo afina durante 3 horas
> Lucio.afinar(PianoFamiliar, 3)
> ```
