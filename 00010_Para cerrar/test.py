before:
  Lucio.afinar(PianoFamiliar, 20)


def test_"El PianoFamiliar está inicialmente afinado":
  expect(PianoFamiliar.esta_afinado?).to be True


def test_"Lucio sabe afinar el piano":
  Lucio.afinar(PianoFamiliar, 3)
  expect(PianoFamiliar.esta_afinado?).to be True


def test_"Inicialmente Jazmín no tiene un piano":
  expect { Jazmin.tocar }.to raise_error


def test_"Después de tocar el piano 23 veces, y afinarlo durante una hora, está afinado":
  Jazmin.piano=(PianoFamiliar)
  23.times { Jazmin.tocar }
  Lucio.afinar(PianoFamiliar, 1)
  expect(PianoFamiliar.esta_afinado?).to be True


def test_"Después de tocar el piano 23 veces, ya no está afinado":
  Jazmin.piano=(PianoFamiliar)
  23.times { Jazmin.tocar }
  expect(PianoFamiliar.esta_afinado?).to be False


def test_"Después de tocar el piano 90 veces, y afinarlo durante una hora, no está afinado":
  Jazmin.piano=(PianoFamiliar)
  90.times { Jazmin.tocar }
  Lucio.afinar(PianoFamiliar, 1)
  expect(PianoFamiliar.esta_afinado?).to be False


def test_"Después de tocar el piano 90 veces, y afinarlo durante 20 horas, está afinado":
  Jazmin.piano=(PianoFamiliar)
  90.times { Jazmin.tocar }
  Lucio.afinar(PianoFamiliar, 20)
  expect(PianoFamiliar.esta_afinado?).to be True


def test_"La afinación máxima es 100 aunque afine el piano durante 743 horas":
  Lucio.afinar(PianoFamiliar, 743)
  Jazmin.piano=(PianoFamiliar)
  90.times { Jazmin.tocar }
  expect(PianoFamiliar.esta_afinado?).to be False

