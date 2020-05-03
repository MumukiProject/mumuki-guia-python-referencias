def test_"La nieta de AbueloGervasio es Melisa":
  expect(AbueloGervasio.nieta).to be Melisa


def test_"La novia de Fito es Melisa":
  expect(Fito.novia).to be Melisa


def test_"Melisa aumentó su felicidad":
  expect(Melisa.felicidad > 100).to be True


def test_"Fito es feliz porque Melisa es feliz":
  expect(Fito.es_feliz_como_su_novia?).to be True


def test_"AbueloGervasio alimentó 3 veces a Melisa":
  expect(AbueloGervasio.veces_alimentada).to eq 3
